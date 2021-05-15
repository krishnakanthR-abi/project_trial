import mysql.connector

def add_user(name, number):

    mydb = mysql.connector.connect(host="localhost", user="root", password="krish2222na", database="practice")

    cursor = mydb.cursor()

    command = "insert into user_details (name, number) values(%s,%s)"
    data = (name, number)

    cursor.execute(command, data)

    mydb.commit()

    mydb.close()

    return "user added to db"