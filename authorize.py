import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar():
    creds = None
    token_path = 'config/token.pickle'
    credentials_path = 'config/credentials.json'

    # Check if token.pickle exists
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    # If there are no valid credentials, prompt the user to log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0, authorization_prompt_message='Please log in with your business email.')

        # Save the credentials for future use
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return creds

def test_token(creds):
    from googleapiclient.discovery import build
    try:
        service = build('calendar', 'v3', credentials=creds)
        # Make a simple API call to check validity
        calendars = service.calendarList().list().execute()
        print("Authorization successful! Calendars retrieved:")
        for calendar in calendars['items']:
            print(f"Calendar: {calendar['summary']}")
    except Exception as e:
        print(f"Error validating credentials: {e}")

if __name__ == '__main__':
    creds = authenticate_google_calendar()
    test_token(creds)
