import os
import boto3

def send_email_ses(account_id: int, reset_token: str):
  try:
    client = boto3.client(
      'ses',
      region_name=os.getenv("AWS_REGION"),
      aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
      aws_secret_access_key=os.getenv("AWS_SECRET_KEY")
    )

    print('API_HOSTNAME')
    print(os.getenv('API_HOSTNAME'))
    print()

    response = client.send_email(
      Source='noreply@kalygo.io',
      Destination={
        'ToAddresses': ['tad@cmdlabs.io']
      },
      Message={
        'Subject': {
          'Data': 'Password Reset Request'
        },
        'Body': {
          'Html': {
            'Data': f"<p>Reset Token: {reset_token}</p><a href='{os.getenv('API_HOSTNAME')}/reset-password?account-id={account_id}'>Reset Password</a>"
          }
        }
      }
    )
    print(response)
  except Exception as e:
    print(e)

