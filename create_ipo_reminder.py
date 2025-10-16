from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime
import pytz

# Path to your existing service account key
SERVICE_ACCOUNT_FILE = r'.json'  # <-- Replace with your file name
SCOPES = ['https://www.googleapis.com/auth/calendar']
CALENDAR_ID = 'primary'  # Or use your Gmail if needed

# Authenticate
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('calendar', 'v3', credentials=credentials)

# India timezone
tz = pytz.timezone('Asia/Kolkata')

# Allotment Reminder Event
event = {
    'summary': '📢 Anthem IPO Allotment – Check Status',
    'description': 'Check Groww, Chittorgarh, or Link Intime for allotment status.',
    'start': {
        'dateTime': tz.localize(datetime(2025, 7, 17, 14, 0)).isoformat(),
        'timeZone': 'Asia/Kolkata',
    },
    'end': {
        'dateTime': tz.localize(datetime(2025, 7, 17, 14, 30)).isoformat(),
        'timeZone': 'Asia/Kolkata',
    },
    'reminders': {
        'useDefault': False,
        'overrides': [
            {'method': 'popup', 'minutes': 30},
            {'method': 'email', 'minutes': 60}
        ],
    },
}

# Insert into Calendar
created_event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
print("✅ Reminder added:", created_event.get('htmlLink'))
