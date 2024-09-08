import google.auth
import os
import json
from google.oauth2 import service_account

def get_principal():
    if (os.getenv("ENVIRONMENT") == "production"):
        GCS_SA = json.loads(os.getenv('GCS_SA'))

        credentials, project = google.auth.load_credentials_from_dict(GCS_SA)
      
        print()
        print('credentials', credentials)
        print('project', project)
        print(f"Principal (service account): {credentials.service_account_email}")
        print()

    else:
        GCS_SA_PATH = os.getenv("GCS_SA_PATH")
        credentials = service_account.Credentials.from_service_account_file(
            GCS_SA_PATH
        ) 
        print(f"Principal (service account): {credentials.service_account_email}")