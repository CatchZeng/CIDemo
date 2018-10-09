pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh '''export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
fastlane test'''
      }
    }
    stage('build') {
      steps {
        sh '''export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
fastlane build'''
      }
    }
    stage('deploy') {
      steps {
        sh '''export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
fastlane deploy'''
      }
    }
  }
}