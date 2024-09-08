from google.cloud import storage
from google.oauth2 import service_account
import google.auth
import os

STORAGE_SERVICE_ACCOUNT_KEY = os.getenv("STORAGE_SERVICE_ACCOUNT_KEY")

class GCSClient:
  @staticmethod
  def get_storage_client():

    if (os.getenv("ENVIRONMENT") == "production"):
        credentials, project = google.auth.default()
    else:
        """Return a Google Cloud Storage client using a specific service account."""
        credentials = service_account.Credentials.from_service_account_file(
        STORAGE_SERVICE_ACCOUNT_KEY
        )
        project = "kalygo-v3"

    return storage.Client(credentials=credentials)
  