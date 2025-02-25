from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask App!"

@app.route("/hello")
def hello():
    return "Hello, World! let's began"

@app.route("/home")
def home():
    return "This is home page to began"

if __name__ == '__main__':
    app.run(debug=True)

# import controller.user_controller as user_controller
# import controller.product_controller as product_controller

# from controller import user_controller, product_controller
from controller import *