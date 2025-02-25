import mysql.connector
from mysql.connector import Error
import json
from flask import make_response
class user_model:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='127.0.0.1', user='mukesh', password='Raindrop@009', database='flask_tuorial')
            self.conn.autocommit = True
            self.cur = self.conn.cursor(dictionary=True)
            # self.cursor = self.conn.cursor()
            print("Connection established")
        except mysql.connector.Error as e:
            print(e)
    def user_getall_model(self):
        # Query execution code
        self.cur.execute("SELECT * FROM user")
        result = self.cur.fetchall()
        if len(result) > 0:
            # return json.dumps(result)
            # return make_response({"payload": result}, 200)
            response = make_response({"payload": result}, 200)
            # response.headers['Content-Type'] = 'application/json'
            response.headers['Access-Control-Allow-Origin'] = '*'
            return response
        else:
            return make_response({"message": "No records found"}, 204)
        # return json.dumps(result)
        # return "This is signup page called from user model"
    
    # Add user to database/ post request  
    def user_add_model(self, data):
        # print(requet.form)
        # self.cur.execute(f"INSERT INTO user (name, email, phone, role, password) VALUES (%s, %s, %s, %s, %s)", (data["name"], data["email"], data["phone"],data["role"], data["password"]))
        self.cur.execute(f"INSERT INTO user (name, email, phone, role, password) VALUES ('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        # self.conn.commit()
        # print(data["email"])
        return make_response({"message": "User added successfully"}, 201)
        
    # Put request to modify user
    
    def user_modify_model(self, data):
        self.cur.execute(f"UPDATE user SET name = '{data['name']}', email = '{data['email']}', phone = '{data['phone']}', role = '{data['role']}', password = '{data['password']}' WHERE id = {data['id']}")
        return make_response({"message": "User modified successfully"}, 201)
    
    # Delete user from database / delete request
    def user_delete_model(self, id):
        self.cur.execute(f"DELETE FROM user WHERE id = {id}")
        return make_response({"message": "User deleted successfully"}, 200)
    
    # Patch method to modify user data, to only update the required fields
    def user_patch_model(self, data):
        # self.cur.execute(f"UPDATE user SET name = '{data['name']}', email = '{data['email']}', role = '{data['role']}', phone = '{data['phone']}', WHERE id = {data['id']}")
        # return make_response({"message": "User modified successfully"}, 201)
        qry = "UPDATE user SET "
        for key, value in data.items():
            qry += f"{key} = '{value}', "
        print(qry)
        qry = qry[:-2]
        qry += f" WHERE id = {data['id']}"
        self.cur.execute(qry)
        return make_response({"message": "User updated successfully"}, 201)
        # return qry

    # Pagination method
    def user_pagination_model(self, limit, page):
        offset = (int(page) - 1) * int(limit)
        self.cur.execute(f"SELECT * FROM user LIMIT {limit} OFFSET {offset}")
        result = self.cur.fetchall()
        if(len(result) > 0):
            return make_response({"payload": result, "page_number": int(page), "limit": int(limit)}, 200)
        else:
            return make_response({"message": "No records found"}, 204)
        # return result