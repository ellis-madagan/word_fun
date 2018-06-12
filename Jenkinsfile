pipeline {
  agent any
  stages {
    stage('Ensure Files Exist') {
      steps {
        fileExists 'word_fun.py'
        fileExists 'word_fun_test.py'
      }
    }
    stage('Run Unit Tests') {
      steps {
        sh 'py -m pytest --junitxml results.xml word_fun_test.py'
      }
    }
    stage('Report Test Results') {
      steps {
        junit 'results.xml'
      }
    }
  }
}