from scripts.authorize import authenticate_google_calendar
from scripts.calendar_operations import get_upcoming_events, create_event
from googleapiclient.discovery import build

if __name__ == '__main__':
    creds = authenticate_google_calendar()
    service = build('calendar', 'v3', credentials=creds)

    # Example: Fetch events
    print("Fetching upcoming events...")
    get_upcoming_events(service)

    # Example: Create a test event
    print("Creating a new event...")
    create_event(
        service,
        summary="Test Event",
        start_time="2025-01-25T10:00:00Z",
        end_time="2025-01-25T11:00:00Z",
        description="This is a test event."
    )
