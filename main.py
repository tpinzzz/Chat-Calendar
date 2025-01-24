from scripts.authorize import authenticate_google_calendar
from scripts.calendar_operations import get_upcoming_events, create_event
from googleapiclient.discovery import build
from datetime import datetime, timedelta

if __name__ == '__main__':
    creds = authenticate_google_calendar()
    service = build('calendar', 'v3', credentials=creds)

    # Example: Fetch events
    print("Fetching events for tomorrow...")
    tomorrow = (datetime.utcnow() + timedelta(days=1)).isoformat() + 'Z'
    day_after_tomorrow = (datetime.utcnow() + timedelta(days=2)).isoformat() + 'Z'
    get_upcoming_events(service, start_date=tomorrow, end_date=day_after_tomorrow)

    print("Fetching events for next week...")
    next_week_start = (datetime.utcnow() + timedelta(days=7)).isoformat() + 'Z'
    next_week_end = (datetime.utcnow() + timedelta(days=14)).isoformat() + 'Z'
    get_upcoming_events(service, start_date=next_week_start, end_date=next_week_end)

    # Example: Create a test event using the timeZone field
    print("Creating a new event...")

    create_event(
        service,
        summary="Test Event",
        start_time="2025-01-24T12:30:00",
        end_time="2025-01-24T13:00:00",
        description="This is when I plan to get my hair fixed.",
        timeZone="America/New_York"  # Specify the time zone directly
    )