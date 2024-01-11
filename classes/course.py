import pyodbc
from databaseConnection import db
db=db()
class Course_class:
    def __init__(self, courseName, yearTeached, Semester, Capacity,teacher_name):
        self.courseName = courseName
        self.yearTeached = yearTeached
        self.Semester = Semester
        self.Capacity = Capacity
        self.teacher_name = teacher_name
        self.Number_enrolled = 0
    def createCourse(self):
        if len(self.teacher_name.split())!=2:
            return False
        else:
            first_name,second_name=self.teacher_name.split()[0],self.teacher_name.split()[1]
            db.cursor.execute("SELECT Email FROM Users WHERE First_Name = ? and Last_Name = ?", (first_name, second_name))
            teacher_email = db.cursor.fetchone()[0]
            if teacher_email == None:
                return False
            else:
                db.cursor.execute("SELECT TeacherID FROM Teachers WHERE Email = ?", (teacher_email))
                teacher_id = db.cursor.fetchone()[0]
                db.cursor.execute("SELECT COUNT(*) FROM Courses")
                db.cursor.execute("SELECT COUNT(*) FROM Courses")
                number_of_rows = db.cursor.fetchone()[0]
                Course_code='Cs'+str(number_of_rows+1)
                db.cursor.execute("insert into Courses(Name, Year, Semester, Course_Code, Capacity, Number_enrolled,TeacherID) values (?, ?, ?, ?, ?, ?,?)", (self.courseName, self.yearTeached, self.Semester, Course_code, self.Capacity,self.Number_enrolled,teacher_id))
                db.cursor.commit()
                return True

    def deleteCourse(self,Course_Code):
        db.cursor.execute('''delete from Courses where Course_Code = ?''', (Course_Code))
        db.cursor.commit()

