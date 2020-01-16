#!/usr/bin/python
 
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="bob",
  passwd="password",
  database="userdb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE MyUsers(name VARCHAR(30) NOT NULL PRIMARY KEY, favcolor VARCHAR(30) NOT NULL, pets VARCHAR(30) NOT NULL)")