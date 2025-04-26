import mysql.connector
print("Hello World")
# Connect to server
mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="1234",
    database="meow")

# Get a cursor
cur = mydb.cursor()

# Execute a query
cur.execute("SELECT CURDATE()")

# Fetch one result
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

cur.execute("INSERT INTO meow(meow.mew,meow.meow) VALUES(2,'C')")
mydb.commit()
# Close connection
mydb.close()
