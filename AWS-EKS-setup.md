# AWS Elastic Kubernetes Service 
EKS CLUSTER

GOT TO YOUR CONSOLE AND CREATE AN INSTANCE ( JUST TO SET UP THE  CLUSTER )
Launch an Instance:
UBUNTU 18.04
T3.Large
KEYPAIR
SG- ANYWHERE
IAM ROLE- EC2FULL ACCESS AND AdministratorAccess
LAUNCH
SSH
Go TO YOUR BROWSER AND INSTALL AWS CLI INSTALLATION USING BELOW LINK:
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

Run this command on your CLI
sudo apt install unzip -y

## install aws cli package by running these 3 command together:
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
## create .aws folder (do ls -al to confirm it's not there) and provide your credentials.
mkdir .aws
touch ~/.aws/credentials
vi ~/.aws/credentials
Go to insert mood  and replace the credentials
[User_Profile]
aws_access_key_id=.....
aws_secret_access_key=.....
region=us-east-1
output=json
## create eksctl package
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version
sudo apt update
sudo apt-get install -y apt-transport-https
### setting up the repo
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
### managing the package manager
sudo touch /etc/apt/sources.list.d/kubernetes.list
### we'er writting the http echo inside the k8s list
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
### update server now
sudo apt-get update
### installation of kubectl utility
sudo apt-get install -y kubectl
### checking the version of kubectl. // client version is the actual version and the Kustomize is an accomplise version
kubectl version --short --client

### create a workspace folder where you store all your files:
mkdir workspace
cd workspace/  --> nano eks-Cluster-Setup.yaml
### Inside your file,copy and paste what you created in your eks-Cluster-Setup.yaml file

YAML file is provided. copy, paste and save: CTRL + X --> Y--> Enter

### orchestrate the cluster and update the cluster name
eksctl create cluster -f eks-cluster-setup.yaml





kubectl api-resources
kubectl -n kube-system get cm
kubectl -n kube-system get configmap aws-auth -o json
kubectl -n kube-system get configmap aws-auth -o yaml
kubectl -n kube-system get configmap aws-auth
