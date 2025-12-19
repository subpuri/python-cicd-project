pipeline {
  agent any

  environment {
    AWS_REGION = "us-east-1"
    ECR_REPO   = "837832656548.dkr.ecr.us-east-1.amazonaws.com/infraops-automator"
    IMAGE_TAG  = "${BUILD_NUMBER}"
  }

  stages {

    stage("Checkout") {
      steps {
        checkout scm
      }
    }

    stage("Test") {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install -r app/requirements.txt
          pytest
        '''
      }
    }

    stage("Build Docker Image") {
      steps {
        sh '''
          docker build -t infraops-automator:${IMAGE_TAG} .
          docker tag infraops-automator:${IMAGE_TAG} ${ECR_REPO}:${IMAGE_TAG}
        '''
      }
    }

    stage("Push to ECR") {
      steps {
        withCredentials([aws(credentialsId: 'aws-creds')]) {
          sh '''
            aws ecr get-login-password --region $AWS_REGION | \
            docker login --username AWS --password-stdin 837832656548.dkr.ecr.us-east-1.amazonaws.com

            docker push ${ECR_REPO}:${IMAGE_TAG}
          '''
        }
      }
    }

    stage("Deploy to Kubernetes") {
      steps {
        withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
          sh '''
            sed -i "s|image:.*|image: ${ECR_REPO}:${IMAGE_TAG}|" k8s/deployment.yaml
            kubectl apply -f k8s/deployment.yaml
            kubectl apply -f k8s/service.yaml
          '''
        }
      }
    }
  }

  post {
    success {
      echo "🚀 Deployment successful!"
    }
    failure {
      echo "❌ Pipeline failed"
    }
  }
}
