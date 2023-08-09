# Microservices Web App Deployment

This repository contains a web app that consumes URLs from environment variables, sends API requests and returns responses. The app is deployed on a Kubernetes cluster, using Helm and GitHub Actions.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Deploying Kubernetes Cluster](#deploying-kubernetes-cluster)
  - [Creating Git Repository](#creating-git-repository)
  - [Setting Up Microservices](#setting-up-microservices)
  - [GitHub Action Workflow](#github-action-workflow)
- [Usage](#usage)

## Prerequisites

- Kubernetes cluster (you can use a local cluster, such as Minikube, k3s, Docker Desktop, or a cloud provider's managed Kubernetes service).
- DockerHub account & repository for pushing Docker images.
- GitHub repository.

## Getting Started

### Deploying Kubernetes Cluster

Set up and configure a Kubernetes cluster according to your preferred platform's documentation.

### Creating GitHub Repository

1. Create a new GitHub repository.
2. Clone the repository to your local machine.

### Codebase & Dockerfile

You'll find the codebase and the Dockerfile in the repository's root directory.
   - `webApp.py`: The Python web app that consumes URLs and returns responses based on routes.
   - `Dockerfile`: Dockerfile that wraps the app into an image with the relevant requierments.

### Helm Chart

Inside the `helm` directory, you'll find the webapp chart. The chart contains the following files:
   - `Chart.yaml` - set the chart name (webapp) & version (1.0.0).
   - `uselessfact-values.yaml` - values file which will route the request to `https://uselessfacts.jsph.pl/random.json`.
   - `funnyfact-values.yaml` - values file which will route the request to `https://api.chucknorris.io/jokes/random`.
   - `templates/deployment.yaml` - creates the pod which contains the webapp and its' replicas.
   - `templates/hpa.yaml` - horizontally scales the pod replicas based on cpu demand.
   - `templates/pdb.yaml` - protects the application by limiting the disruption of the pods in rescheduling times.

### GitHub Action Workflow

1. Inside the `.github/workflows` directory, you'll find the `webapp.yml` file.
2. The workflow performs the below actions:
   - Pull the source code from the Git repository.
   - Build a Docker image and tag it with a build number.
   - Push the image to the DockerHub repository.
   - Deploy the service on the Kubernetes cluster using Helm (both services in the same namespace) with the correct environment variable which represents the microservice with the relevant route.
   -  Run tests to verify that the requests are responding correctly to all routes.

## Usage

The microservices can be deployed manually, using Helm (CLI) or GitHub Actions:
 - Deploy the microservices using Helm (CLI) - don't forget to change <SERVICE_NAME>, <DOCKER_REPO_NAME> and <IMAGE_TAG> with the relevant parameters:
   ```sh
   helm upgrade --install <SERVICE_NAME> webapp -n webapp -f ./webapp/<SERVICE_NAME>-values.yaml --set service.image.repository='<DOCKER_REPO_NAME>',service.image.tag=<IMAGE_TAG> --create-namespace
 - Trigger deployment from GitHub: 
   - Go to the GitHub repository and navigate to the `Actions` tab. 
   - Choose the workflow named `webapp workflow` and run it. 
   - Provide the service name as a parameter.