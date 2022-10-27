import mariadb, os
from dotenv import load_dotenv

load_dotenv()
db_user = os.getenv("DBUSER")
db_password = os.getenv("DBPASSWORD")
db_host = os.getenv("DBHOST")
db_name = os.getenv("DBNAME")

print(db_host, db_user, db_name, db_password)

conn_params= {
    "user" : db_user,
    "password" : db_password,
    "host" : db_host,
    "database" : db_name
}

database = mariadb.connect(**conn_params)
cursor = database.cursor()

cursor.close()
database.close()
