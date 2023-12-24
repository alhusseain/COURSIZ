from users import *
import databaseConnection
c = connection.cursor()
class professors(users):
    def __init__(self, name, email, password, professorID):
        super().__init__(name, email, password)
        self.professorID = professorID
        
    # Will allow teachers to send to each student their grade
    def sendGrade(self, student, course, grade):
        c.execute('''insert into Enroll_in(Student_ID, Course_Code, grade)
            values (?, ?, ?)''', (student.studentID, course.courseCode, grade))
        c.commit()
        c.close()