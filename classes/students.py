from users import users
import databaseConnection

class students(users):
    def __init__(self, name, email, password, studentID):
        super().__init__(name, email, password)
        self.studentID = studentID

        