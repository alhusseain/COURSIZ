import pyodbc
# first install pyodbc using pip install pyodbc
# get the server name SQL Server
# create a new database in SQL Server
# then execute sql commands in the "SQL code.sql" file
# replace the server with your server name
# replace the database with your database name
class db:
    def __init__(self):
        self.connectionString = ('Driver={ODBC Driver 18 for SQL Server};Server=tcp:coursizdata.database.windows.net,1433;Database=finaldatabase;Uid=coursizsa;Pwd={ZC-coursiz};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
        self.connection = pyodbc.connect(self.connectionString)
        self.cursor = self.connection.cursor()
