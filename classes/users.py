import pyodbc
connection=pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:coursizdata.database.windows.net,1433;Database=finaldatabase;Uid=coursizsa;Pwd={ZC-coursiz};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = connection.cursor()
from datetime import datetime


class users:

    def __init__(self):
        self.email=None
        self.password=None
        self.First_name=None
        self.Last_name=None
        self.type=None
        self.today=None

    def sign_up_values(self, email, password,First_name,Last_name,type):
        self.email = email
        self.password = password
        self.First_name=First_name
        self.Last_name=Last_name
        self.type=type
        self.today=datetime.now()
        self.today=self.today.strftime("%Y-%m-%d %H:%M:%S")
    
    def sign_in_values(self, email, password):
        self.email = email
        self.password = password
        self.type = None
        self.First_name = None
        self.last_name = None

    def get_main(self,name,type,email,id):
        self.name=name
        self.type=type
        self.email=email
        self.id=id

    def sign_up(self):
          cursor.execute("INSERT INTO dbo.Users(Email,First_Name,Last_Name,Password, User_Type,Account_creation_date) VALUES(?,?,?,?,?,?)", (self.email,self.First_name,self.Last_name, self.password, self.type,self.today))
          connection.commit()

          if self.type == "Student":
              cursor.execute('SELECT MAX(Student_ID) FROM dbo.Students')
              max_student_id = cursor.fetchone()[0]
              if max_student_id is None:
                self.student_id = 1
              else:
                self.student_id = max_student_id + 1
              cursor.execute("INSERT INTO dbo.Students(Email,Student_ID) VALUES(?,?)", (self.email,self.student_id))
              connection.commit()
              print(cursor.messages)

          elif self.type == "Teacher":
              cursor.execute('SELECT MAX(TeacherID) FROM dbo.Teachers')
              max_teacher_id = cursor.fetchone()[0]
              if max_teacher_id is None:
                self.teacher_id = 1
              else:
                self.teacher_id = max_teacher_id + 1
              cursor.execute("INSERT INTO dbo.Teachers(Email,TeacherID) VALUES(?,?)", (self.email,self.teacher_id))
              connection.commit()
              print(cursor.messages)
          elif self.type == "Supervisor":
              cursor.execute('SELECT MAX(SuperVisorID) FROM dbo.Supervisors')
              max_supervisor_id = cursor.fetchone()[0]
              if max_supervisor_id is None:
                self.supervisor_id = 1
              else:
                self.supervisor_id = max_supervisor_id + 1
              cursor.execute("INSERT INTO dbo.SuperVisors(Email,SupervisorID) VALUES(?,?)", (self.email,self.supervisor_id))
              connection.commit()
              print(cursor.messages)

    def sign_in_validation(self):
        cursor.execute("SELECT * FROM dbo.Users WHERE Email = ? AND Password = ?", (self.email, self.password))
        if cursor.fetchone() is not None:
            return True
        else:
            return False
    
    def sign_in_get_data(self):
        cursor.execute('SELECT User_Type FROM dbo.Users WHERE Email = ?', (self.email))
        self.type = cursor.fetchone()[0]
        cursor.execute('SELECT First_Name,Last_Name FROM dbo.Users WHERE Email = ?', (self.email))
        fetched=cursor.fetchone()
        self.First_name = fetched[0]
        self.Last_name = fetched[1]

        if self.type == "Student":
            cursor.execute('SELECT Student_ID FROM dbo.Students WHERE Email = ?', (self.email))
            self.student_id = cursor.fetchone()[0]
            return self.First_name,self.Last_name, self.student_id,self.type
        if self.type == "Teacher":
            cursor.execute('SELECT TeacherID FROM dbo.Teachers WHERE Email = ?', (self.email))
            self.teacher_id = cursor.fetchone()[0]
            return self.First_name, self.Last_name, self.teacher_id,self.type
        if self.type=="Supervisor":
            cursor.execute('SELECT SupervisorID FROM dbo.Supervisors WHERE Email = ?', (self.email))
            self.supervisor_id = cursor.fetchone()[0]
            return self.First_name, self.Last_name, self.supervisor_id,self.type
    
    # def course_info():




# user=users()
# user.sign_up_values('husseainshalaby8@gmail.com','1234567899','hussein','shalaby','Student')
# user.sign_up()

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
    
