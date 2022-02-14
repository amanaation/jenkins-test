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
                sh 'pip -V'
                sh 'pip install --no-cache-dir --user python-dotenv '
                sh 'pip install --no-cache-dir --user requests'
                sh 'python3  github_Actions.py'
            }
        }

    }
}