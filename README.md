# Deploying a Spark Job on Kubernetes with Argo Workflows

This guide walks you through deploying a Spark job on a Kubernetes cluster using Argo Workflows.

## Prerequisites

1. **Kubernetes Cluster**: Ensure you have a running Kubernetes cluster. (e.g., using [Kind](https://kind.sigs.k8s.io/) or a cloud provider).
2. **Helm**: Install Helm for managing Kubernetes manifests.
3. **Spark**: You should have Spark installed locally.
4. **Argo Workflows**: Ensure Argo Workflows is installed in the cluster.

## Steps

### 1. Create a Spark Docker Image

1. Package your Spark application into a JAR file.
2. Create a Docker image with Spark and your application. Here’s an example Dockerfile:

    ```dockerfile
    FROM apache/spark:latest
    COPY your-spark-application.jar /opt/spark-apps/
    ```

3. Build and push the image to a container registry:

    ```bash
    docker build -t <your-registry>/<your-image-name>:<tag> .
    docker push <your-registry>/<your-image-name>:<tag>
    ```

### 2. Install Argo Workflows

If Argo Workflows is not installed, you can install it using Helm:

```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm install argo argo/argo-workflows
```

### 3. Create the Argo Workflow Manifest

1. Create an Argo Workflow YAML file (spark-job-workflow.yaml) that defines your Spark job. For example:

    ```yaml
    apiVersion: argoproj.io/v1alpha1
    kind: Workflow
    metadata:
      generateName: spark-job-
    spec:
      entrypoint: spark-job
      templates:
      - name: spark-job
        container:
          image: <your-registry>/<your-image-name>:<tag>
          command: ["/opt/spark/bin/spark-submit"]
          args: [
            "--master", "k8s://https://kubernetes.default.svc",
            "--deploy-mode", "cluster",
            "--class", "org.example.YourMainClass",
            "local:///opt/spark-apps/your-spark-application.jar"
            ]
    ```

  ### 4. Submit the Workflow

Submit the workflow to Argo:

```bash
kubectl create -f spark-job-workflow.yaml -n <namespace>
```

Check the status of your workflow:

```bash
kubectl get po -n <namespace>
```

To view logs of a specific job:

```bash
kubectl logs <pod_name> -n <namespace>
```

   ### 5. Verify Job Completion
   
   You can monitor the status of your Spark job and check its logs via Argo's UI or command line:

## Troubleshooting
  • Ensure that the Docker image is accessible to the Kubernetes cluster.
  
  • Check Spark and Argo logs for any specific errors related to configurations.
