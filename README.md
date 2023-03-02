### Create your AMAZON EKS cluster:
AWS-EKS-setup.md provide step-by-step process (files used to build docker images for shits and users containers are also attached)

### 1- Deploy your Metrics-server:
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

### 2- Deploy manifest files with deployments, service and Horizontal Pod autoscaler: (source: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)
- Auto scale define within HPA block targetCPUUtilizationPercentage set at 70%.


kubectl apply -f hpa-takehome-shift-deployment.yaml  

kubectl apply -f hpa-takehome-users-deployment.yaml    ( 2 separate deployments so they can scale independently)

### 3- Kubernetes can roll back to previous version by default.
### 4- Type of IAM controls:
We will use IAM Group, users and Policies, and we make use of RBAC at the level of Kubernetes.
## How to assign specific role to Dev Team:
create a rbac.yaml file where you define the ClusterRole and ClusterRoleBinding in ClusterRole block define resources that you want to give access. and the permissions.(rbac.yaml file is provided for this project) then create using: kubectl apply -f rbac.yaml (or the path where the file is located)
To map AWS user to RBAC
Create policy in AWS that grant eks read write permissions and assign it to Group dev-users
create a user called flavio, attach to group and save secret key and access key.
To map the user in configmap, from your terminal run:  kubectl edit -n kube-system configmap/aws-auth
Under data: add "mapUsers" and under it add:
 - userarn: (user ARN)
   username: flavio
   groups:
   - dev-users
and save it.
now we can access verify by accessing EKS as flavio: aws eks --region us-east-1 update-kubeconfig --name take-home-test-cluster --profile flavio (make sure aws configure was already performed to save access key and secret key to the environment)

Then run: kubectl config view --minify   to view profile
and "kubectl auth can-i ..." commands (kubectl auth can-i get pods   for example)

### Bonus:
- We can apply the configs to multiple environments by enabling setting up assume role policy that will grant to a user (a manager for example) access across mutiple accounts.
- Network latency is a metric type that can be define at the level of the HPA bolck (see comments under HPA block).


