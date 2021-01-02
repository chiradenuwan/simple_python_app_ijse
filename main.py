from flask import Flask
from flask import render_template
from flask import request
from nic_parser.parser import Parser

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     print(f"{request.args}")
#     name = f"{request.args['name']}"
#     nic = f"{request.args['nic']}"
#
#     print(f"Name is {name}")
#     print(f"Nic is {nic}")
#
#     dob = Parser(f"{nic}").birth_date
#     gender = Parser(f"{nic}").gender
#     print(dob)
#     print(gender)
#
#     return f"Dob : {dob} , Gender : {gender.name}"

# @app.route("/test")
# def index():
#     return render_template("index.html", name="AAA")
#
class User:
    name: None
    nic: 0
    dob: None
    gender: None

    def __init__(self, name, nic):
        self.nic = nic
        self.name = name
        self.dob = Parser(f"{nic}").birth_date
        self.gender = Parser(f"{nic}").gender


name_list = []


@app.route("/insert_user", methods=["get", "post"])
def insert_user_data():
    print("insert_user_data_method")
    name = ""
    print(request.method)
    if request.method == "POST":
        print("inside post filter")
        print(request.args)
        print(request.form)
        name = request.form.get("user_name")
        nic = request.form.get("nic")
        # dob = request.form.get("do")
        # gender = request.form.get("nic")
        user = User(name=name, nic=nic)
        print(f"User : {user}")
        name_list.append(user)
        print(name)
        print(name_list)
    return render_template("insert_user_data.html", name_list=name_list);


# @app.route("/file")
# def hello_world():
#     index_file = open("templates/index.html", "r")
#     index_string = index_file.readlines()
#     temp_string = Template(''.join(index_string))
#     index_string = temp_string.substitute(name="Chiranjaya")
#     return f"{index_string}"
#

if __name__ == '__main__':
    app.run(port=3232)
