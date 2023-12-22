import pyodbc
connection=pyodbc.connect('Driver={SQL Server};SERVER=DESKTOP-9IHIA03;DATABASE=Coursiz;Trusted_Connection=yes')
cursor = connection.cursor()

class users:


    def __init__(self, email, password,First_name,Last_name,type):
        self.email = email
        self.password = password
        self.First_name=First_name
        self.Last_name=Last_name
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.type = None
        self.First_name = None
        self.last_name = None

    def set_type(self, types):
        self.type=types

    def sign_up(self):
          cursor.execute("INSERT INTO dbo.Users(Email,First_Name,Last_Name,Password, User_Type) VALUES(?,?,?,?,?)", (self.email,'ahmed','awad', self.password, 'teacher'))
          connection.commit()
    
    def sign_in_validation(self):
        cursor.execute("SELECT * FROM dbo.Users WHERE Email = ? AND Password = ?", (self.email, self.password))
        if cursor.fetchone() is not None:
            return True
        else:
            return False
    

    # def roleSelection(self, role):
    #     if role == "Student":
    #         student = students()
    #         student.studentsEntry()
    #     elif role == "Professor":
    #         prof = professors()
    #         prof.professorsEntry()
    #     elif role == "Supervisor":
    #         supervisor = supervisors()
    #         supervisor.supervisorsEntry()
    
    # def signIn(self, username, password):
    #     pass
    
    # def signUp(self, username, email, password):
    #     pass
    