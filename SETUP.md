# Quick Setup Guide

## Prerequisites Checklist

- [ ] Microsoft SQL Server installed
- [ ] Python 3.7+ installed  
- [ ] Required Python packages installed

## Step-by-Step Setup

### 1. Install Python Dependencies
```bash
pip install pyodbc pandas
```

### 2. Create Databases in SQL Server
```sql
-- Connect to SQL Server and create databases
CREATE DATABASE lab03;
CREATE DATABASE nwdatawarehouse;
```

### 3. Update Connection Strings
Edit the server name in Python scripts to match your SQL Server instance:

**Find and replace in all .py files:**
- `DESKTOP-TIBJBLC\\USMAN` → `YOUR_SERVER_NAME`
- `DESKTOP-U2H7KFI\\SQLEXPRESS` → `YOUR_SERVER_NAME`

### 4. Test Your Setup
```bash
python test_setup.py
```

### 5. Run LAB03 (OLTP Database)
```bash
cd LAB03
python creatingtables.py
python CategoriesData.py
python CustomersData.py
python ProductsData.py
python OrdersData.py
python OrdersDetailsData.py
python EmployeesData.py
python SuppliersData.py
python ShippersData.py
python RegionsAndTerritories.py
python EmployeesTerritoriesData.py
```

### 6. Run lab5 (Data Warehouse)
```bash
cd ../lab5
python datawarehouse.py
# Then execute LAB5_data.txt in SQL Server Management Studio
```

### 7. Test Business Intelligence Queries
Execute the queries in `lab5/QUERIES.txt` to see analytical results.

## Common Issues

**Connection Errors:**
- Ensure SQL Server is running
- Check Windows Authentication is enabled
- Verify database names exist
- Update server names in connection strings

**Driver Errors:**
- Install SQL Server ODBC drivers
- Use appropriate driver name for your system

**Data Loading Errors:**
- Check CSV file paths are correct
- Verify table schemas match data structure
- Ensure foreign key constraints are satisfied

## File Structure Quick Reference

```
LAB03/                  # OLTP Implementation
├── *.csv              # Source data files
├── creatingtables.py  # Create database schema
└── *Data.py           # Load data from CSV

lab5/                   # Data Warehouse Implementation  
├── datawarehouse.py   # Create DW schema
├── LAB5_data.txt      # Sample data inserts
└── QUERIES.txt        # BI analytical queries
```