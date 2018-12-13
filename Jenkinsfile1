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
    stage('notify') {
      steps {
        echo 'notify'
        sh '''gitmessage=$(git log --format=%B -n 1)
python fastlane/dingding.py -r https://oapi.dingtalk.com/robot/send?access_token=febcd5e36d19097f93c9afbe5b72d6015381d8682cb0be24ed00deeb239315bd -m "${gitmessage}"'''
      }
    }
  }
  post {
    failure {
      node('master') {
        echo 'failure'
        sh '''gitmessage=$(git log --format=%B -n 1)
python fastlane/dingding.py -t fail -r https://oapi.dingtalk.com/robot/send?access_token=febcd5e36d19097f93c9afbe5b72d6015381d8682cb0be24ed00deeb239315bd -m ${gitmessage}'''
      }
    }
  }
}