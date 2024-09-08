from google.cloud import storage
import google.auth
from google.oauth2 import service_account
from datetime import datetime, timedelta
import os
from src.clients.gcs_client import GCSClient

STORAGE_SERVICE_ACCOUNT_KEY = os.getenv("STORAGE_SERVICE_ACCOUNT_KEY")

def generate_signed_url(bucket_name, file_name, expiration=3600):
    storage_client = GCSClient.get_storage_client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    expiration_time = datetime.now() + timedelta(seconds=expiration)
    url = blob.generate_signed_url(expiration=expiration_time)
    return url