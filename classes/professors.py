from users import *

class professors(users):
    def sign_in(self, username, password):
        if username == "1" and password == "1":
            return true
        else:
            return false

    def sign_up(self, username, email, password):
        return username, email, password
    
    def studentsEntry(self, choice):
        if choice == "Sign in":
            self.sign_in(username, password)
        elif choice == "Sign up":
            self.sign_up(username, email, password)

    