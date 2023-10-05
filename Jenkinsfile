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

    stage('Log into Dockerhub') {
      environment {
        DOCKERHUB_USER = 'shivansh15'
        DOCKERHUB_PASSWORD = '@microprocessor#'
      }
      steps {
        sh '''docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASSWORD
'''
      }
    }

    stage('Push to Dockerhub') {
      steps {
        sh 'docker push cvapp:latest'
      }
    }

  }
}