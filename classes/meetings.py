import requests
import json
from datetime import datetime, timezone, timedelta
import pytz
import pycountry

COUNTRY_NAME = "Egypt"
COUNTRY_CODE = "EG"

def get_country_code(country_name = COUNTRY_NAME):
    try:
        country = pycountry.countries.get(name=country_name)
        if country:
            return country.alpha_2
        else:
            return None  # Country not found in the database
    except Exception as e:
        return None


def get_timezone_offset(countryCode = COUNTRY_CODE):
    try:
        timezone = pytz.country_timezones.get(countryCode.upper())
        if timezone:
            tz = pytz.timezone(timezone[0])
            current_time = datetime.now(tz)
            utc_offset = current_time.utcoffset()
            offset_hours = utc_offset.total_seconds() / 3600
            return offset_hours
        else:
            return None  # Country not found in the database
        
    except Exception as e:
        return None


def generate_iso_format(year, month, day, hour, minute, second = 1, millisecond = 1, country = COUNTRY_NAME):
    country_code = get_country_code(country)
    timezone_offset = get_timezone_offset(country_code)
    user_datetime = datetime(year, month, day, hour, minute, second, 1000 * millisecond)
    offset = timedelta(hours=timezone_offset)
    user_datetime_with_offset = user_datetime - offset
    iso_format = user_datetime_with_offset.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + f"{offset.total_seconds() / 3600:+03.0f}:00"
    return iso_format

iso_format = generate_iso_format(2022, 3 , 25, 12, 30)
print(iso_format)

def create_teams_meeting(self, token, user_id, startYear, endYear, startMonth, endMonth, startDay, endDay, startHour, endHour, startMinute, endMinute, country = "Egypt" , subject = "User Meeting"):
    # Replace user_id with the user id from portal.azure.com
    url = f"https://graph.microsoft.com/v1.0/users/{user_id}/onlineMeetings"

    headers = {
        # replace token with the access token from portal.azure.com
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    countryOffset = get_timezone_offset(country)
    payload = json.dumps({
        "startDateTime": generate_iso_format(startYear, startMonth, startDay, startHour, startMinute, 1, 1, country),
        "endDateTime": generate_iso_format(endYear, endMonth, endDay, endHour, endMinute, 1, 1, country),
        "subject": subject
    })

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 201:
        meeting_url = response.json()['joinWebUrl']
        return meeting_url
    else:
        return None
