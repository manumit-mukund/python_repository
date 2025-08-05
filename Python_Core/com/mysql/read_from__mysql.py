import mysql.connector

# Database connection details
DB_CONFIG = {
    'host': 'localhost',  # Or the IP address/hostname of your MySQL server
    'user': 'root',
    'password': 'root',
    'database': 'myhibernate'
}

try:
    # Establish the connection
    mydb = mysql.connector.connect(**DB_CONFIG)

    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # Execute a sample query (e.g., selecting data from a table)
    mycursor.execute("SELECT * FROM customers")

    # Fetch all the results
    results = mycursor.fetchall()

    # Print the results
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection to release resources
    if 'mycursor' in locals() and mycursor:
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
    print("MySQL connection closed.")

