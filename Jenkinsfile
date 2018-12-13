pipeline {
    agent any
    parameters {
        string(name: 'PERSON', defaultValue: 'Catch Zeng', description: 'Who should I say hello to?')
    }
    stages {
        stage('Example') {
            steps {
                echo "Hello ${params.PERSON}"
            }
        }
    }
}