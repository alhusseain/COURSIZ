import pyodbc
connection=pyodbc.connect('Driver={SQL Server};SERVER=KAREEM;DATABASE=Coursiz;Trusted_Connection=yes')
query = connection.cursor()

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
            query.execute("SELECT Email FROM Users WHERE First_Name = ? and Last_Name = ?", (first_name, second_name))
            teacher_email = query.fetchone()[0]
            if teacher_email == None:
                return False
            else:
                query.execute("SELECT TeacherID FROM Teachers WHERE Email = ?", (teacher_email))
                teacher_id = query.fetchone()[0]
                query.execute("SELECT COUNT(*) FROM Courses")
                query.execute("SELECT COUNT(*) FROM Courses")
                number_of_rows = query.fetchone()[0]
                Course_code='Cs'+str(number_of_rows+1)
                query.execute("insert into Courses(Name, Year, Semester, Course_Code, Capacity, Number_enrolled,TeacherID) values (?, ?, ?, ?, ?, ?,?)", (self.courseName, self.yearTeached, self.Semester, Course_code, self.Capacity,self.Number_enrolled,teacher_id))
                query.commit()
                return True

    def deleteCourse(self,Course_Code):
        query.execute('''delete from Courses where Course_Code = ?''', (Course_Code))
        query.commit()

