import sqlite3

## Connect to the SQlite DAtabase
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record, create table

cursor=connection.cursor()

## Create a table

table_info="""
CREATE TABLE STUDENT(NAME VARCHAR(50),CLASS VARCHAR(50),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

##Insert records

cursor.execute("""Insert Into STUDENT values('Om','Data Science','A',88)""")
cursor.execute("""Insert Into STUDENT values('Ram','Data Science','B',78)""")
cursor.execute("""Insert Into STUDENT values('Shyam','DEVOPS','A',82)""")
cursor.execute("""Insert Into STUDENT values('Shiva','DEVOPS','A',66)""")
cursor.execute("""Insert Into STUDENT values('Hari','Data Science','B',56)""")

#Display all the records

print("The Inserted Records Are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int the databse
connection.commit()
connection.close()