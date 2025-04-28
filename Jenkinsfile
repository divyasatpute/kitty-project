pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', credentialsId: 'git-cred', url: 'https://github.com/divyasatpute/kitty-project.git'
            }
        }

        stage('Docker Build & Tag ') {
            steps {
                script{
                   withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker') {

                sh 'docker build -t divyasatpute/kitty:latest . --no-cache '
                   }
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar-server') {
                sh '''$SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=kitty -Dsonar.projectKey=kitty \
                 -Dsonar.java.binaries=target'''
               }
            }
        }

        stage('Docker Push') {
            steps {
                script{
                   withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker') {

                sh 'docker push divyasatpute/kitty:latest'
                   }
                }
            }
        }

        stage('Post-Build Actions') {
            steps {
                script {
                    // Notify build success/failure (you can integrate email or Slack here)
                    echo "Pipeline completed successfully!"
                }
            }
        }
    }

    post {
        always {
            // Clean up unused Docker images after the build
            sh 'docker system prune -f'
        }
    }
}
