import pyodbc
import pyodbc
connection=pyodbc.connect('Driver={SQL Server};SERVER=DESKTOP-9IHIA03;DATABASE=Coursiz;Trusted_Connection=yes')
query = connection.cursor()

class upload:
    def upload_info(self,course_code):
            self.course_code=course_code
            query.execute("select Upload_ID from Uploads where Course_Code = ?",self.course_code )
            self.up_id=[]
            for row in query.fetchall():
                self.up_id.append(row[0])

            query.execute("select Upload_header from Uploads where Course_Code = ?", (self.course_code))
            
            self.up_header=[]
            for row in query.fetchall():
                self.up_header.append(row[0])
            
            query.execute("select Upload_type from Uploads where Course_Code = ?", (self.course_code))
            
            self.up_type=[]
            for row in query.fetchall():
                self.up_type.append(row[0])
            
            query.execute("select Upload_description from Uploads where Course_Code = ?", (self.course_code))
            
            self.up_desc=[]
            for row in query.fetchall():
                self.up_desc.append(row[0])
            
            query.execute("select Document_link from Uploads where Course_Code = ?", (self.course_code))
            
            self.up_link=[]
            for row in query.fetchall():
                self.up_link.append(row[0])


        
        