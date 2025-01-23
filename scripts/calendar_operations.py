from googleapiclient.discovery import build
from datetime import datetime, timedelta


def get_upcoming_events(service, start_date=None, end_date=None):
    now = datetime.utcnow().isoformat() + 'Z'  # Current time in UTC
    time_min = start_date or now
    time_max = end_date or (datetime.utcnow() + timedelta(days=7)).isoformat() + 'Z'

    events_result = service.events().list(
        calendarId='primary',
        timeMin=time_min,
        timeMax=time_max,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    if not events:
        print("No events found in the specified range.")
        return []

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f"{start}: {event.get('summary', 'No Title')}")
    return events

def create_event(service, calendar_id='primary', summary=None, start_time=None, end_time=None, description=None):
    event = {
        'summary': summary,
        'start': {'dateTime': start_time, 'timeZone': 'UTC'},
        'end': {'dateTime': end_time, 'timeZone': 'UTC'},
        'description': description,
    }
    event_result = service.events().insert(calendarId=calendar_id, body=event).execute()
    print(f"Event created: {event_result.get('htmlLink')}")
    return event_result
