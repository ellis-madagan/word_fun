pipeline {
  agent any
  stages {
    stage('Ensure Files Exist') {
      steps {
        fileExists 'word_fun.py'
        fileExists 'word_fun_test.py'
      }
    }
  }
}