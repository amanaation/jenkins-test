pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh 'sudo python3 -m venv .venv '
                sh 'sudo source .venv/bin/activate'
                sh 'sudo pip3 install -r requirements.txt'
                sh 'sudo python3  github_Actions.py'
            }
        }

    }
}