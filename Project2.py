import mysql.connector
# connection with Database 
conne =mysql.connector.connect(host='localhost',user='root',password='Degavath75@',database='Restaurants')
cursor =conne.cursor()
#Creating Database
cursor.execute("CREATE DATABASE Restaurants")
cursor.execute("Show DATABASES;")


# for creating table1(user) 
cursor.execute("create table USER (User_id int,Fname varchar(50),Lname varchar(50),Password varchar(50))")

# insert user (table)
sql =" INSERT INTO USER (User_id,Fname,Lname,Password) VALUES (%s,%s,%s,%s)"
val=(1,'Degavath',"Mamatha","Degavath123@")
cursor.execute(sql,val)
conne.commit()
print(cursor.rowcount,"record insert")

# Delecting col
cursor.execute('ALTER TABLE USER DROP COLUMN Password')

# Update
sql = "UPDATE USER SET Fname = 'Rathod' WHERE User_id = 1"
cursor.execute(sql)
conne.commit()
print(cursor.rowcount, "record(s) affected")
cursor.execute('SELECT * FROM USER')
for i in cursor:
   print(i)

 # Select
cursor.execute("SELECT * FROM USER WHERE Lname LIKE '%tha%' ")
myresult=cursor.fetchall()
for x in myresult:
    print(x)

# ORDEY
sql = "SELECT * FROM USER ORDER BY  Fname DESC"
cursor.execute(sql)
myresult = cursor.fetchall()
for x in myresult:
  print(x)

# Joining table
sql = 'SELECT OWNER.Fname,User_id FROM USER \
    INNER JOIN OWNER ON OWNER.Fname = USER.Fname'



# creating table2(Restaurant)
cursor.execute("create table Restaurant(Name varchar(100),Location varchar(100),Contact varchar(100),Opening_Closing_Time varchar(100),Details varchar(200))")

# insert Restaurant (table)
sql = "INSERT INTO Restaurant (Name,Location,Contact,Opening_Closing_Time,Details) VALUES (%s,%s,%s,%s,%s)"
val=("Tandoori By Nature","Gannaram at Telangana","9010478592","10:00 AM - 12:00 AM","None")
cursor.execute(sql,val)
conne.commit()
print(cursor.rowcount,"record insert")

# Delecting
cursor.execute('ALTER TABLE Restaurant DROP COLUMN Details')

# Update table
sql = "UPDATE USER SET Fname =%s WHERE Fname =%s"
val =("Degavath","Lakavath")
cursor.execute(sql,val)
conne.commit()
print(cursor.rowcount,"record(s) affected")

# creating table3(OWNER)
cursor.execute("create table OWNER (Fname varchar(15),Lname varchar(15),Contact varchar(100),Rest_Name varchar(200))")

# insert table(owner)
sql="INSERT INTO OWNER (Fname,Lname,Contact,Rest_Name) VALUES (%s,%s,%s,%s)"
val =("Degavath","Mamatha","9010478592","Tandoori By Nature")
cursor.execute(sql,val)
conne.commit()
print(cursor.rowcount,"record(s) affected")

# creating table4(menu)
cursor.execute("create table Menu (Menu_Id int,Name varchar(150),Price varchar(100),Type varchar(200),Category varchar(200))")

# insert table(menu)
sql="INSERT INTO Menu (Menu_Id,Name,Price,Type,Category) VALUES (%s,%s,%s,%s,%s)"
val=[(1,"Vegetable Pakora","3.00","Veg","Starters"),(2,"Vegetable Samosa","3.00","Veg","Starters"),
(3,"Onion Bhaji ","3.00","Veg","Starters"),(4,"Potato and Mushroom Chaat","3.00","Veg","Starters"),
(5,"Mushroom Garlic Fry","3.00","Veg","Starters"),(6,"Chicken Tikka","4.00","Non-Veg","Starters"),
(7,"Tandoori Chicken","4.00","Non-Veg","Starters"),(8,"Chicken Garlic Fry","4.00","Non-Veg","Starters"),
(9,"Tandoori King Prawn","6.95","Non-Veg","SeaFood"),(10,"King Prawn Rosun","5.95","Non-Veg","SeaFood"),
(11,"Chi/Lam Sashlik Chi","9.95","Non-Veg","Tandoori Specials"),(12,"Tandoori Deluxe","12.95","Non-Veg","Tandoori Specials"),
(13,"Tandoori Chicken Main","9.95","Non-Veg","Tandoori Specials"),(14,"Chicken Tikka","7.95","Non-Veg","Tandoori Specials"),
(15,"Lamb Tikka","9.95","Non-Veg","Tandoori Specials")]
cursor.executemany(sql,val)
conne.commit()
print(cursor.rowcount,"record(s) affected")

