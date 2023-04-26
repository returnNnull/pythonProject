from flask import Flask, request, session

app = Flask(__name__)

data = {
    "name": "Igor",
    "age": 25
}

users = []

changes = [{
    "active": "false",
    "end": "142341asf",
    "id": 0,
    "start": "123241qwf"
},
    {
        "active": "false",
        "end": "142341asfqdq",
        "id": 1,
        "start": "123241qwf"
    },
    {
        "active": "false",
        "end": "142341asfqdq",
        "id": 2,
        "start": "123241qwfqwd"
    }]
changesIdCount = 0


@app.route("/user", methods=["POST"])
def login():
    user_login = request.form["login"]
    password = request.form["password"]
    role = request.form["role"]
    for u in users:
        if user_login == u["login"] and password == u["password"]:
            session["login"] = user_login
            session["role"] = role

    return "Not found", 404


app.route("/adminApi")


def admin_api():
    if session["role"] == "admin":
        print("actions....")
    return "Forbidden for you", 403


@app.route("/user", methods=["GET"])
def hello_world():
    return data, 201


@app.route("/change/add", methods=["GET"])
def change_add():
    global changesIdCount
    start = request.args.get("start")
    end = request.args.get("end")
    c = {
        "id": changesIdCount,
        "start": start,
        "end": end,
        "active": "false"
    }
    changes.append(c)
    changesIdCount += 1
    return c, 200


@app.route("/change/active", methods=["GET"])
def is_active():
    changeId = int(request.args.get("id"))
    for i in changes:
        print(i.get("id"))
        print(changeId)
        if i["id"] == changeId:
            i["active"] = "true"
            return i, 200
    return "Not found"


@app.route("/change")
def get_all():
    return changes, 200
