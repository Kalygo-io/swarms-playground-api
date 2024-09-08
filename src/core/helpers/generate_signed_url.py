from google.cloud import storage
import google.auth
from google.oauth2 import service_account
from datetime import datetime, timedelta
import os

STORAGE_SERVICE_ACCOUNT_KEY = os.getenv("STORAGE_SERVICE_ACCOUNT_KEY")


def generate_signed_url(bucket_name, file_name, expiration=3600):
    # credentials, project = google.auth.default()
    """Return a Google Cloud Storage client using a specific service account."""
    credentials = service_account.Credentials.from_service_account_file(
      STORAGE_SERVICE_ACCOUNT_KEY
    )
    project = "kalygo-v3"

    storage_client = storage.Client(credentials=credentials, project=project)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    expiration_time = datetime.now() + timedelta(seconds=expiration)
    url = blob.generate_signed_url(expiration=expiration_time)
    return url