# creating table Customer
cursor.execute("create table Customer (Customer_Id int,Fname varchar(155),Lname varchar(155),Contact varchar(200),Email_Id varchar(50))")

# insert table(customer)
sql="INSERT INTO Customer(Customer_Id,Fname,Lname,Contact, Email_Id) VALUES (%s,%s,%s,%s,%s)"
val=[(1,"Arpit","Sharma","938912","arpit.sharma@students.iiit.ac.in"),(2,"Yash","Shah","289374","yash.shah@students.iiit.ac.in"),
(3,"Darshit","Serna","234322","darshit.serna@students.iiit.ac.in"),(4,"Aditya","Sharma","778989","aditya.sharma@students.iiit.ac.in"),
(5,"Pallav","Shah","364932","pallav.shah@students.iiit.ac.in"),(6,"Rajat","Bharadwaj","734277","rajat.bharadwaj@students.iiit.ac.in")]
cursor.executemany(sql,val)
conne.commit()
print(cursor.rowcount,"record(s) affected")

# creating table Bill
cursor.execute("create table Bill (Order_Id int,Customer_Fname varchar(155),Customer_Lname varchar(155), Customer_id int,Contact varchar(200),Total_Amount int)")

# Delecting col
cursor.execute('ALTER TABLE Bill DROP COLUMN Contact')

# insert table(bill)
sql="INSERT INTO Bill ( Order_Id,Customer_Fname,Customer_Lname,Customer_id,Total_Amount) VALUES (%s,%s,%s,%s,%s)"
val=[(1,"Arpit","Sharma",1,100),(2,"Yash","Shah",2,200),(3,"Darshit","Serna",3,3500),
(4,"Rajat","Bharadwaj",4,4100),(5,"Pallav","Shah",5,5500)]
cursor.executemany(sql,val)
conne.commit()
print(cursor.rowcount,"record(s) affected")

# creating table DELIVERY_BOY
cursor.execute("create table DELIVERY_BOY (Delivery_Boy_Id int,Fname varchar(155),Lname varchar(155),Contact varchar(200),Address varchar(130),Salary varchar(30),Sex varchar(20),Bdate date, Join_Date date)")

# insert table
sql="INSERT INTO DELIVERY_BOY(Delivery_Boy_Id,Fname,Lname,Contact,Address,Salary,Sex,Bdate,Join_Date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
val=[(1,"Tarang","Goyal","133132","E-17 OBH , IIIT Hyderabad","10000","M","1993-02-21","2012-08-01"),
(2,"Saksham","Maheshwari","657569","E-17 OBH , IIIT Hyderabad","10000","M","1992-10-21","2012-08-01"),
(3,"Rajat","Agarwal","596509","E-16 OBH , IIIT Hyderabad","10000","M","1993-02-21","2012-08-01"),
(4,"Vidit","Bhaskar","344244","E-15 OBH , IIIT Hyderabad","10000","M","1993-10-22","2012-08-01")]
cursor.executemany(sql,val)
conne.commit()
print(cursor.rowcount,"record(s) affected")



# Show the tables
cursor.execute('Show tables;')
for i in cursor:
    print(i)

# Joining table
sql =  "SELECT \
  OWNER.Fname AS user, \
  USER.User_id AS id \
  FROM USER \
  INNER JOIN OWNER ON USER.Lname = OWNER.Lname"
cursor.execute(sql)
# cursor.execute('SELECT * FROM OWNER')
for i in cursor:
    print(i)