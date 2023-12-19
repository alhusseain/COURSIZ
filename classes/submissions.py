from students import students
from databaseConnection import *
import random
import time

c = connection.cursor()
class submissions(students, ):
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
            
    # def submitQuiz(self, durationInMinutes, is_started, student):
    #     if isStarted:
    #         print("Quiz has started")
    #         time.sleep(durationInMinutes * 60)
    #     if isFinished:
    #         c.execute('''insert into Enroll_in(Student_ID, Course_Code, grade)
    #         values (?, ?, ?, ?)''', (random.randint(1,10000), EnrollIn.courseID,))
    #     conn.commit()
    #     conn.close()
    #     print("Quiz submitted successfully")