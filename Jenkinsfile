pipeline {
  agent any
  stages {
    stage('Code Checkout') {
      steps {
        git(url: 'https://github.com/Codeansh/Resume_Builder', branch: 'Main')
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t cvapp  .'
      }
    }

  }
}