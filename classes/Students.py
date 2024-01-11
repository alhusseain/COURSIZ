from users import users
from databaseConnection import db
db=db()
class students(users):
    def __init__(self,id):
        self.id=id
    def addStudentToCourse(self,Course_Code):
        db.cursor.execute("SELECT Course_Code FROM Courses WHERE Course_Code = ?", (Course_Code))
        fetched=db.cursor.fetchone()
        if fetched is None:
            return False
        else:
            db.cursor.execute("select Capacity,Number_enrolled from Courses where Course_Code = ?", (Course_Code))
            fetched=db.cursor.fetchone()
            if fetched[0] is None:
                self.Number_enrolled=0
            else: self.Number_enrolled=fetched[0]
            # self.Capacity=fetched[1]
            # if self.Number_enrolled >= self.Capacity:
            #     return False
            # else:
            db.cursor.execute("update Courses set Number_enrolled = ? where Course_Code = ?", (self.Number_enrolled + 1 , Course_Code))
            db.cursor.commit()
            db.cursor.execute("insert into Enroll_in(Student_ID,Course_Code) values(?,?)", (self.id, Course_Code))
            db.cursor.commit()
            return True
    
    def removeStudentFromCourse(self,Course_Code):
        db.cursor.execute('''update Courses set Number_enrolled = ? where Course_Code = ?''', (self.Number_enrolled - 1 , Course_Code))
        db.cursor.commit()
        db.cursor.execute('''delete from Enroll_in where Student_ID = ? and Course_Code = ?''', (self.id, Course_Code))
        db.cursor.commit()
    
    def get_courses(self):
        db.cursor.execute("select Course_Code from Enroll_in where Student_ID = ?", (self.id))
        fetched=[]
        for i in db.cursor.fetchall():
            i=i[0]
            fetched.append(i)
        return fetched

