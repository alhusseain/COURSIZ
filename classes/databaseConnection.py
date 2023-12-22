import pyodbc

# first install pyodbc using pip install pyodbc
# get the server name SQL Server
# create a new database in SQL Server
# then execute sql commands in the "SQL code.sql" file
# replace the server with your server name
# replace the database with your database name
connectionString = (
    r'DRIVER={SQL Server};'
    r'SERVER= server;'
    r'DATABASE= databaseName;'
    r'Trusted_Connection=yes;'
)
connection = pyodbc.connect(connectionString)
cursor = connection.cursor()
