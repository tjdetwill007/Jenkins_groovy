
pipeline{
    agent any
    environment{

        def name='tjdetwill007/mycloudapp:latest'

    }
    stages{
        stage("Clone code"){
            steps{
                git url: "https://github.com/tjdetwill007/Jenkins_groovy.git", branch: "master"
            }
        }
        stage("build"){
            steps{
                echo "Entered to build stage"
                sh "sudo docker build -t ${name} ."
                echo "Successfully built the image Now pushing to Docker Hub"
                sh "sudo docker push ${name}"
            }
        }
        stage("Uploading to s3"){
            steps{
                echo "Creating Pacakge to upload"
                sh "zip -j artifact/artifact.zip artifact/* -x upload.py"
                sh "sudo yum install pip -y"
                sh "sudo pip install boto3"
                sh "python artifact/upload.py"
                echo "Successfully Uploaded the artifact to S3"
                echo "Proceeding to Cleanup"
                sh "sudo rm -f artifact/artifact.zip"
            }
        }

        stage("Deploy"){
            steps{
                    awsCodeDeploy(applicationName: 'mycloudapp',
                              deploymentGroup: 'mycloudappgroup',
                              deploymentConfig: 'CodeDeployDefault.OneAtATime',
                              bucketName: 'testbucket1sept2023',
                              fileExistsBehavior: 'OVERWRITE',
                              sourceFolder: '/',
                              subdirectory: 'artifact.zip',
                              region: 'us-east-1')
                
            }
        }
}