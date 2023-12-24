import pyodbc


connectionString = (
    r'DRIVER={SQL Server};'
    r'SERVER=DESKTOP-0TH5VGS\SQLEXPRESS;'
    r'DATABASE=Coursiz;'
    r'Trusted_Connection=yes;'
)
connection = pyodbc.connect(connectionString)
    