from flask import Flask, render_template,request, session
from dblogin import *
from s3 import *



app = Flask(__name__)
app.secret_key = 'your secret key'



@app.route('/', methods=['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'emailId' in request.form and 'usr-password' in request.form: #checking if the form is filled
        # Connection to db
        user_email=request.form['emailId']
        user_password=request.form['usr-password']
        response = dbfun(user_email,user_password)
        if response:
            session['loggedin']= True
            session['id']=response['id']
            session['username']=response['username']
            return render_template('index.html')              
        else:
            msg="Invalid email or password!"    
    return render_template('login.html',msg=msg)


@app.route('/register', methods=['GET','POST'])
def register():
    msg=''
    if (request.method == 'POST' and 'username' in request.form 
        and 'userpassword' in request.form and 'useremail' in request.form 
        and 're_password' in request.form):
        
        username=request.form['username']
        userpassword=request.form['userpassword']
        useremail=request.form['useremail']
        response=dbcreate(username,userpassword,useremail)
        if response == 0:
            msg="Account already exist!"
            return render_template('register.html',msg=msg)
        createbucket(username)
        return render_template('register.html', msg="Registered successfully")
    
    return render_template('register.html',msg=msg)
    



# s3 = boto3.client('s3', region_name="us-east-1")
# @app.route('/')
# def hello():
#     return render_template("index.html")
#     # return 'Hello, World!'
# @app.route('/upload', methods=['POST'])
# def upload():
#     if 'photo' not in request.files:
#         return "No photo uploaded", 400

#     photo = request.files['photo']
#     if photo.filename == '':
#         return "No selected photo", 400
    
#     ## Generate Pre-signed URL
#     presigned_url = s3.generate_presigned_url(
#     ClientMethod='put_object',
#     Params={
#         'Bucket': "mywebservicetest",
#         'Key': photo.filename,
#     },
#     ExpiresIn=3600)
#     print(presigned_url)
   

#     ##Upload object using pre-signed url's
#     response = requests.put(presigned_url, data=photo.filename)

#     ## Below is previous method for uploading using aws keys.
#     # s3.upload_fileobj(photo, S3_BUCKET, photo.filename) 

#     return render_template("uploaded.html")
# @app.route('/getdetails', methods=['GET'])
# def getdetails():
#     data = requests.get("https://3abbqzj227.execute-api.us-east-1.amazonaws.com/prod/lambda")
#     print(data)
#     maindata = data.json()
#     print(maindata)
#     maindata=json.loads(maindata)
#     return render_template("final.html", result=maindata)




app.run(port=80)