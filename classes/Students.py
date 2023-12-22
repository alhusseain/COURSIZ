from classes.users import *

class students(users):

    def sign_up(self,student_id,course_codes):
        self.student_id=student_id
        self.course_code=[]
        for i in course_codes:
            self.course_code.append(i)
        cursor.execute('INSERT INTO students (student_id) VALUES (?)', ( self.student_id, self.course_code))
        connection.commit()