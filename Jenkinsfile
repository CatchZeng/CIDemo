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
        stage('catch') {
            when {
              allOf {
                branch 'master'
                expression {
                  shortCommit = sh(returnStdout: true, script: "git log --format=%B -n 1").trim()
                  echo "${shortCommit}"
                  return shortCommit =~ /catch/
                }
              }
            }
            steps {
              echo 'catch'
            }
        }
    }
}