# Importing essential libraries like sqllite to connect the database with code
import sqlite3
from datetime import datetime

#connect to or create the database
db_path = '/Users/rishikeshsingh/Library/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/TimesheetDB'
conn = sqlite3.connect(db_path)


cursor = conn.cursor()

#Input values from user
emp_id = int(input("Enter the employee_id of the resource: "))
end_date = input("Enter the end date of employee: ")
emp_status = input("Enter the updated status of the employee: ")

# Check tables in the DB
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()
# print("Tables in DB:", tables)

########################### create table for testing #############################
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS ResourceMaster(
#                Employee_ID INTEGER PRIMARY KEY,
#                NAME Text,
#                StartDate Text,
#                EndDate Text,
#                Employee_Status Text
#                )
#                ''')

# # sample data

# cursor.execute("INSERT INTO ResourceMaster VALUES(101, 'Rishikesh', '02-05-2022','31-12-9999','Active')")
# cursor.execute("INSERT INTO ResourceMaster VALUES(102, 'Ankit', '01-01-2022','31-12-9999','Active')")
# cursor.execute("INSERT INTO ResourceMaster VALUES(103, 'Vishal Rathour', '03-05-2022','31-12-9999','Active')")
# cursor.execute("INSERT INTO ResourceMaster VALUES(104, 'Prince Goyal', '04-07-2022','31-12-9999','Active')")
# cursor.execute("INSERT INTO ResourceMaster VALUES(105, 'Kedharnath Punnusawamy', '05-11-2022','31-12-9999','Active')")
# cursor.execute("INSERT INTO ResourceMaster VALUES(106, 'Hemant Kumar', '11-06-2022','31-12-9999','Active')")
# cursor.execute("INSERT INTO ResourceMaster VALUES(107, 'Artemio Matinez', '01-01-2021','31-12-9999','Active')")


# conn.commit()
# print("✅ New DB and table created at:", db_path)

########################### create table for testing #############################


########################### retreving the data from database #############################

# cursor.execute("select * from ResourceMaster where Employee_Id = ?",(emp_id,))
# result = cursor.fetchone()
# print(f"Records: {result}")

########################### retreving the data from database #############################

########################### updating the data into database #############################

cursor.execute("update ResourceMaster set EndDate = ?, Employee_Status = ? where Employee_Id = ? and Employee_Status = 'Active'",(end_date,emp_status,emp_id))
update_count = cursor.rowcount
print(f"✅ Row updated successfully: {update_count}")
cursor.execute("select * from ResourceMaster where Employee_Id=?",(emp_id,))
result = cursor.fetchone()
print(f"After updatation the updated row is:  {result}")


conn.close()