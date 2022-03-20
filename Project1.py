import mysql.connector
conn = mysql.connector.connect(
   host='localhost',
   user='root',
   password='Degavath75@',database='Management')
cursor = conn.cursor()
# create database
cursor.execute("CREATE DATABASE Management ")
cursor.execute('Show DATABASES;')

# for creating table1  department 
cursor.execute("create table Department ( Dep_id int,dep_name varchar(255),dep_Location varchar(200))")

# Show the tables
cursor.execute('Show tables;')
for i in cursor:
    print(i)

# Creting new row
cursor.execute('ALTER TABLE employee ADD salary integer')
# for createing table2 employee
cursor.execute("create table employee( Emp_id int,Firstname varchar(255),LastName varchar(255),Job_name varchar(255), Email varchar(255),Address varchar(255), Blood_group varchar(255),phone_No int,Age int)")

# for creating table3 Salary_grade
cursor.execute("create table Salary_Grad (Grade int,min_salary int,max_salary int)")

# for creating table4 Employee details
cursor.execute("create table Employee_details (Emp_DOJ DATE,Emp_DOL DATE,EMP_Time TIME,Status varchar(200),Promotion varchar(200))")

# insert table1 Department 
sql= "INSERT INTO Department (Dep_id,dep_name ,dep_Location) VALUES (%s,%s,%s) "
val=[(1,"BANK manager","Telangana"),(2,"ISA","Telangana"),(3,"Manager","Hyderabad"),(4,"HR","Chhattisgarh"),(5,"Teacher","kamareddy")]
cursor.executemany(sql,val)
conn.commit()
print(cursor.rowcount,"record insert")

# Select
cursor.execute("SELECT * FROM Department ")
myresult =cursor.fetchall()
for x in myresult:
  print(x)

#  Where
sql = "SELECT * FROM Department WHERE dep_Location LIKE '%na%'"
cursor.execute(sql)
myresult = cursor.fetchall()
for x in myresult:
  print(x)

# ORDEY
sql = "SELECT * FROM Department ORDER BY dep_name  DESC"
cursor.execute(sql)
myresult = cursor.fetchall()
for x in myresult:
  print(x)

#  Update
sql = "UPDATE Department SET dep_name = 'Developer' WHERE Dep_id = 1"
cursor.execute(sql)
conn.commit()
print(cursor.rowcount, "record(s) affected")
cursor.execute('SELECT * FROM Department')
for i in cursor:
   print(i)




# insert table employee
sql = 'INSERT INTO employee (Emp_id,Firstname,LastName,Job_name,Email,Address,Blood_group,phone_No,Age,salary,Dep_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val = [(1,"Degavath","Mamatha","BANK manager","mamatha20@navgurukul.org","Telangana","B+",90111013,22,65000,1),
(2,"Degavath","Thirupathi","IAS","thirupathi20@navgurukul.org","Telangana","A",82435422,20,850000,2),
(3,"Lakavath","Santosh","Manager","santoshlakavath@gmail.com","Hyderabad","B+",85008331,24,750000,3),
(4,"Andan","kalyan","HR","andankalyan@gmail.com","Chhattisgarh","A",82478411,20,950000,4),
(5,"malavath","Ruthika","Teacher","malavathruthika@gmail.com","kamareddy","O", 90103423,18,650000,5)]
cursor.executemany(sql,val)
conn.commit()
print(cursor.rowcount,"record insert")


#insert table Salary_Grad 
sql = 'INSERT INTO  Salary_Grad (Grade,min_salary,max_salary) VALUES (%s,%s,%s)'
val =[(1,65000,80000),(2,85000,90000),(3,75000,80000),(4,950000,980000),(5,650000,900000)]
cursor.executemany(sql,val)
conn.commit()
print(cursor.rowcount,"record insert")

# insert table Employee_details 
sql ="INSERT INTO   Employee_details (Emp_DOJ ,Emp_DOL  ,Status ,Promotion ) VALUES (%s,%s,%s,%s)"
val =[('2000-7-2','2050-6-20',"Working","YES"),
('2008-5-8','2050-6-20',"Working","YES"),('2004-9-4','2050-6-20',"Working","No")]
cursor.executemany(sql,val)
conn.commit()
print(cursor.rowcount,"record insert")


# Delecting col
cursor.execute('ALTER TABLE Employee_details DROP COLUMN  EMP_Time ')


#  Joining table
sql = "SELECT \
   employee.Dep_id AS user, \
   Department.Dep_id AS id \
   FROM Department \
   INNER JOIN employee ON employee.Dep_id = Department.Dep_id"
cursor.execute(sql)
for i in cursor:
   print(i)
