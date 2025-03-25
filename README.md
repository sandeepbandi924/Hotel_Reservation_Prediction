# HOTEL RESRVATION PREDICTIONS




---------------------------- Setup jenkins COntainer--------------------------------------------------


(venv) S:\MLOPS_GCP_CICD\MLOPS_PROJECT_1\custom_jenkins>docker run -d --name jenkins-dind ^
More? --privileged ^
More? -p 8080:8080 -p 50000:50000 ^
More? -v //var/run/docker.sock:/var/run/docker.sock ^
More? -v jenkins_home:/var/jenkins_home ^
More? jenkins-dind