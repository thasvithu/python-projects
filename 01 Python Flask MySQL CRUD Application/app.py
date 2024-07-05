import mysql.connector as connection
from mysql.connector import Error

class StudentManagementSystem:
    def __init__(self):
        self.cur = None
        self.stdb = None

    def create_account(self):
        """"
        Creates a new user account.

        This method allows a new user to create an account by providing necessary details.
        It typically involves gathering user input such as name, index_number, mobile_no, age
        and store these details in a database.

        Raises:
            ValueError: If the input does not meet the required criteria.
            DatabaseError: If there is an issue with storing the details in the database.

        Note:
            This method does not return any value. It provides feedback through print statements.,
        """
        print("--- Create Account ---")

        try:
            # get user inputs
            name = input("Enter your name : ")
            index_number = int(input("Enter your index number : "))
            mobile_no = int(input("Enter your mobile number : "))
            age = int(input("Enter your age : "))

            #create mysql connection
            self.stdb = connection.connect(host = "localhost", user = "root", password = "mysql", database = "python_crud")
            self.cur = self.stdb.cursor() # create connection object

            query = """
                    INSERT INTO student (name, index_number, mobile_no, age)
                    VALUES(%s, %s, %s, %s)
                    """

            data = (name, index_number, mobile_no, age)

            self.cur.execute(query, data)
            self.stdb.commit()

            print("Account created successfully!")

        except ValueError as ve:
            print(f"Input error : {ve}")
        except Error as db_error:
            print(f"Database error : {db_error}")
        except Exception as e:
            print(f"An error occurred : {e}")
        finally:
            if self.cur:
                self.cur.close()
            if self.stdb and self.stdb.is_connected():
                self.stdb.close()


    def account_info(self):
        print("Account details")

    def modify_account(self):
        print("Modify the user details")

    def delete_account(self):
        print("Delete Account")

    def welcome(self):
        print("\n--- Welcome to Student Management System ---")
        print("1. Login the account")
        print("2. Create new account")
        choice = int(input("Select the option : "))

        if choice == 1:
            self.account_info()
        else:
            self.create_account()


system = StudentManagementSystem()
system.welcome()