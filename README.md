# Minikube-deployment and testing

#Prerequisites
-Minikube cluster
-Cypress installed
-frontend and backend services deployed

#setup
-start a local kubernetes cluster
-minikube start
-kubectl create ns test
-kubectl apply -f https://raw.githubusercontent.com/Vengatesh-m/qa-test/refs/heads/main/Deployment/backend-deployment.yaml -n test
-kubectl apply -f https://raw.githubusercontent.com/Vengatesh-m/qa-test/refs/heads/main/Deployment/frontend-deployment.yaml -n test
access URL
minikube service frontend-service

#run test
-npm install cypress
-npx cypress open
-select test script file and run in desired browser offered by cypress
