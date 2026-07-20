pipeline {
    agent any 
    stages {
        stage('Hello World Stage') {
            steps {
                echo 'Hello World!'
            }
        }
        stage('check docker version'){
            steps {
                sh """
                sudo docker --version
                """
            }
        }
    }
}
