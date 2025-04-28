![ChatGPT Image Apr 29, 2025, 12_13_21 AM](https://github.com/user-attachments/assets/5cc1dd6a-8907-40ba-84a2-35fffdd0ff8d)


# 🐾 Kitty Project

Welcome to the **Kitty Project** — a modern, scalable, and cloud-native web application fully automated with industry-standard DevOps practices.

This project demonstrates how to **build, test, secure, and deploy** a production-grade application on **AWS EKS** using a complete CI/CD pipeline with **Jenkins**, **SonarQube**, **Docker**, **Terraform**, and **ArgoCD**.

---

## 📚 Project Structure

| Layer          | Technology                     | Purpose                        |
|----------------|---------------------------------|--------------------------------|
| Infrastructure | Terraform                      | EKS Cluster, VPC, IAM Roles    |
| CI/CD          | Jenkins, SonarQube, Docker      | Build, Test, Quality Scan, Push|
| Deployment     | Kubernetes, ArgoCD              | GitOps-Based Automated Deployments |
| Monitoring     | (Planned) Prometheus, Grafana   | Observability (Optional future scope) |

---

## 🚀 Workflow Overview

1. **Infrastructure**:  
   - Provision AWS VPC, EKS Cluster, IAM, Networking using Terraform.

2. **Source Code Management**:
   - Host application code on GitHub.

3. **Continuous Integration (CI)**:
   - Jenkins Pipeline:
     - Checkout source code
     - Build Docker image
     - Perform static code analysis using SonarQube
     - Run unit tests
     - Push Docker image to DockerHub (or ECR)

4. **Continuous Deployment (CD)**:
   - Update Kubernetes manifests
   - Use ArgoCD to deploy to EKS automatically (GitOps)

5. **Post-Build**:
   - Clean up docker resources
   - Send build notifications (optional)

---

## 🔧 Tools and Technologies

- **Cloud**: AWS (EKS, IAM, VPC, EC2, S3)
- **Containerization**: Docker
- **Orchestration**: Kubernetes (EKS)
- **GitOps**: ArgoCD
- **CI Server**: Jenkins
- **Static Code Analysis**: SonarQube
- **Infrastructure as Code**: Terraform
- **Monitoring (Future)**: Prometheus + Grafana

---

## 🛠️ Prerequisites

- AWS Account
- Terraform installed
- Docker installed
- Kubernetes CLI (`kubectl`) installed
- Jenkins Server configured
- SonarQube Server running
- ArgoCD Server configured

---
![image](https://github.com/user-attachments/assets/b0cd43ef-3b94-4def-89ce-6bbd685f8637)


![image](https://github.com/user-attachments/assets/e7e4fc5f-4426-4b3b-81ec-34999ac7dd0f)


