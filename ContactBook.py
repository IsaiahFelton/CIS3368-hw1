from ContactData import contactData
import datetime
from datetime import date
import mysql.connector
from mysql.connector import Error

# Creating connection to with AWS(code was referenced from Professor Otto in his in class example)
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )  
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# Executing the info from the query as a string once the connection is established with AWS(code was referenced from Professor Otto in his in class example)
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
# Executing query to fetch all the info from the called table once the connection is established with AWS(code was referenced from Professor Otto in his in class example)
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# Personal connection
connection = create_connection("cis3368v5.cwb2r4cwyvi9.us-east-2.rds.amazonaws.com", "admin", "Wolfpack69!", "cis3368db")


# Selecting all the info from my contacts table in MySql
select_contacts = "SELECT * FROM contacts"
contacts = execute_read_query(connection, select_contacts)



# Menu interface 
print(" Menu \n","a - Add contact \n","d - Remove contact \n","u - Update contact details \n","b - Output all contacts in alphebetical order\n","c - Output all contacts by creation date \n", "o - output all contacts \n","q - Quit ")
value = input("choose and option: \n")

# Asking user for contact details and giving the user the creation dat of the newly added contact
if value == "a":
    contactDetails = input("Enter First Name: \n")
    creationDate = date.today()
    
    print("You created",contactDetails,"on",creationDate)
    addContact = "INSERT INTO contacts (contactDetails, creationDate) VALUES ('%s','%s')" % (contactDetails, creationDate)
    execute_query(connection, addContact)




# Updating a user in the contacts table in MySql
if value == "u":
    for contact in contacts:
        print(contact)
    updateDetails = input("Enter updated first name: ")
    updatedDetails = input("Enter id for the update: ")
    updateDetails_query = """   
    UPDATE contacts
    SET contactDetails = '%s'
    WHERE id = %s """ % (updateDetails, updatedDetails)   
    execute_query(connection, updateDetails_query)                            
    
     


# Deleting a user in the contacts table in MySql
if value == "d":   
    for contact in contacts:
        print(contact)
    deleteDetails = input("Enter id of the person thats to be deleted: ")
    deleteUser = "DELETE FROM contacts WHERE id = '%s'" % (deleteDetails)
    execute_query(connection, deleteUser)


# Printing all contacts in the contacts table to the console
if value == "o":
    for contact in contacts:
        print(contact)

# Outputting all contacts in alphbetical order
if value =="b":
    select_contactDetails = "SELECT * FROM contacts ORDER BY contactDetails" #used ORDER BY to sort the names in my contactDetails column
    contactDetails = execute_read_query(connection, select_contactDetails)
    for DetailsOfContact in contactDetails:
        print(DetailsOfContact[1])

