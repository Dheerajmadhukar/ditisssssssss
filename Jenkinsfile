pipeline {
    agent any 
    stages {
        stage('Hello World Stage') {
            steps {
                echo 'Hello World!'
            }
        }
        stage('Run linux command'){
            steps {
                sh """
                uname -a
                """
            }
        }
    }
}
