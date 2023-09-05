import mysql.connector

# Create a connection to the database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="RafaelSouto17",
    database="pythonsql"
)
cur = con.cursor()


