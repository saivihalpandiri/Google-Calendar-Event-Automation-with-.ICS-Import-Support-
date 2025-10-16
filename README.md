# Google Calendar IPO Reminder System

Python automation scripts for creating IPO-related calendar events using Google Calendar API with service account authentication.

## Overview

These scripts help automate the creation of IPO tracking events in Google Calendar. Instead of manually adding reminders for IPO deadlines and allotment dates, you can run these scripts to create events automatically.

## Prerequisites

- Python 3.7+
- Google Cloud Project
- Calendar API enabled
- Service account with JSON key file

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Setup

### Google Cloud Configuration

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create or select a project
3. Enable Google Calendar API
4. Create a Service Account
5. Download the JSON key file

### Calendar Access

Share your Google Calendar with the service account email found in your JSON key file. The email looks like `something@project-id.iam.gserviceaccount.com`. Give it "Make changes to events" permission.

### Update Scripts

Replace the service account file path in each script:

```python
SERVICE_ACCOUNT_FILE = r'path/to/your/credentials.json'
```

## Scripts

### create_event.py
Basic event creation without custom reminders.

### create_event_with_reminders.py
Creates events with custom popup and email reminders. Useful when you need notifications at specific times.

### create_ipo_reminder.py
Specialized for IPO allotment reminders with proper timezone handling using pytz.

### import_ics_events.py
Import multiple events from .ics calendar files. Useful for bulk imports.

## Usage

Run any script directly:

```bash
python create_event.py
```

Modify the event details in the script before running:

```python
event = {
    'summary': 'Your Event Title',
    'description': 'Event description',
    'start': {
        'dateTime': '2025-07-17T12:00:00+05:30',
        'timeZone': 'Asia/Kolkata',
    },
    'end': {
        'dateTime': '2025-07-17T12:30:00+05:30',
        'timeZone': 'Asia/Kolkata',
    },
}
```

### Adding Reminders

For scripts with reminder support:

```python
'reminders': {
    'useDefault': False,
    'overrides': [
        {'method': 'popup', 'minutes': 60},
        {'method': 'email', 'minutes': 1440},
    ],
}
```

Available methods: `popup`, `email`, `sms`

### Importing from .ics Files

Place your .ics file in the same directory and update the filename:

```python
with open('your-file.ics', 'rb') as f:
    cal = Calendar.from_ical(f.read())
```

## Troubleshooting

**Calendar API not enabled**
Enable it in Google Cloud Console under APIs & Services.

**Insufficient permissions**
Make sure you shared your calendar with the service account email.

**Invalid credentials**
Check if the JSON file path is correct and the file hasn't been revoked.

**Events not appearing**
Verify the calendar ID is correct. Try using `'primary'` instead of an email address.

**Timezone issues**
Use `pytz.timezone('Asia/Kolkata').localize()` for datetime objects to ensure proper timezone handling.

## Notes

- Keep your service account JSON file secure
- Never commit credentials to public repositories
- The service account email is different from your personal email
- Use raw strings `r''` for Windows file paths

## Resources

- [Google Calendar API Documentation](https://developers.google.com/calendar/api/v3/reference)
- [Service Account Guide](https://cloud.google.com/iam/docs/service-accounts)
- [pytz Timezone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
