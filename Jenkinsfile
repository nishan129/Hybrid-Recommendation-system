pipeline{
    agent any

    stages{
        stage("Cloning from Github...."){
            step{
                script{
                    echo 'Cloning from Github'          
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/nishan129/Hybrid-Recommendation-system.git']])
                }
            }
        }
    }
}