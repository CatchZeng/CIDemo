pipeline {
  agent any
  stages {
    stage('branch') {
      when {
        branch 'master'
      }
      steps {
        echo 'Hello World on master branch'
      }
    }
    stage('branch release') {
      when {
        branch 'release'
      }
      steps {
        echo 'Hello World on release branch'
      }
    }
  }
}