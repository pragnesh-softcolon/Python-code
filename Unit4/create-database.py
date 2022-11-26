# Write a program to create a database named “Sample_DB” in MySQL(). [First ensure connection is made or not and then check if the database Sample_DB already exists or not, if yes then print appropriate message]

import mysql.connector as mydb
db_name=input("enter DatabaseName: ")
# try:
mydb=mydb.connect(host="localhost",user="root",password="")
# except:
print("there is a problem in connecting mysql…")
try:
    cursor=mydb.cursor()
    cursor.execute("CREATE DATABASE %s"%db_name)
    cursor.close()
except:
    print("database %s already exists,please try to create database with othre name"%db_name)
else:
    print("Databas %s sucessfully created"%db_name)