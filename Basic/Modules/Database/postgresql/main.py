
import psycopg2
import getpass

'''
we are using a psycopg2 to connect to rds protgres database
intension.:
           perform 

'''


#working with Database
#Learn How to man, and perform some CRUD(CREATE,READ,UPDATE,DELETE)
#HOW DO DATA BE RESTORED IN A DATABASE
#RELATIONAL DATABASE.(RDBMS)
'''

connection = psycopg2.connect(
    user = "postgres",
    password = getpass("enter your password"),
    host = "kojitechs.c1hezcsltwdt.us-east-1.rds.amazonaws.com",
    port = "5432",
    database = "postgres"
  )
connection.close()
'''

with psycopg2.connect(user = "python", password = "admin",host = "localhost",port = "5432", database = "kojitechs") as connection:
    cursor = connection.cursor()
    print("Print postgres server infomation")
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")


with psycopg2.connect(user = "python", password = "admin",host = "localhost",port = "5432", database = "kojitechs") as connection:
    cursor = connection.cursor()

'''CREATE TABLE students
        (ID INT PRIMARY KEY    NOT NULL,
        STUT_NAME  TEXT NOT NULL ,
        Email   TEXT NOT NULL,
        Phone_Number   TEXT NOT NULL,
        STUT_ADD TEXT NOT NULL,
        STUT_APP TEXT NOT NULL,
        zip INT NOT NULL,
        Amount_paid REAL NOT NULL,
        PaidFull bool NOT NULL);'''
