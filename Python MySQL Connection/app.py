import mysql.connector

try:
    dbcon = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
    print("Success")
    
except mysql.connector.Error as err:
    print(f"Error: {err}")
    # Handle the error or exit the program as needed

finally:
    # Close the database connection in any case
    if 'dbcon' in locals() and dbcon.is_connected():
        dbcon.close()
