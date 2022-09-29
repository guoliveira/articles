from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

credentialFileOfServiceAccount = 'credentials.json' # Please set the file path of the creadential file of service account
flow = InstalledAppFlow.from_client_secrets_file(
            credentialFileOfServiceAccount, ['https://www.googleapis.com/auth/drive.metadata.readonly'])
creds = flow.run_local_server(port=0)

service = build('drive', 'v3', credentials=creds)

results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
items = results.get('files', [])

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print(u'{0} ({1})'.format(item['name'], item['id']))