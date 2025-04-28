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

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image for the application
                    sh 'docker build -t ${DOCKER_REGISTRY}/${IMAGE_NAME}:latest .'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Run SonarQube analysis for code quality checks
                    sh """
                    sonar-scanner \
                        -Dsonar.projectKey=${SONARQUBE_PROJECT_KEY} \
                        -Dsonar.projectName=${SONARQUBE_PROJECT_NAME} \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=${SONARQUBE_URL}
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests (adjust this according to your stack)
                    // Example: if Node.js, run `npm install && npm test`
                    echo 'Running tests...'
                }
            }
        }

        stage('Push Docker Image to Registry') {
            steps {
                script {
                    // Log in to Docker registry
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'

                    // Push the built Docker image to Docker registry
                    sh 'docker push ${DOCKER_REGISTRY}/${IMAGE_NAME}:latest'
                }
            }
        }

        stage('Deploy to EKS with ArgoCD') {
            steps {
                script {
                    // Set up kubectl to interact with AWS EKS cluster
                    sh 'aws eks --region ${AWS_REGION} update-kubeconfig --name ${EKS_CLUSTER}'

                    // Sync the application using ArgoCD for deployment
                    sh 'argocd app sync ${ARGOCD_APP_NAME} --auth-token <argo-auth-token>'
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
