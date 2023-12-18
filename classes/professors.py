from users import *
import requests
import json
from datetime import datetime, timezone, timedelta
import pytz

def get_timezone_offset(country = "Egypt"):
    try:
        timezone = pytz.country_timezones.get(country.upper())
        if timezone:
            tz = pytz.timezone(timezone[0])
            utc_offset = tz.utcoffset(datetime.now())
            offset_hours = utc_offset.total_seconds() / 3600
            return offset_hours
        else:
            return None  # Country not found in the database
        
    except Exception as e:
        return None

def generate_iso_format(year, month, day, hour, minute, second = 1, millisecond = 1, get_timezone_offset(country) = 2):
    user_datetime = datetime(year, month, day, hour, minute, second, 1000 * millisecond)
    offset = timedelta(hours=timezone_offset)
    user_datetime_with_offset = user_datetime - offset
    iso_format = user_datetime_with_offset.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + f"{offset.total_seconds() / 3600:+03.0f}:00"
    return iso_format

class professors(users):
    def sign_in(self, username, password):
        if username == "1" and password == "1":
            return true
        else:
            return false

    def sign_up(self, username, email, password):
        return username, email, password
    
    def studentsEntry(self, choice):
        if choice == "Sign in":
            self.sign_in(username, password)
        elif choice == "Sign up":
            self.sign_up(username, email, password)

    
    def create_teams_meeting(self, token, user_id, startYear, endYear, startMonth, endMonth, startDay, endDay, startHour, endHour, startMinute, endMinute, country = "Egypt" , subject = "User Meeting"):
        # Replace user_id with the user id from portal.azure.com
        url = f"https://graph.microsoft.com/v1.0/users/{user_id}/onlineMeetings"

        headers = {
            # replace token with the access token from portal.azure.com
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }

        payload = json.dumps({
            "startDateTime": generate_iso_format(startYear, startMonth, startDay, startHour, startMinute, second = 1, millisecond = 1, get_timezone_offset(country) = 2),
            "endDateTime": generate_iso_format(endYear, endMonth, endDay, endHour, endMinute, second = 1, millisecond = 1, get_timezone_offset(country) = 2),
            "subject": subject
        })

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 201:
            meeting_url = response.json()['joinWebUrl']
            return meeting_url
        else:
            return None
