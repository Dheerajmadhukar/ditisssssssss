pipeline {
    agent any 
    stages {
        stage('Hello World Stage') {
            steps {
                echo 'Hello World!'
            }
         stage('Check uname') {
             steps {
                 sh 'uname -a'
             }
         }
        }
    }
}
