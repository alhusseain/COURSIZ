from users import users
from databaseConnection import db
db=db()
class teacher(users):

    def __init__(self, teacher_id):
        self.id = teacher_id
    def sign_up(self):
        db.cursor.execute('INSERT INTO Teachers (teacher_id, course_code) VALUES (?, ?)', ( self.teacher_id, self.course_code))
        db.connection.commit()
    
    def get_courses(self):
        db.cursor.execute("select Course_Code from Courses where TeacherID = ?", (self.id))
        fetched=[]
        for i in db.cursor.fetchall():
            i=i[0]
            fetched.append(i)
        return fetched




    # def studentsEntry(self, choice):
    #     if choice == "Sign in":
    #         self.sign_in(username, password)
    #     elif choice == "Sign up":
    #         self.sign_up(username, email, password)

    
