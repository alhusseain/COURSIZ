import pyodbc
from databaseConnection import db
from datetime import datetime
db=db()

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
            db.cursor.execute("select Upload_ID from Uploads where Course_code = ?",self.course_code )
            for row in db.cursor.fetchall():
                self.up_id.append(row[0])

            db.cursor.execute("select Upload_header from Uploads where Course_code = ?", (self.course_code))
            for row in db.cursor.fetchall():
                self.up_header.append(row[0])
            
            db.cursor.execute("select Upload_type from Uploads where Course_code = ?", (self.course_code))
            for row in db.cursor.fetchall():
                self.up_type.append(row[0])
            
            db.cursor.execute("select Upload_description from Uploads where Course_code = ?", (self.course_code))
            for row in db.cursor.fetchall():
                self.up_desc.append(row[0])
            
            db.cursor.execute("select Document_link from Uploads where Course_code = ?", (self.course_code))
            for row in db.cursor.fetchall():
                self.up_link.append(row[0])

            db.cursor.execute("select Date_of_Upload from Uploads where Course_code=? ",(self.course_code))
            for row in db.cursor.fetchall():
                if row[0] is None:
                    self.up_date.append("No Date")
                else:
                    self.up_date.append(row[0]) 

    def insert_upload(self,header,type,description,link,course_code):
            self.today=datetime.now()
            self.today=self.today.strftime("%Y-%m-%d %H:%M:%S")
            db.cursor.execute("select count(*) from Uploads")
            self.id=db.cursor.fetchone()[0]+1
            db.cursor.execute("""INSERT INTO Uploads(Upload_ID,Upload_header,Upload_type,Upload_description,Document_link,Course_code,Date_of_Upload) VALUES(?,?,?,?,?,?,?)""",(self.id,header,type,description,link,course_code,self.today))
            db.cursor.commit()


        
        
