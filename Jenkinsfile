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
                sh 'python -m py_compile github_Actions.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
    }
}