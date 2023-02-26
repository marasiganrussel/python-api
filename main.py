from fastapi import FastAPI, Request, Response, HTTPException
import mysql.connector
from pydantic import BaseModel

host_local = 'sql12.freesqldatabase.com'
username = 'sql12601077'
password = 'Gk16DAWxii'

app = FastAPI()

@app.get("/get-all", status_code=200)
def get_all():
    try:
        obj_final = []
        conn = mysql.connector.connect(host=host_local,user=username,passwd=password)
        if conn.is_connected():
           sql_select_Query = "select * from sql12601077.person"
           mycursor = conn.cursor()
           mycursor.execute(sql_select_Query)
           result = mycursor.fetchall()
           for row in result:
                obj = {"id": row[0], "first_name": row[1],"last_name": row[2], "age": row[3]}
                obj_final.append(obj)
           return obj_final
           
    except:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.get("/get/{user_id}", status_code=200)
def get_user(user_id):
    try:
        obj_final = []
        conn = mysql.connector.connect(host=host_local,user=username,passwd=password)
        if conn.is_connected():
           sql_select_Query = "select * from sql12601077.person where id="+user_id
           mycursor = conn.cursor()
           mycursor.execute(sql_select_Query)
           result = mycursor.fetchall()
           for row in result:
                obj = {"id": row[0], "first_name": row[1],"last_name": row[2], "age": row[3]}
                obj_final.append(obj)
           return obj_final
           
    except:
        raise HTTPException(status_code=404, detail="Item not found")


@app.post("/upload/",status_code=201)
def upload_user(first_name: str, last_name: str, age: int):
    obj = {"first_name": first_name, "last_name": last_name, "age": age}
    try:
        conn = mysql.connector.connect(host=host_local,user=username,passwd=password)
        if conn.is_connected():
           sql_select_Query = "INSERT INTO sql12601077.person (first_name, last_name, age) VALUES (%s, %s, %s)"
           val = (first_name, last_name, age)
           mycursor = conn.cursor()
           mycursor.execute(sql_select_Query,val)
           conn.commit()
           return {"Uploaded Successfully"}
           
    except:
        raise HTTPException(status_code=400)

class addUser(BaseModel):
    first_name: str
    last_name: str
    age: int

@app.post("/upload/v2/",status_code=201)
def upload_user_v2(user: addUser):
    item_dict = user.dict()
    try:
        conn = mysql.connector.connect(host=host_local,user=username,passwd=password)
        if conn.is_connected():
           sql_select_Query = "INSERT INTO sql12601077.person (first_name, last_name, age) VALUES (%s, %s, %s)"
           val = (item_dict['first_name'], item_dict['last_name'], item_dict['age'])
           mycursor = conn.cursor()
           mycursor.execute(sql_select_Query,val)
           conn.commit()
           return {"Uploaded successfully"}
           
    except:
        raise HTTPException(status_code=400)
        


