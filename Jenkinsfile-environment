pipeline {
  agent any
  environment { 
    AA = 'Hello'
  }
  stages {
    stage('test') {
      environment { 
        BB = 'World'
      }
      steps {
        echo "${env.AA} ${env.BB}"
        echo "Running on ${env.JENKINS_URL}"
      }
    }
  }
}