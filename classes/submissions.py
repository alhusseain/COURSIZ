import databaseConnection


class submissions:
    def __init__(self, Submission_ID, Submission_type, studentID, Document_link):
        self.Submission_ID = Submission_ID
        self.Submission_type = Submission_type
        self.Deadline_Date = Deadline_Date
        self.Document_link = Document_link
        self.studentID = studentID

        
    def createSubmission(self, Document_link, Submission_type, course):
        query = databaseConnection.connection.cursor()
        if document_link is None:
            return False
        elif document_link.startswith("https://docs.google.com/") and document_link.endswith("/sharing"):
            query.execute("SELECT COUNT(*) FROM Submissions")
            number_of_rows = query.fetchone()[0]
            Submission_ID = number_of_rows + 1
            Submission_type = "Document"
            query.execute("INSERT INTO Submissions(Submission_ID, Submission_type, studentID, Document_link, Course_Code) VALUES(?, ?, ?, ?, ?)", (Submission_ID, Submission_type, studentID, Document_link, courseCode))
            databaseConnection.connection.commit()
            return True
        elif document_link.startswith("https://github.com/"):
            query.execute("SELECT COUNT(*) FROM Submissions")
            number_of_rows = query.fetchone()[0]
            Submission_ID = number_of_rows + 1
            Submission_type = "Project"
            query.execute("INSERT INTO Submissions(Submission_ID, Submission_type, studentID, Document_link, Course_Code) VALUES(?, ?, ?, ?, ?)", (Submission_ID, Submission_type, studentID, Document_link, courseCode))
            databaseConnection.connection.commit()
            return True
        else:
            query.execute("SELECT COUNT(*) FROM Submissions")
            number_of_rows = query.fetchone()[0]
            Submission_ID = number_of_rows + 1
            query.execute("INSERT INTO Submissions(Submission_ID, Submission_type, studentID, Document_link, Course_Code) VALUES(?, ?, ?, ?, ?)", (Submission_ID, Submission_type, studentID, Document_link, courseCode))
            databaseConnection.connection.commit()
            return True
        
    def deleteSubmission(self, Submission_ID):
        query = databaseConnection.connection.cursor()
        query.execute("DELETE FROM Submissions WHERE Submission_ID = ?", (Submission_ID))
        databaseConnection.connection.commit()
        return True
    
    def updateSubmission(self, Submission_ID, Submission_type, Document_link):
        query = databaseConnection.connection.cursor()
        query.execute("UPDATE Submissions SET Submission_type = ?, Document_link = ? WHERE Submission_ID = ?", (Submission_type, Document_link, Submission_ID))
        databaseConnection.connection.commit()
        return True
    
    def viewSubmission(self, Submission_ID):
        query = databaseConnection.connection.cursor()
        query.execute("SELECT * FROM Submissions WHERE Submission_ID = ?", (Submission_ID))
        return query.fetchone()
    
    def viewAllSubmissionsForTeaceher(self):
        query = databaseConnection.connection.cursor()
        query.execute("SELECT * FROM Submissions")
        return query.fetchall()