from icalendar import Calendar
from google.oauth2 import service_account
from googleapiclient.discovery import build
import pytz

# Path to your service account key
SERVICE_ACCOUNT_FILE = r'.json' # <-- Replace with your file name
SCOPES = ['https://www.googleapis.com/auth/calendar']
CALENDAR_ID = 'primary'  # or your Gmail if you use a shared calendar

# Authenticate
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('calendar', 'v3', credentials=credentials)

# Read the .ics file
with open('invite.ics', 'rb') as f:
    cal = Calendar.from_ical(f.read())

# Parse events and insert
for component in cal.walk():
    if component.name == "VEVENT":
        summary = str(component.get('summary'))
        description = str(component.get('description'))
        start = component.get('dtstart').dt
        end = component.get('dtend').dt

        # Convert to timezone-aware datetime if needed
        if not hasattr(start, 'tzinfo') or start.tzinfo is None:
            start = pytz.timezone('Asia/Kolkata').localize(start)
        if not hasattr(end, 'tzinfo') or end.tzinfo is None:
            end = pytz.timezone('Asia/Kolkata').localize(end)

        event = {
            'summary': summary,
            'description': description,
            'start': {'dateTime': start.isoformat(), 'timeZone': 'Asia/Kolkata'},
            'end': {'dateTime': end.isoformat(), 'timeZone': 'Asia/Kolkata'},
        }

        # Insert event
        created_event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        print("✅ Event created:", created_event.get('htmlLink'))

