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
            echo 'PIPELINE THANH CONG!'
        }

        failure {
            echo 'PIPELINE THAT BAI!'
        }

        always {
            echo 'Jenkins pipeline finished.'
        }
    }
}