import pyodbc
# first install pyodbc using pip install pyodbc
# get the server name SQL Server
# create a new database in SQL Server
# then execute sql commands in the "SQL code.sql" file
# replace the server with your server name
# replace the database with your database name
class db:
    def __init__(self):
        self.connectionString = ('Driver={SQL Server};SERVER=DESKTOP-9IHIA03;DATABASE=Coursiz;Trusted_Connection=yes')
        self.connection = pyodbc.connect(self.connectionString)
        self.cursor = self.connection.cursor()
