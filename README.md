# Spark • PySpark • YARN • Kubernetes – Distributed Computing Project

This project demonstrates distributed data processing using Apache Spark, PySpark, Hadoop YARN (via Docker), and Kubernetes (Minikube).  
It includes:  
- Basic PySpark RDD transformations  
- Spark job execution via `spark-submit`  
- Persistence-level comparison (MEMORY_ONLY vs DISK_ONLY)  
- Running Spark on a YARN cluster  
- Dynamic node management in Kubernetes (add/remove/cordon/uncordon)

---

# Install required tools (macOS)
brew install openjdk

brew install scala

brew install apache-spark

brew install python

# Verify installation
spark-shell --version

pyspark --version

python3 --version

# Run PySpark
pyspark

# Submit Spark script (standalone)
spark-submit --master 'local[*]' scripts/top10_words.py data/file1 MEMORY_ONLY

spark-submit --master 'local[*]' scripts/top10_words.py data/file1 DISK_ONLY

# Run Docker-based Hadoop + YARN cluster
docker compose up -d

docker ps

# Enter Spark client container
docker exec -it spark-client bash

# Submit Spark script on YARN
spark-submit --master yarn --deploy-mode client /scripts/top10_words.py /data/file1 MEMORY_ONLY

spark-submit --master yarn --deploy-mode client /scripts/top10_words.py /data/file1 DISK_ONLY

# Exit container
exit

# Stop Docker cluster
docker compose down

# Start Minikube Kubernetes cluster (2 nodes)
minikube start -p spark-k8s --driver=docker --cpus=4 --memory=6000 --nodes=2

kubectl get nodes

# Add and delete nodes
minikube -p spark-k8s node add

minikube -p spark-k8s node delete <node-name>

# Cordon / Uncordon nodes (scheduler control)
kubectl cordon <node-name>

kubectl uncordon <node-name>

# Kubernetes cleanup
minikube stop -p spark-k8s

minikube delete -p spark-k8s
