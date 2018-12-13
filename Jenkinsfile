pipeline {
  agent any
  stages {
    stage('Example') {
      steps {
        echo 'Hello World'
      }
    }
  }
  post { 
    always { 
      echo 'I will always say Hello again!'
    }
    failure {
      echo 'failure'
    }
    success {
      echo 'success'
    }
  }
}