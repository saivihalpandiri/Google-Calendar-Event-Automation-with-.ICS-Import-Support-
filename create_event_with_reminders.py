from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import pytz

# Path to your service account key
SERVICE_ACCOUNT_FILE = r'.json' # <-- Replace with your file name

# Your calendar ID (can be your email or primary)
CALENDAR_ID = 'saivihal042@gmail.com'  # or use 'primary'

# Define the scope
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Authenticate
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the calendar service
service = build('calendar', 'v3', credentials=credentials)

# Set your timezone
timezone = 'Asia/Kolkata'

# Define event details
event = {
    'summary': 'Anthem Biosciences IPO Last Date',
    'description': 'Final day to apply for Anthem Biosciences IPO',
    'start': {
        'dateTime': datetime(2025, 7, 16, 10, 0).isoformat(),
        'timeZone': timezone,
    },
    'end': {
        'dateTime': datetime(2025, 7, 16, 11, 0).isoformat(),
        'timeZone': timezone,
    },
    'reminders': {
        'useDefault': False,
        'overrides': [
            {'method': 'popup', 'minutes': 60},
            {'method': 'email', 'minutes': 24 * 60},
        ],
    },
}

# Add event to calendar
event_result = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()

print(f"Event created: {event_result.get('htmlLink')}")
