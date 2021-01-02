from flask import Flask
from flask import render_template
from flask import request

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

@app.route("/insert_user")
def insert_user_data():
    name = ""
    if "user_name" in request.args:
        print(request.args["user_name"])
    return render_template("insert_user_data.html", name=name)


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
