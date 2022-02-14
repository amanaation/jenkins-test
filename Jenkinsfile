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
            withEnv(["HOME=${env.WORKSPACE}"]) {
                sh 'ls -la'
                sh 'pip -V'
                sh 'pip install  --user python-dotenv '
                sh 'pip3 install --no-cache-dir --user requests'
                sh 'python3  github_Actions.py'
            }
            }
        }

    }
}