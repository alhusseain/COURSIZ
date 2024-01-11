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
    
    def get_courses_info(self):
        db.cursor.execute('Select Course_Code,Name from Teachers t join Courses c on t.TeacherID=c.TeacherID where t.TeacherID=?',(self.id))
        self.course_codes=[]
        list=db.cursor.fetchall()
        for i in list:
            i=i[0]
            self.course_codes.append(i)
        self.course_names=[]
        for i in list:
            i=i[1]
            self.course_names.append(i)
        return self.course_codes,self.course_names
    def get_students_in_course(self):
        self.course_students=[]
        for i in self.course_codes:
            current_students=[]
            for i in self.course_codes:
                db.cursor.execute('Select s.Student_ID,u.First_Name,u.Last_Name,u.Email  from students s join Users u on u.Email=s.Email join Enroll_in E on s.Student_ID=E.Student_ID where E.Course_Code=? ',(i))
                for j in db.cursor.fetchall():
                    current_students.append(j)
            self.course_students.append(current_students)
        return self.course_students



    # def studentsEntry(self, choice):
    #     if choice == "Sign in":
    #         self.sign_in(username, password)
    #     elif choice == "Sign up":
    #         self.sign_up(username, email, password)

    
