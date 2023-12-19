from students import students
from databaseConnection import *
import random
import time

c = connection.cursor()
class submissions():
    def submitWork(self, workLink, student):
        submissionID = random.randint(1 , 10000)
        if workLink.startswith("https://docs.google.com/") or workLink.startswith("https://drive.google.com/") and workLink.endswith("sharing"):
            try:
                # student id and upload id are hardcoded until edible population for the database
                c.execute('''insert into Submissions(Submission_ID, Document_link, Student_ID, Upload_ID) 
                            values (?, ?, ?, ?)''', (submissionID , workLink , 1, 1))
                c.commit()
                c.close()
                print("Work submitted successfully")
            except pyodbc.IntegrityError:
                self.submitWork(workLink, student)
        else:
            print("Invalid link")
            self.submitWork(input("Enter a valid link: "), student)
    
    # when the student enter the link of the quiz, the setTimeForQuiz function will be called using get method linked by clicking on the link
    def setTimeForQuiz(self, durationInMinutes):
        # setting timer on
        isStarted = True
        isFinished = False
        isEnded = False
        # using google sheets api, when the student submit the quiz, the isFinished will be set to True
        isFinished = True
        if isFinished:
            isStarted = False
            print("Quiz has ended")
        # when the durationInMinutes is over, the isEnded will be set to True
        isEnded = True
        if not isFinished and isEnded:
            # close the forms using google forms API
            print("Quiz has ended")
        # add the grade to the database from the google sheets using google sheets API
        c.execute('''insert into Enroll_in(Student_ID, Course_Code, grade)
            values (?, ?, ?, ?)''', (random.randint(1,10000), EnrollIn.courseID,))
        c.commit()
        c.close()