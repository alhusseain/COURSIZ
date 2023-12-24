import submissions
import courses
import datetime
import professors
import supervisors
class uploads:
    def uploadAssignment(self, uploadLink):
        uploadID = random.randint(1 , 10000)
        c.execute('''insert into Uploads(Upload_ID, Course_code, Date_of_Upload, Upload_header, Upload_type, Upload_description, Document_link, professorID, SupervisorID)
                    values (?, ?, ?)''', (uploadID , input("Enter the link of the assignment: ") , 1))
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
    