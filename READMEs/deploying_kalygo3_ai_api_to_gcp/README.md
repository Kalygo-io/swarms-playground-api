# TLDR

Documenting process of deploying Kalygo 3.0 A.I. API to GCP

## ToC

1. Artifact Registry
2. Cloud Build
3. Cloud Run
4. CICD with Github Actions

## 1. Artifact Registry

- TODO: setup gcloud inside of Devcontainer
- `gcloud artifacts repositories create kalygo3-fastapi --repository-format docker --project kalygo-v3 --location us-central1`
- CONFIRM REPOSITORY WAS CREATED: `https://console.cloud.google.com/artifacts?hl=en&project=kalygo-v3`
## 2. Cloud Build

- `gcloud builds submit --region=us-central1 --config cloudbuild.yaml`