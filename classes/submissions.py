from databaseConnection import db
db=db()
# Submission_ID, Submission_type, studentID, Document_link


class submissions:
    def createSubmission(self,upload_id,course_code,out_of,Deadline):
        query = db.cursor
        query.execute("insert into Sumbissions(Submission_ID,Deadline_Date) values(?,?)",(upload_id,Deadline))
        db.connection.commit()
        query.execute("select distinct Student_ID from Enroll_in where Course_Code=?",(course_code))
        student_ids = query.fetchall()
        for student_id in student_ids:
            query.execute("insert into Submits(SubID,student_id,out_of) values(?,?,?)",(upload_id,student_id[0],out_of))
        db.connection.commit()

    # def createSubmission(self, Document_link, Submission_type, course):
    #     query = db.cursor()
    #     if self.Document_link is None:
    #         return False
    #     elif self.Document_link.startswith("https://docs.google.com/") and document_link.endswith("/sharing"):
    #         query.execute("SELECT COUNT(*) FROM Submissions")
    #         number_of_rows = query.fetchone()[0]
    #         Submission_ID = number_of_rows + 1
    #         Submission_type = "Document"
    #         query.execute("INSERT INTO Submissions(Submission_ID, Submission_type, studentID, Document_link, Course_Code) VALUES(?, ?, ?, ?, ?)", (Submission_ID, Submission_type, studentID, Document_link, courseCode))
    #         db.connection.commit()
    #         return True
    #     elif self.Document_link.startswith("https://github.com/"):
    #         query.execute("SELECT COUNT(*) FROM Submissions")
    #         number_of_rows = query.fetchone()[0]
    #         Submission_ID = number_of_rows + 1
    #         Submission_type = "Project"
    #         query.execute("INSERT INTO Submissions(Submission_ID, Submission_type, studentID, Document_link, Course_Code) VALUES(?, ?, ?, ?, ?)", (Submission_ID, Submission_type, studentID, Document_link, courseCode))
    #         databaseConnection.connection.commit()
    #         return True
    #     else:
    #         query.execute("SELECT COUNT(*) FROM Submissions")
    #         number_of_rows = query.fetchone()[0]
    #         Submission_ID = number_of_rows + 1
    #         query.execute("INSERT INTO Submissions(Submission_ID, Submission_type, studentID, Document_link, Course_Code) VALUES(?, ?, ?, ?, ?)", (Submission_ID, Submission_type, studentID, Document_link, courseCode))
    #         databaseConnection.connection.commit()
    #         return True
        
    # def deleteSubmission(self, Submission_ID):
    #     query = databaseConnection.connection.cursor()
    #     query.execute("DELETE FROM Submissions WHERE Submission_ID = ?", (Submission_ID))
    #     databaseConnection.connection.commit()
    #     return True
    
    # def updateSubmission(self, Submission_ID, Submission_type, Document_link):
    #     query = databaseConnection.connection.cursor()
    #     query.execute("UPDATE Submissions SET Submission_type = ?, Document_link = ? WHERE Submission_ID = ?", (Submission_type, Document_link, Submission_ID))
    #     databaseConnection.connection.commit()
    #     return True
    
    # def viewSubmission(self, Submission_ID):
    #     query = databaseConnection.connection.cursor()
    #     query.execute("SELECT * FROM Submissions WHERE Submission_ID = ?", (Submission_ID))
    #     return query.fetchone()
    
    # def viewAllSubmissionsForTeaceher(self):
    #     query = databaseConnection.connection.cursor()
    #     query.execute("SELECT * FROM Submissions")
    #     return query.fetchall()
