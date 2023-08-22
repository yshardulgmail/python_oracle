import flask
import json
import traceback

# from save import save

  
app = flask.Flask(__name__)

  
@app.route("/users", methods=["POST"])
def users():
    posted_data = flask.request.json
    if "name" not in  posted_data or "age" not in posted_data:
       return flask.jsonify(message = {"message": "Either name or age is missing"}, status=400), 400
    if len(posted_data["name"]) > 32:
       return flask.jsonify(message = {"message": "Name should be less than 32 chars"}, status=400), 400
    if not posted_data["age"].isdigit():
       return flask.jsonify(message = {"message": "Age should be number"}, status=400), 400
    if int(posted_data["age"]) < 16:
       return flask.jsonify(message = {"message": "Age should be number"}, status=400), 400
    
    return flask.jsonify(message = {"message": save(posted_data)}, status=201), 201

  
if __name__ == "__main__":
  app.run()