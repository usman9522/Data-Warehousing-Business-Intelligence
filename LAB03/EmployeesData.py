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

# Function to insert data into the Employees table
def insert_employee_data(cursor):
    existing_ids = set()

    # Fetch existing EmployeeIDs from the database
    cursor.execute("SELECT EmployeeID FROM Employees")
    for row in cursor.fetchall():
        existing_ids.add(row[0])

    # Generate unique EmployeeIDs
    while len(existing_ids) < 10:  # Ensure we have 10 unique EmployeeIDs
        EmployeeID = random.randint(100, 999)  # Generate random EmployeeID
        if EmployeeID not in existing_ids:
            existing_ids.add(EmployeeID)  # Add to existing IDs if it's unique
            LastName = fake.last_name()
            FirstName = fake.first_name()
            Title = fake.job()
            TitleOfCourtesy = random.choice(['Mr.', 'Mrs.', 'Ms.', 'Dr.'])
            BirthDate = fake.date_of_birth(minimum_age=18, maximum_age=65)
            HireDate = fake.date_this_decade()
            Address = fake.address().replace('\n', ', ')
            City = fake.city()
            Region = fake.state_abbr()
            PostalCode = fake.postcode()
            Country = fake.country()
            HomePhone = fake.phone_number()
            Extension = str(random.randint(1000, 9999))
            Photo = None  # Placeholder, as it's an image field
            Notes = fake.text(max_nb_chars=200)
            ReportsTo = None  # Null, or set as an EmployeeID from a previous insert
            PhotoPath = fake.image_url()

            # Insert data into Employees table
            try:
                cursor.execute('''
                    INSERT INTO Employees (EmployeeID, LastName, FirstName, Title, TitleOfCourtesy, BirthDate, HireDate, 
                                           Address, City, Region, PostalCode, Country, HomePhone, Extension, Photo, Notes, 
                                           ReportsTo, PhotoPath)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (EmployeeID, LastName, FirstName, Title, TitleOfCourtesy, BirthDate, HireDate, Address, City, 
                      Region, PostalCode, Country, HomePhone, Extension, Photo, Notes, ReportsTo, PhotoPath))
                print(f"Inserted EmployeeID={EmployeeID}, Name={FirstName} {LastName}, Title={Title}")
            except Exception as e:
                print(f"Error inserting EmployeeID={EmployeeID}: {e}")

    conn.commit()  # Save the changes

# Insert employee data
insert_employee_data(cursor)

# Close the connection
conn.close()
