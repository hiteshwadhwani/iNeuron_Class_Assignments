from flask import Flask, request, jsonify, redirect, url_for

# 1 . Write a program to insert a record in sql table via api
# 2.  Write a program to update a record via api
# 3 . Write a program to delete a record via api
# 4 . Write a program to fetch a record via api
# 5 . All the above questions you have to answer for mongo db as well .

import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="indore11"

)
app = Flask(__name__)
mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE test_api')
mycursor.execute('USE test_api')
mycursor.execute("""create table if not exists test_table (
	                    name varchar(20),
	                    age int(20)
                        )""")


@app.route("/test", methods=['GET'])
def test():
    return "test_function"


@app.route('/insert', methods=['POST'])
def insert_data():
    if request.method == 'POST':
        name = request.json['name']
        age = request.json['age']
        sql = "INSERT INTO test_table values (%s,%s)"
        val = (name, age)
        mycursor.execute(sql, val)
        mydb.commit()
        return "record inserted"


@app.route('/update', methods=['POST'])
def update_name():
    if request.method == 'POST':
        oldName = request.json['oldName']
        newName = request.json['newName']
        sql = "UPDATE test_table SET name = %s WHERE name = %s"
        val = (newName, oldName)
        mycursor.execute(sql, val)
        mydb.commit()
        return "record updated"


@app.route('/delete', methods=['POST'])
def delete_record():
    if request.method == 'POST':
        name = request.json['name']
        sql = "DELETE FROM test_table WHERE name = %s"
        mycursor.execute(sql, name)
        mydb.commit()
        return "record deleted"


@app.route('/fetch', methods=['GET'])
def fetch_all_record():
    mycursor.execute("SELECT * from test_table")
    records = mycursor.fetchall()
    return jsonify(str(records))


if __name__ == '__main__':
    app.run()
