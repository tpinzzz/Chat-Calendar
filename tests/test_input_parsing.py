import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from input_parser import parse_event_input

def test_parse_event_input():
    test_cases = [
        {
            "input": "Create an event titled 'Lunch with Alex' tomorrow at 1 PM for 2 hours.",
            "expected": {
                "title": "Lunch with Alex",
                "date": "2025-01-25",  # Assuming today's date is Jan 24
                "start_time": "13:00",
                "end_time": "15:00",
                "description": None
            }
        },
        {
            "input": "Schedule 'Doctor's Appointment' for January 27 at 10 AM. Description: Bring medical reports.",
            "expected": {
                "title": "Doctor's Appointment",
                "date": "2025-01-27",
                "start_time": "10:00",
                "end_time": "11:00",
                "description": "Bring medical reports"
            }
        },
        {
            "input": "Plan lunch with Sarah next Wednesday at 1 PM.",
            "expected": {
                "title": "Lunch with Sarah",
                "date": "2025-01-29",  # Next Wednesday
                "start_time": "13:00",
                "end_time": "14:00",
                "description": None
            }
        }
    ]

    for i, case in enumerate(test_cases):
        print(f"Running Test Case {i + 1}: {case['input']}")
        parsed_event = parse_event_input(case["input"])
        assert parsed_event == case["expected"], f"Test Case {i + 1} Failed! Expected {case['expected']}, got {parsed_event}"
        print("Test Passed!")

if __name__ == "__main__":
    test_parse_event_input()