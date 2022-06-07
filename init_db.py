# Import MySQL Connector Driver
import mysql.connector as mysql

# Load the credentials from the secured .env file
import os
from dotenv import load_dotenv
load_dotenv('credentials.env')

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST'] # must 'localhost' when running this script outside of Docker

# Connect to the database
db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
cursor.execute("drop table if exists Users;")

# Create a TStudents table (wrapping it in a try-except is good practice)
try:
  cursor.execute("""
    CREATE TABLE Users (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      first_name  VARCHAR(30) NOT NULL,
      last_name   VARCHAR(30) NOT NULL,
      email       VARCHAR(50) NOT NULL,
      user_role   VARCHAR(50) NOT NULL,
      password    VARCHAR(20) NOT NULL,
      created_at  TIMESTAMP
    );
  """)
except:
  print("Users table already exists. Not recreating it.")

# Insert Records
query = "insert into Users (first_name, last_name, email, user_role, password, created_at) values (%s, %s, %s, %s, %s, %s)"
values = [
  ('Rick','Gessner','rick@gessner.com', 'instructor', 'abc123', '2020-02-20 12:00:00'),
  ('Ramsin','Khoshabeh','ramsin@khoshabeh.com', 'instructor','abc123', '2020-02-20 12:00:00'),
  ('Al','Pisano','al@pisano.com', 'teacher assistant', 'abc123', '2020-02-20 12:00:00'),
  ('Truong','Nguyen','truong@nguyen.com', 'teacher assistant','abc123', '2020-02-20 12:00:00'),
  ('Nick','Muñoz','nmunoz@ucsd.edu', 'team member', 'abc123', '2020-02-20 12:00:00'),
  ('Raymond','Urbina','raurbina@ucsd.edu', 'team member','abc123', '2020-02-20 12:00:00'),
  ('Rusul','Al-Bulsultan','ralbusul@ucsd.edu', 'team member','abc123', '2020-02-20 12:00:00'),
  ('Marcin','Kierebinski','mrkiereb@ucsd.edu', 'team member','abc123', '2020-02-20 12:00:00'),
  ('Karen','Hernandez','klhernan@ucsd.edu', 'team member','abc123', '2020-02-20 12:00:00')
  ]
cursor.executemany(query, values)
db.commit()

# Selecting Records
cursor.execute("select * from Users;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]
db.close()