pipeline {
    agent any
    environment {
        SONAR_HOME = tool "Sonar"
        GITHUB_USERNAME = 'Bakhtawarkhan90'   // GitHub username used in the pipeline
    }
    stages {
        stage("Workspace Clean-up") {
            steps {
                script {
                    // Clean the workspace before starting a new build
                    cleanWs()
                }
            }
        }
        stage("Cloning Code") {
            steps {
                // Clone the application source code from GitHub
                git url: "https://github.com/Bakhtawarkhan90/Tailstore.git", branch: "main"
            }
        }
        stage("Sonarqube Code Analysis") {
            steps {
                // Run SonarQube analysis on the project
                withSonarQubeEnv("Sonar") {
                    sh "$SONAR_HOME/bin/sonar-scanner -Dsonar.projectName=Tailstore -Dsonar.projectKey=Tailstore -X"
                }
            }
        }
        stage("Download SonarQube Report") {
            steps {
                script {
                    // Download SonarQube metrics report as JSON
                    sh """
                    curl -u admin:admin "192.168.31.33:9000/api/measures/component?component=Bistro&metricKeys=bugs,vulnerabilities,code_smells,coverage,duplicated_lines_density" -o sonar-report.json
                    """
                }
            }
        }
        stage("Docker Image Building") {
            steps {
                // Build the Docker image for the application
                sh "docker build . -t bakhtawar375/tailstore:latest"
            }
        }
        stage('Trivy Image Scanning') {
            steps {
                echo "Trivy Image Scanning"
                // Scan the Docker image for vulnerabilities
                retry(3) {
                    sh 'trivy image bakhtawar375/tailstore:latest || sleep 60'
                }
            }
        }
        stage("Push Docker-Hub") {
            steps {
                withCredentials([usernamePassword(credentialsId: "dockerHub", passwordVariable: "dockerHubPass", usernameVariable: "dockerHubUser")]) {
                    // Log in to Docker Hub using stored credentials
                    sh "echo \\$dockerHubPass | docker login -u \\$dockerHubUser --password-stdin"
                   // Tagging can be added here if needed before pushing
                    sh "docker push ${env.dockerHubUser}/tailstore:latest"
                }
            }
        }
        stage("Run Docker Container ") {
            steps {
                // Stop existing containers and start the updated application
                sh " docker compose down & docker compose up -d --build"
            }
        }
    }
    post {
        success {
            // Send email when the pipeline succeeds
            mail to: 'royalbakhtawar@gmail.com',
                subject: "Pipeline Success: ${currentBuild.fullDisplayName}",
                body: "The Pipeline '${env.JOB_NAME}' has successfully completed.\n" +
                      "Check it here: ${env.BUILD_URL}"
        }
        failure {
            // Send email when the pipeline fails
            mail to: 'royalbakhtawar@gmail.com',
                subject: "Pipeline Failed: ${currentBuild.fullDisplayName}",
                body: "The Pipeline '${env.JOB_NAME}' has failed.\n" +
                      "Check it here: ${env.BUILD_URL}"
        }
    }
}
