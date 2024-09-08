from src.clients.gcs_client import GCSClient

def upload_csv_to_gcs(csv_data, bucket_name, file_name):
        # Use the storage service account to upload the file
        storage_client = GCSClient.get_storage_client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(file_name)
        blob.upload_from_string(csv_data, content_type='text/csv')