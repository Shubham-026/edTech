import psycopg2
import os

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="first",
    user="postgres",
    password="123456"
)
# Create a cursor
cur = conn.cursor()



while True:
    os.system("cls")
    print("---------Data Entry wizard----------")
    name = input("Name: ")
    clss = (input("Class: "))
    sec = input("Section: ")
    roll = (input("Roll No: "))
    mob = input("Mobile: ")
    father = input("Father's Name: ")
    mother = input("Mother's Name: ")
    addr = input("Address: ")
    bgr = input("Blood Type: ")

    cur.execute(" insert into students (name, cls,sec, roll, mob,father,mother,address,bgroup) values('"+name+"',"+clss+",'"+sec+"',"+roll+",'"+mob+"','"+father+"','"+mother+"','"+addr+"','"+bgr+"');")
    conn.commit()
    print("Data entered successfully------")
    input("use ctrl+c to exit")
    input("---press enter to proceed---")


# Cleanup
cur.close()
conn.close()
