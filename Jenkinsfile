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
                sh 'python3 -m venv .venv ||
                source .venv/bin/activate ||
                pip3 install -r requirements.txt ||
                python3  github_Actions.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }

    }
}