pipeline {
    agent none
    stages {
        stage('build') {
            parallel {
                stage('mac') {
                    agent {
                        label 'master'
                    }
                    steps {
                        echo 'build on mac'
                    }
                }
                stage('windows') {
                    agent {
                        label 'win-test'
                    }
                    steps {
                        echo 'build on windows'
                    }
                }
            }
        }
    }
}