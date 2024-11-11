pipeline {
    agent any

    environment {
        BACKEND_SERVICE = "http://backend:8000"  // URL do serviço FastAPI na rede Docker
    }

    stages {
        stage('Clonar o Repositório') {
            steps {
                git 'https://github.com/calel95/sistema_de_rifa.git'
            }
        }

        stage('Construir Imagens Docker') {
            steps {
                script {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Subir Serviços com Docker Compose') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Esperar Backend') {
            steps {
                script {
                    // Aguardar até que a API do FastAPI esteja disponível
                    retry(5) {
                        sh "sleep 10"
                        sh "curl --fail ${BACKEND_SERVICE}/docs || exit 1"
                    }
                }
            }
        }

        stage('Verificar API com GET') {
            steps {
                script {
                    // Faz uma requisição GET à API FastAPI
                    sh "curl -X GET ${BACKEND_SERVICE}/numeros"
                }
            }
        }
    }

    post {
        always {
            echo 'Finalizando Pipeline'
            sh 'docker-compose down'
        }
    }
}
