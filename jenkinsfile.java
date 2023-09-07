
pipeline{
    agent any
    environment{

        def name='tjdetwill007/mycloudapp:latest'
        // def docker=credentials('a750fad4-d124-4d6c-9e2e-84c6f29f64c0')
   

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
                // echo "Logging in to Docker HUB"
                // sh "sudo docker login --username ${docker_USR} --password ${docker_PSW}"
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

                    withAWS(credentials: 'AwsCred', region: 'us-east-1') {

    // some block
                    def myBooleanParam = true
                    createDeployment(applicationName: 'mycloudapp',
                              deploymentGroupName: 'mycloudappgroup',
                              deploymentConfigName: 'CodeDeployDefault.OneAtATime',
                              s3Bucket: 'testbucket1sept2023',
                              s3BundleType:"zip",
                              s3Key:"artifact.zip",
                              fileExistsBehavior: 'OVERWRITE'                          
                              )
                            }
                    }
                
            }
        }
   }
}