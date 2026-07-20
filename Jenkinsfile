pipeline {
    agent any 
    stages {
        stage('Clone the repo') {
            steps {
                git branch: "main",
                url: "https://github.com/Dheerajmadhukar/ditisssssssss"
            }
        }
        stage('Run docker container with ditisss project') {
            steps {
                sh """
                sudo docker rm -f demo1server
                sudo docker run -d --name demo1server -p 80:80 -v /var/lib/jenkins/workspace/ss:/usr/local/apache2/htdocs httpd:latest 
                """
            }
        } 
    }
}
