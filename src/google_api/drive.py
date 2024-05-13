from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import os
from dotenv import load_dotenv


CLIENT_SECRETS = os.getenv('CLIENT_SECRETS')

print(CLIENT_SECRETS)

client_secrets = CLIENT_SECRETS


SCOPES = ['https://www.googleapis.com/auth/drive']


flow = InstalledAppFlow.from_client_secrets_file(client_secrets, SCOPES)


credentials = flow.run_local_server(port=8080)


service = build('drive', 'v3', credentials=credentials)

print('Authentication is successful.')
