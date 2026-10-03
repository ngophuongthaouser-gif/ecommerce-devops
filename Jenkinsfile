pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo '=== CHECKOUT ==='
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                echo '=== SETUP PYTHON ==='

                sh '''
                    python3 --version
                    python3 -m venv .venv
                    .venv/bin/pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Django Check') {
            steps {
                echo '=== DJANGO CHECK ==='

                sh '''
                    .venv/bin/python manage.py check
                '''
            }
        }
    }

    post {
        success {
            echo '========================================'
            echo 'PIPELINE THANH CONG!'
            echo 'Django system check OK!'
            echo '========================================'
        }

        failure {
            echo '========================================'
            echo 'PIPELINE THAT BAI!'
            echo '========================================'
        }

        always {
            echo 'Jenkins pipeline finished.'
        }
    }
}