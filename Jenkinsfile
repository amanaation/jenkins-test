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
                sh '/usr/local/bin/python -m pip install --upgrade pip'
                sh 'ls -la'
                sh 'pip -V'
                sh 'pip install --user python-dotenv '
                sh 'pip install --user requests'
                sh 'python3  github_Actions.py'
            }
        }

    }
}