
pipeline{
    agent any
    environment{

        def name='tjdetwill007/mycloudapp:latest'
        AWS_CREDENTIALS=credentials('AwsCred')

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
                    script{

                        def awsEnv = [
                        AWS_ACCESS_KEY_ID: AWS_CREDENTIALS.AWSAccessKeyId,
                        AWS_SECRET_ACCESS_KEY: AWS_CREDENTIALS.AWSSecretKey
                    ]
                    createDeployment(applicationName: 'mycloudapp',
                              deploymentGroupName: 'mycloudappgroup',
                              deploymentConfigName: 'CodeDeployDefault.OneAtATime',
                              s3Bucket: 'testbucket1sept2023',
                              s3BundleType:"zip",
                              s3Key:"artifact.zip",
                              fileExistsBehavior: 'OVERWRITE',
                              environmentVariables: awsEnv
                              )
                            }
                
            }
        }
   }
}