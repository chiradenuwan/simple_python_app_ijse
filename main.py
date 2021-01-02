from flask import Flask
from flask import request
from string import Template
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


@app.route("/file")
def hello_world():
    index_file = open("template/index.html", "r")
    index_string = index_file.readlines()
    temp_string = Template(''.join(index_string))
    index_string = temp_string.substitute(name="Chiranjaya")
    return f"{index_string}"




if __name__ == '__main__':
    app.run(port=3232)
