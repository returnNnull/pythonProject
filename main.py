from flask import Flask, request, session

app = Flask(__name__)

data = {
    "name": "Igor",
    "age": 25
}

users = [{
    "id": 0,
    "login": "admin",
    "password": "1111"
}]

changes = [{
    "active": False,
    "end": "142341asf",
    "id": 0,
    "start": "123241qwf"
},
    {
        "active": False,
        "end": "142341asfqdq",
        "id": 1,
        "start": "123241qwf"
    },
    {
        "active": False,
        "end": "142341asfqdq",
        "id": 2,
        "start": "123241qwfqwd"
    }]
changesIdCount = 3
usersId = 1

employers = []
employersId = 0


@app.route("/api-tort/login")
def signin():
    user_login = request.form["login"]
    password = request.form["password"]
    for u in users:
        if u["login"] == user_login and u["password"] == password:
            return {
                "data": {
                    "user_token": "nbadodifhkwjdvl[mqbkefiyupl"
                }
            }

    return {
        "error": {
            "code": 403,
            "message": "Forbidden. There are open shifts!"
        }
    }


@app.route("/api-tort/user", methods=["GET"])
def get_all_employer():
    return {
               "data": employers
           }, 200



@app.route("/api-tort/work-shift/<id>/open")
def work_shift(id):
    for i in changes:
        if i["active"] == True:
            return {
                "error": {
                    "code": 403,
                    "message": "Forbidden. There are open shifts!"
                }
            }
        if i["id"] == int(id):
            i["active"] = True
            return {"data": i}, 200


#
# Для примера
#
@app.route("/change/add", methods=["GET"])
def change_add():
    global changesIdCount
    start = request.args.get("start")
    end = request.args.get("end")
    c = {
        "id": changesIdCount,
        "start": start,
        "end": end,
        "active": False
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
