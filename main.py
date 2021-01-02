from flask import Flask
from flask import request
from nic_parser.parser import Parser

app = Flask(__name__)


@app.route("/")
def hello_world():
    print(f"{request.args}")
    name=f"{request.args['name']}"
    nic=f"{request.args['nic']}"

    print(f"Name is {name}")
    print(f"Nic is {nic}")

    dob = Parser(f"{nic}").birth_date
    gender = Parser(f"{nic}").gender
    print(dob)
    print(gender)

    return f"Dob : {dob} , Gender : {gender.name}"


if __name__ == '__main__':
    app.run(port=3232)
