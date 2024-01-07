from users import users
import pyodbc
connection=pyodbc.connect('Driver={SQL Server};SERVER=DESKTOP-9IHIA03;DATABASE=Coursiz;Trusted_Connection=yes')
query = connection.cursor()
class teacher(users):

    def __init__(self, teacher_id):
        self.id = teacher_id
    def sign_up(self):
        query.execute('INSERT INTO Teachers (teacher_id, course_code) VALUES (?, ?)', ( self.teacher_id, self.course_code))
        connection.commit()
    
    def get_courses(self):
        query.execute("select Course_Code from Courses where TeacherID = ?", (self.id))
        fetched=[]
        for i in query.fetchall():
            i=i[0]
            fetched.append(i)
        return fetched




    # def studentsEntry(self, choice):
    #     if choice == "Sign in":
    #         self.sign_in(username, password)
    #     elif choice == "Sign up":
    #         self.sign_up(username, email, password)

    