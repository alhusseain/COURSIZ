from users import *
import requests
import json

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

    def create_teams_meeting(self, token, user_id):
        url = f"https://graph.microsoft.com/v1.0/users/{user_id}/onlineMeetings"

        headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }

        payload = json.dumps({
            "startDateTime":"2022-07-12T14:30:34.2444915-07:00",
            "endDateTime":"2022-07-12T15:00:34.2464912-07:00",
            "subject":"User Meeting"
        })

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 201:
            meeting_url = response.json()['joinWebUrl']
            print(f'Meeting created: {meeting_url}')
            return meeting_url
        else:
            print(f'Could not create meeting, status code: {response.status_code}')
            return None