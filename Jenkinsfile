pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.7-alpine'
                }
            }
            steps {
                sh 'python3 -m venv .venv '
                sh 'source ./.venv/bin/activate '
                sh 'pip3 install --user -r requirements.txt'
                sh 'python3  github_Actions.py'
            }
        }

    }
}