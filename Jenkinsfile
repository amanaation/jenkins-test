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
                sh 'ls -la'
                sh 'pip -V'
                sh 'chown -R jenkins:jenkins /usr/local/lib/python3.7/site-packages/pip  '
                sh '/usr/local/lib/python3.7/site-packages/pip install  --user python-dotenv '
                sh 'pip3 install --no-cache-dir --user requests'
                sh 'python3  github_Actions.py'
            }
        }

    }
}