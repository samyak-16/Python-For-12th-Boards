import mysql.connector as db


# Connecting to db
conn = db.connect(host="localhost",user="root",password="asdfghjkl")
print("Connected to database successfully")

#  Creating a Cursor : A cursor executes SQL queries.

cursor = conn.cursor()
#cursor.execute() - helps to execute mySql querries 



cursor.execute("USE startersql")
print("Switched db to startersqlr")




#! fetchone()

# cursor.execute("SELECT * FROM users")

# row1 = cursor.fetchone()
# row2 = cursor.fetchone()
# row3 = cursor.fetchone()

# print (row1)
# print (row2)
# print (row3)


#! fetchall()

# cursor.execute("SELECT * FROM users")
# users = cursor.fetchall()

# print (users)


#! fetchmany()

cursor.execute("SELECT * FROM users")
users = cursor.fetchmany(2)

print (users)

