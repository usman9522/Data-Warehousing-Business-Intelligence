import pyodbc
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Connect to the SQL Server database
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-TIBJBLC\\USMAN;"
    "Database=lab03;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()
# Test insert single hard-coded value
try:
    cursor.execute('''
        INSERT INTO Employees (EmployeeID, LastName, FirstName, Title, TitleOfCourtesy, BirthDate, HireDate, 
                               Address, City, Region, PostalCode, Country, HomePhone, Extension, Photo, Notes, 
                               ReportsTo, PhotoPath)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (1000, 'Doe', 'John', 'Developer', 'Mr.', '1985-01-01', '2023-01-01', 
          '123 Main St', 'Sample City', 'SC', '12345', 'Country', '123-456-7890', '1234', None, 
          'Some notes', None, 'http://example.com/photo.jpg'))
    conn.commit()
    print("Hard-coded row inserted successfully!")

    

except Exception as e:
    print(f"Error inserting hard-coded row: {e}")
cursor.close()
conn.close()
