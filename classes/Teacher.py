from classes.users import *

class teacher(users):
    def __init__(self, teacher_id, course_code):
        self.teacher_id = teacher_id
        self.course_code = course_code
    def sign_up(self):
        cursor.execute('INSERT INTO Teachers (teacher_id, course_code) VALUES (?, ?)', ( self.teacher_id, self.course_code))
        connection.commit()
    



    # def studentsEntry(self, choice):
    #     if choice == "Sign in":
    #         self.sign_in(username, password)
    #     elif choice == "Sign up":
    #         self.sign_up(username, email, password)

    