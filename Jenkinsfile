pipeline {
    agent any 
    stages {
        stage('Clone the repo') {
            steps {
                git branch: "main",
                url: "https://github.com/Dheerajmadhukar/ditisssssssss"
            }
        }
        stage('Shift-left SAST') {
            steps {
                sh """
                cd /var/lib/jenkins/workspace/ss
                pysonar --sonar-host-url=http://18.133.65.127:9000 --sonar-token=sqp_c321da032730b322c7f07e7dfc0b2d05508a8d75 --sonar-project-key=demo1_ci
                """
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
