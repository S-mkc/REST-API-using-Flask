from app import app
from model.user_model import user_model
from flask import request

obj = user_model()
@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/adduser", methods=['POST'])
def user_add_controller():
    # print(request.form)
    return obj.user_add_model(request.form)

@app.route("/user/modifyuser", methods = ['PUT'])
def user_modify_controller():
    return obj.user_modify_model(request.form)

@app.route("/user/deleteuser/<id>", methods = ["Delete"])
def user_delete_controller(id):
    return obj.user_delete_model(id)

@app.route("/user/modifyuser_patch", methods = ['PATCH'])
def user_patch_controller():
    return obj.user_patch_model(request.form)

@app.route("/user/getall/limit/<limit>/page/<page>", methods = ["GET"])
def user_pagination_controller(limit, page):
    return obj.user_pagination_model(limit, page)