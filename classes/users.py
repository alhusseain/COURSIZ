
class users:
    def roleSelection(self, role):
        if role == "Student":
            student = students()
            student.studentsEntry()
        elif role == "Professor":
            prof = professors()
            prof.professorsEntry()
        elif role == "Supervisor":
            supervisor = supervisors()
            supervisor.supervisorsEntry()
    
    def signIn(self, username, password):
        pass
    
    def signUp(self, username, email, password):
        pass
    