pipeline{
    agent any

    environment{
        VENV_DIR = 'venv'
        GCP_PROJECT='mlops-new-454707'
        GCLOUD_PATH='/var/jenkins_home/google_cloud-sdk/bin'
    }

    stages{
        stage('Cloning github repo to jenkins'){
            steps{
                script{
                    echo 'Cloning github repo to jenkins..............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/sandeepbandi924/Hotel_Reservation_Prediction.git']])
                }
            }
        }
        stage('Setting up our Virutal Environment and Installing dependiencies'){
            steps{
                script{
                    echo 'Setting up our Virutal Environment and Installing dependiencies..............'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

        stage('Building and Pushing Docker Image to GCR'){
            steps{
                withCredentials([file(credentialsId:'gcp-key', variable:'GOOGLE_APPLICATION_CREDENTIALS')]){
                script{
                    echo 'Building and Pushing Docker Image to GCR........................'
                    sh '''
                    export PATH=$PATH:${GCLOUD_PATH}

                    gcloud auth activate-service account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                    gcloud config set project ${GCP_PROJECT}

                    gcloud auth configure-docker --quiet

                    docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                    docker push gcr.io/${GCP_PROJECT}/ml-project:latest 

                    '''
                }
            }
        }
    }
}
}
