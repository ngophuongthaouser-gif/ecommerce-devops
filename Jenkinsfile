pipeline {
    agent any

    stages {

        stage('Test') {
            steps {
                echo 'Jenkins da ket noi voi project Ecommerce!'
                echo 'Pipeline dang chay thanh cong!'

                bat '''
                    .venv\\Scripts\\python.exe manage.py check
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
            echo 'Hay kiem tra log ben tren.'
            echo '========================================'
        }

        always {
            echo 'Jenkins pipeline finished.'
        }
    }
}