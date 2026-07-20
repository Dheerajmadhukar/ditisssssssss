pipeline {
    agent any 
    stages {
        stage('Hello World Stage') {
            steps {
                echo 'Hello World!'
            }
         stage('Check uname') {
             step {
                 sh 'uname -a'
             }
         }
        }
    }
}
