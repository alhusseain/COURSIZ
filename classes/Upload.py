import pyodbc
import pyodbc
connection=pyodbc.connect('Driver={SQL Server};SERVER=DESKTOP-9IHIA03;DATABASE=Coursiz;Trusted_Connection=yes')
query = connection.cursor()
from datetime import datetime

class upload:
    def __init__(self):
        self.up_id=[]
        self.up_header=[]
        self.up_type=[]
        self.up_desc=[]
        self.up_link=[]
        self.up_date=[]
    def upload_info(self,course_code):
            self.course_code=course_code
            query.execute("select Upload_ID from Uploads where Course_code = ?",self.course_code )
            for row in query.fetchall():
                self.up_id.append(row[0])

            query.execute("select Upload_header from Uploads where Course_code = ?", (self.course_code))
            for row in query.fetchall():
                self.up_header.append(row[0])
            
            query.execute("select Upload_type from Uploads where Course_code = ?", (self.course_code))
            for row in query.fetchall():
                self.up_type.append(row[0])
            
            query.execute("select Upload_description from Uploads where Course_code = ?", (self.course_code))
            for row in query.fetchall():
                self.up_desc.append(row[0])
            
            query.execute("select Document_link from Uploads where Course_code = ?", (self.course_code))
            for row in query.fetchall():
                self.up_link.append(row[0])

            query.execute("select Date_of_Upload from Uploads where Course_code=? ",(self.course_code))
            for row in query.fetchall():
                if row[0] is None:
                    self.up_date.append("No Date")
                else:
                    self.up_date.append(row[0]) 

    def insert_upload(self,header,type,description,link,course_code):
            self.today=datetime.now()
            self.today=self.today.strftime("%Y-%m-%d %H:%M:%S")
            query.execute("select count(*) from Uploads")
            id=query.fetchone()[0]+1
            query.execute("""INSERT INTO Uploads(Upload_ID,Upload_header,Upload_type,Upload_description,Document_link,Course_code,Date_of_Upload) VALUES(?,?,?,?,?,?,?)""",(id,header,type,description,link,course_code,self.today))
            connection.commit()


        
        