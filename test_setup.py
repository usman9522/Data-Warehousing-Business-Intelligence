#!/usr/bin/env python3
"""
Database Connection Test Script
This script validates the database setup for the Data Warehousing & BI project.
"""

import pyodbc
import sys

def test_connection(connection_string, db_name):
    """Test database connection and return status."""
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        # Test basic query
        cursor.execute("SELECT 1 as test")
        result = cursor.fetchone()
        
        conn.close()
        
        if result and result[0] == 1:
            print(f"✅ {db_name} connection successful!")
            return True
        else:
            print(f"❌ {db_name} connection failed - query test failed")
            return False
            
    except Exception as e:
        print(f"❌ {db_name} connection failed: {str(e)}")
        return False

def main():
    """Main test function."""
    print("🔧 Testing Database Connections for Data Warehousing Project")
    print("=" * 60)
    
    # Test LAB03 connection
    lab03_conn = (
        "Driver={SQL Server};"
        "Server=localhost;"  # Update with your server name
        "Database=lab03;"
        "Trusted_Connection=yes;"
    )
    
    # Test lab5 connection  
    lab5_conn = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost;"  # Update with your server name
        "Database=nwdatawarehouse;"
        "Trusted_Connection=yes;"
    )
    
    print("\n📊 Testing LAB03 (OLTP Database)...")
    lab03_success = test_connection(lab03_conn, "LAB03")
    
    print("\n🏭 Testing lab5 (Data Warehouse)...")
    lab5_success = test_connection(lab5_conn, "lab5")
    
    print("\n" + "=" * 60)
    
    if lab03_success and lab5_success:
        print("🎉 All connections successful! You're ready to start the labs.")
        print("\n💡 Next steps:")
        print("   1. Run LAB03/creatingtables.py to create OLTP schema")
        print("   2. Load data using LAB03/*Data.py scripts") 
        print("   3. Run lab5/datawarehouse.py to create DW schema")
        print("   4. Execute lab5/LAB5_data.txt to load sample data")
        return 0
    else:
        print("⚠️  Some connections failed. Please check:")
        print("   - SQL Server is running")
        print("   - Databases 'lab03' and 'nwdatawarehouse' exist")
        print("   - Update server name in connection strings")
        print("   - pyodbc is installed: pip install pyodbc")
        return 1

if __name__ == "__main__":
    sys.exit(main())