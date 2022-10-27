import mariadb, os
from dotenv import load_dotenv
from sys import exit
from os import getenv

load_dotenv()
db_user = getenv("DBUSER")
db_password = getenv("DBPASSWORD")
db_host = getenv("DBHOST")
db_name = getenv("DBNAME")

conn_params = {
    "user": db_user,
    "password": db_password,
    "host": db_host,
    "database": db_name,
}
try:
    database = mariadb.connect(**conn_params)
    cursor = database.cursor()
except SyntaxError as e:
    print("ERROR COULD NOT CONNECT TO DATABASE... ERROR: {0}".format(e))
    exit()


def dbrun(cmd, arg):
    print(f"Executing: {cmd}, {arg}")
    cursor.execute(cmd, arg)
    row = cursor.fetchall()
    return row


tag = input("Discord tag: ")
id = dbrun("SELECT id FROM people WHERE tag=?", (tag,))[0][0]
print(id)
rem = dbrun("SELECT homeworkid FROM todo WHERE personid=?", (id,))
print(rem)
for i in rem:
    print(i[0])
    hm = dbrun("SELECT name FROM homework WHERE id=?", (i[0],))
    print(hm)

cursor.close()
database.close()
