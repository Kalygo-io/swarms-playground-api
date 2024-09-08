from google.cloud import storage
from google.oauth2 import service_account
import os

STORAGE_SERVICE_ACCOUNT_KEY = os.getenv("STORAGE_SERVICE_ACCOUNT_KEY")

class GCSClient:
  @staticmethod
  def get_storage_client():
    """Return a Google Cloud Storage client using a specific service account."""
    credentials = service_account.Credentials.from_service_account_file(
      STORAGE_SERVICE_ACCOUNT_KEY
    )
    return storage.Client(credentials=credentials)
  