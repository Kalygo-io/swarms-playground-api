import google.auth

def get_principal():
    # Get the credentials and project ID from the environment
    credentials, project_id = google.auth.default()

    # Print the service account email (principal)
    print(f"Principal (service account): {credentials.service_account_email}")