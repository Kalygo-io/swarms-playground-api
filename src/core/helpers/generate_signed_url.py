from google.cloud import storage
import google.auth
from google.oauth2 import service_account
from datetime import datetime, timedelta
import os
from core.helpers.get_principal import get_principal
from src.clients.gcs_client import GCSClient

def generate_signed_url(bucket_name, file_name, expiration=3600):
    print()
    print("generate_signed_url")
    print()

    print("1")
    storage_client = GCSClient.get_storage_client()
    print("2")
    bucket = storage_client.get_bucket(bucket_name)
    print("3")
    blob = bucket.blob(file_name)
    print("4")
    expiration_time = datetime.now() + timedelta(seconds=expiration)
    print("5")

    print('get_principal()')
    print(get_principal())

    print('blob')
    print(blob)

    url = blob.generate_signed_url(expiration=expiration_time)
    print("6")
    return url