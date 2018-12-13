pipeline {
  agent any
  environment { 
      CC = 'clang'
  }
  stages {
      stage('Example') {
          environment { 
              AN_ACCESS_KEY = credentials('my-prefined-secret-text') 
          }
          steps {
              sh 'printenv'
              echo '${CC}'
              echo '${AN_ACCESS_KEY}'
          }
      }
  }
}