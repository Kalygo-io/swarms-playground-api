# TLDR

Info regarding how the FastAPI was integrated with GCS (Google Cloud Storage)

## log

- Go to IAM & Admin section of the GCP console
- Created a Google S.A. with the `Storage Object User` role
- Create JSON key for using the S.A.
- Created a bucket called: `swarms`
- Add more permissions to the GCS S.A. account
  - gcloud projects add-iam-policy-binding 137963986378 \
    --member="serviceAccount:kalygo3-gcs-sa@kalygo-v3.iam.gserviceaccount.com" \
    --role="roles/storage.admin"

## Permissions to CRUD to GCS

- NOTE: a different technique for importing the S.A. creds is needed in local (dev machine) vs production (Cloud Run)


## Needed to give SA in GitHub action an additional permission for giving a non-default S.A. when deploying Cloud Run services

- gcloud iam service-accounts add-iam-policy-binding kalygo3-gcs-sa@kalygo-v3.iam.gserviceaccount.com \
  --member="serviceAccount:kalygo3-sa@kalygo-v3.iam.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser"

- gcloud projects add-iam-policy-binding 137963986378 \
  --member="serviceAccount:kalygo3-gcs-sa@kalygo-v3.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"

## WTF

--service-account kalygo3-gcs-sa@kalygo-v3.iam.gserviceaccount.com