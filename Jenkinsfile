pipeline {
    agent none
    stages {
        stage('test on mac') {
            agent { 
                label 'master'
            }
            steps {
              echo 'hello mac' 
            }
        }
        stage('test on windows') {
            agent { 
                label 'win-test'
            }
            steps {
                echo 'hello windows'
            }
        }
    }
}