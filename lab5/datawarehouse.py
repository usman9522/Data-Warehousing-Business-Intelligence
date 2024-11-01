import pyodbc

# Establish the connection
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-U2H7KFI\\SQLEXPRESS;"
    "Database=nwdatawarehouse;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

# Drop tables if they exist to avoid conflicts
tables = [
    "Sales", "Employee", "Customer", "Supplier", "Product", "Category", "Time",
    "Shipper", "Territories", "City", "State", "Country", "Continent"
]
for table in tables:
    cursor.execute(f"IF OBJECT_ID('{table}', 'U') IS NOT NULL DROP TABLE {table};")
conn.commit()

# Table creation scripts with CustomerKey as surrogate key
create_table_queries = [
    """
    CREATE TABLE Continent (
        ContinentKey INT PRIMARY KEY,
        ContinentName NVARCHAR(50)
    );
    """,
    
    """
    CREATE TABLE Country (
        CountryKey INT PRIMARY KEY,
        CountryName NVARCHAR(50),
        CountryCode NVARCHAR(10),
        CountryCapital NVARCHAR(50),
        Population BIGINT,
        Subdivision NVARCHAR(50),
        ContinentKey INT FOREIGN KEY REFERENCES Continent(ContinentKey)
    );
    """,
    
    """
    CREATE TABLE State (
        StateKey INT PRIMARY KEY,
        StateName NVARCHAR(50),
        EnglishStateName NVARCHAR(50),
        StateType NVARCHAR(50),
        StateCode NVARCHAR(10),
        StateCapital NVARCHAR(50),
        RegionName NVARCHAR(50),
        RegionCode NVARCHAR(10),
        CountryKey INT FOREIGN KEY REFERENCES Country(CountryKey)
    );
    """,
    
    """
    CREATE TABLE City (
        CityKey INT PRIMARY KEY,
        CityName NVARCHAR(50),
        StateKey INT FOREIGN KEY REFERENCES State(StateKey),
        CountryKey INT FOREIGN KEY REFERENCES Country(CountryKey)
    );
    """,
    
    """
    CREATE TABLE Category (
        CategoryKey INT PRIMARY KEY,
        CategoryName NVARCHAR(50),
        Description NVARCHAR(250)
    );
    """,
    
    """
    CREATE TABLE Supplier (
        SupplierKey INT PRIMARY KEY,
        CompanyName NVARCHAR(50),
        Address NVARCHAR(100),
        PostalCode NVARCHAR(20),
        CityKey INT FOREIGN KEY REFERENCES City(CityKey)
    );
    """,
    
    """
    CREATE TABLE Product (
        ProductKey INT PRIMARY KEY,
        ProductName NVARCHAR(50),
        QuantityPerUnit NVARCHAR(50),
        UnitPrice DECIMAL(10, 2),
        Discontinued BIT,
        CategoryKey INT FOREIGN KEY REFERENCES Category(CategoryKey)
    );
    """,
    
    # Customer table with CustomerKey as a surrogate key (IDENTITY)
    """
    CREATE TABLE Customer (
        CustomerKey INT IDENTITY PRIMARY KEY,
        CustomerID NVARCHAR(50) UNIQUE,
        CompanyName NVARCHAR(50),
        Address NVARCHAR(100),
        PostalCode NVARCHAR(20),
        CityKey INT FOREIGN KEY REFERENCES City(CityKey)
    );
    """,
    
    """
    CREATE TABLE Employee (
        EmployeeKey INT PRIMARY KEY,
        FirstName NVARCHAR(50),
        LastName NVARCHAR(50),
        Title NVARCHAR(50),
        BirthDate DATE,
        HireDate DATE,
        Address NVARCHAR(100),
        City NVARCHAR(50),
        Region NVARCHAR(50),
        PostalCode NVARCHAR(20),
        Country NVARCHAR(50),
        SupervisorKey INT FOREIGN KEY REFERENCES Employee(EmployeeKey)
    );
    """,
    
    """
    CREATE TABLE Time (
        TimeKey INT PRIMARY KEY,
        Date DATE UNIQUE,
        DayNbWeek INT,
        DayNameWeek NVARCHAR(50),
        DayNbMonth INT,
        DayNbYear INT,
        WeekNbYear INT,
        MonthNumber INT,
        MonthName NVARCHAR(50),
        Quarter INT,
        Semester INT,
        Year INT
    );
    """,
    
    """
    CREATE TABLE Shipper (
        ShipperKey INT PRIMARY KEY,
        CompanyName NVARCHAR(50)
    );
    """,
    
    """
   CREATE TABLE Sales (
    CustomerKey INT,
    EmployeeKey INT,
    OrderDateKey INT,
    DueDateKey INT,
    ShippedDateKey INT,
    ShipperKey INT,
    ProductKey INT,
    SupplierKey INT,
    OrderNo INT,
    OrderLineNo INT,
    UnitPrice DECIMAL(10, 2),
    Quantity INT,
    Discount DECIMAL(5, 2),
    SalesAmount DECIMAL(10, 2),
    Freight DECIMAL(10, 2),
    PRIMARY KEY (CustomerKey, EmployeeKey, OrderDateKey, DueDateKey, ShippedDateKey, ShipperKey, ProductKey,SupplierKey),
    FOREIGN KEY (CustomerKey) REFERENCES Customer(CustomerKey),
    FOREIGN KEY (EmployeeKey) REFERENCES Employee(EmployeeKey),
    FOREIGN KEY (OrderDateKey) REFERENCES Time(TimeKey),
    FOREIGN KEY (DueDateKey) REFERENCES Time(TimeKey),
    FOREIGN KEY (ShippedDateKey) REFERENCES Time(TimeKey),
    FOREIGN KEY (ShipperKey) REFERENCES Shipper(ShipperKey),
    FOREIGN KEY (ProductKey) REFERENCES Product(ProductKey),
    FOREIGN KEY (SupplierKey) REFERENCES Supplier(SupplierKey)
);

    """,
    
    """
    CREATE TABLE Territories (
        EmployeeKey INT FOREIGN KEY REFERENCES Employee(EmployeeKey),
        CityKey INT FOREIGN KEY REFERENCES City(CityKey)
    );
    """
]

# Execute each table creation script
# for query in create_table_queries:
#     cursor.execute(query)
#     pass

# Close the connection

print("Tables created successfully with CustomerKey as surrogate key in Customer table.")

# ------------------------------------------------------------------------------------------------

# Close the connection




conn.commit()
cursor.close()
conn.close()