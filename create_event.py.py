from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = '.json'  # <-- Replace with your file name

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('calendar', 'v3', credentials=credentials)

event = {
    'summary': 'Anthem IPO – Allotment Status',
    'description': 'Check IPO allotment status on Groww/Chittorgarh.',
    'start': {
        'dateTime': '2025-07-17T12:00:00+05:30',
        'timeZone': 'Asia/Kolkata',
    },
    'end': {
        'dateTime': '2025-07-17T12:30:00+05:30',
        'timeZone': 'Asia/Kolkata',
    },
}

event_result = service.events().insert(calendarId='primary', body=event).execute()

print(f"✅ Event created: {event_result.get('htmlLink')}")
