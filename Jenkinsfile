pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.7-slim-buster'
                }
            }
            steps {
                sh 'python3 -m venv .venv '
                sh 'source .venv/bin/activate '
                sh 'ls -la'
                sh 'pip3 -V'
                sh 'sudo pip3 install python-dotenv --user'
                sh 'pip3 install requests --user'
                sh 'python3  github_Actions.py'
            }
        }

    }
}