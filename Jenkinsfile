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
                sh 'python3 -m venv venv '
                sh 'source venv/bin/activate '
                sh 'ls -la'
                sh 'w'
                sh 'mkdir /.local'
                sh 'ls -la /.local'
                sh 'pip3 -V'
                sh 'pip3 install --user python-dotenv '
                sh 'pip3 install --user requests --user'
                sh 'python3  github_Actions.py'
            }
        }

    }
}