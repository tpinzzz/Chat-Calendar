from googleapiclient.discovery import build

def get_upcoming_events(service, calendar_id='primary', max_results=10):
    events_result = service.events().list(
        calendarId=calendar_id,
        maxResults=max_results,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    if not events:
        print("No upcoming events found.")
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
