pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh 'fastlane test'
      }
    }

    stage('build') {
      steps {
        sh 'fastlane build'
      }
    }

    stage('deploy') {
      steps {
        sh 'fastlane deploy'
      }
    }
  }
}