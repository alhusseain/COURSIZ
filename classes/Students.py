from users import users
import pyodbc
connection=pyodbc.connect('Driver={SQL Server};SERVER=DESKTOP-9IHIA03;DATABASE=Coursiz;Trusted_Connection=yes')
query = connection.cursor()
class students(users):
    def __init__(self,id):
        self.id=id
    def addStudentToCourse(self,Course_Code):
        query.execute("SELECT Course_Code FROM Courses WHERE Course_Code = ?", (Course_Code))
        fetched=query.fetchone()
        if fetched is None:
            return False
        else:
            query.execute("select Capacity,Number_enrolled from Courses where Course_Code = ?", (Course_Code))
            fetched=query.fetchone()
            if fetched[0] is None:
                self.Number_enrolled=0
            else: self.Number_enrolled=fetched[0]
            # self.Capacity=fetched[1]
            # if self.Number_enrolled >= self.Capacity:
            #     return False
            # else:
            query.execute("update Courses set Number_enrolled = ? where Course_Code = ?", (self.Number_enrolled + 1 , Course_Code))
            query.commit()
            query.execute("insert into Enroll_in(Student_ID,Course_Code) values(?,?)", (self.id, Course_Code))
            query.commit()
            return True
    
    def removeStudentFromCourse(self,Course_Code):
        query.execute('''update Courses set Number_enrolled = ? where Course_Code = ?''', (self.Number_enrolled - 1 , Course_Code))
        query.commit()
        query.execute('''delete from Enroll_in where Student_ID = ? and Course_Code = ?''', (self.id, Course_Code))
        query.commit()
    
    def get_courses(self):
        query.execute("select Course_Code from Enroll_in where Student_ID = ?", (self.id))
        fetched=[]
        for i in query.fetchall():
            i=i[0]
            fetched.append(i)
        return fetched