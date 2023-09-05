function test(){
    alert('test');
}
function register(){
    let current_url = window.location.href;
    console.log(current_url);
    window.location.href = current_url+'register'
}
function formvalidation(){
    debugger;
    var username=document.getElementById('username').value;
    var useremail=document.getElementById('useremail').value;
    var password=document.getElementById('userpassword').value;
    var re_password=document.getElementById('re_password').value;
    var error=document.getElementById('errorMsgBlock');
    var errorMsg=document.getElementById('errorMsg');
    var hasError=false;
    

    if (username==undefined || useremail ==undefined || password==undefined || 
        re_password==undefined || username=="" || useremail =="" || 
        password=="" || re_password==""){
        errorMsg.innerText="Fields can't be blank";
        hasError=true;
        
    }
    if(!hasError && password != re_password){
        errorMsg.innerText="Password didn't match";
        hasError=true;
    }

    if (hasError){
        error.style.display = 'block';
        return false;
    }
    
}