import mysql.connector
from mysql.connector import Error

# Replace with your connection details
try:
  mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Kalashnikov007#",
  )

  if mydb.is_connected():
        print("Connected to MySQL server successfully!")

  # Execute SQL statements using the execute() method on the cursor
  mycursor = mydb.cursor()

  # Create a Database named `alx_book_store` (if it doesn't exist)
  mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
  print("Database 'alx_book_store' created successfully!")
  # Close connection to the databasse  
  mycursor.close()
  mydb.close()

except Error as err:
    print("Failed to connect to MySQL:", err)
