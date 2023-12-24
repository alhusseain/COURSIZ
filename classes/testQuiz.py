import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import random
from databaseConnection import *

c = connection.cursor()

class QuizHandler:
    def __init__(self):
        self.isStarted = False
        self.isFinished = False
        self.isEnded = False

        # Set up Google Sheets API
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        self.client = gspread.authorize(creds)

    def setTimeForQuiz(self, durationInMinutes):
        # Assume quiz started
        self.isStarted = True

        # Simulate quiz submission through Google Sheets API
        # isFinished will be set to True upon submission
        # Replace this with actual Google Sheets API logic
        # Assuming spreadsheet has columns: Student_ID, Course_Code, grade
        if self.isStarted:
            # Simulating quiz submission and data preparation
            data_to_submit = [random.randint(1, 10000), 'Your_Course_Code', 'A']  # Replace 'Your_Course_Code' with actual course code

            try:
                # Accessing the specific worksheet by title
                sheet = self.client.open_by_key('YOUR_SPREADSHEET_ID').worksheet('Sheet1')
                sheet.append_row(data_to_submit)

                self.isFinished = True  # Simulating quiz submission
                print("Quiz has ended")

            except Exception as e:
                print("Error submitting quiz:", e)

        # Simulate timer completion after durationInMinutes
        # Replace this with actual timer functionality
        self.isEnded = True

        if not self.isFinished and self.isEnded:
            # Simulate closing the quiz form using Google Forms API (HTTP request)
            # Replace this with actual form closing logic
            form_url = 'https://docs.google.com/forms/d/e/YOUR_FORM_ID/formResponse'
            data = {
                'entry.1234567890': 'Close'  # Replace with your form field IDs and appropriate data to close the form
            }

            response = requests.post(form_url, data=data)

            if response.status_code == 200:
                print("Quiz form closed.")
            else:
                print("Error closing the quiz form.")

            # Adding the grade to the database using SQLite
            try:
                # Establish a connection to the database


                # Assuming Enroll_in table structure: Student_ID, Course_Code, grade
                c.execute('''INSERT INTO Enroll_in(Student_ID, Course_Code, grade)
                                  VALUES (?, ?, ?)''', (random.randint(1, 10000), 'Your_Course_Code', 'A'))  # Replace 'Your_Course_Code' with actual course code and "A" with actual grade

                # Commit changes and close the connection
                connection.commit()
                connection.close()

            except pydbc.Error as error:
                print("Error while working with SQLite:", error)
