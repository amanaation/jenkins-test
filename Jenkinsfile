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
                sh 'python3 -m venv .venv '
                sh 'source .venv/bin/activate'
                sh 'pip3 install -r requirements.txt'
                sh 'python3  github_Actions.py'
                # stash(name: 'compiled-results', includes: '*.py*')
            }
        }

    }
}