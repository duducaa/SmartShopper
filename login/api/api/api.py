import sys, os

root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(root)
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data/models')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data')))

from flask import Flask, request, Blueprint
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://smartshopper-interface:3000/*"}})

from users import Users

@app.route("/", methods=["POST"])
@cross_origin()
def login():
    if request.method == "POST":
        try:
            data = request.get_json()[0]
            key = ""
            
            user = Users.select().where(Users.email == data["email"]).first()
            
            if user is None:
                return json.dumps({"Message": "Wrong email or password"}), 401
            
            if user.password == data["password"]:
                key = "key"
                
                result = {"key": key, "user_id": user.id}
                return json.dumps(result), 200
            else:
                return json.dumps({"Message": "Wrong email or password"}), 401
            
        except Exception as err:
            print(err)
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only POST allowed", 405

if __name__ == "__main__":
    app.run(host="smartshopper-login", debug=True)
