import mysql.connector
from mysql.connector import Error

localhost = 'localhost'
root = 'root'
password = ''

def connect():
   try:
       conn = mysql.connector.connect(host=localhost,
                                   user=root,
                                   passwd=password)
       
       mycursor = conn.cursor()

       if conn.is_connected():
           print('Connected to MySQL database')

   except Error as e:
       print(e)

def gett():
    