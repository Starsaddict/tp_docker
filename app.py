import os
from flask import Flask
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

app = Flask(__name__)

def mongo_client():
	uri = os.environ.get("MONGO_URI","mongodb://mongo:27017")
	return MongoClient(uri,serverSelectionTimeoutMS=3000)

@app.get("/")
def index():
	return "Flask is running"

@app.get("/healthz")
def healthz():
	try:
		client = mongo_client()
		client.admin.command("ping")
		return "MongoDB:OK"
	except ServerSelectionTimeoutError as e:
		return f"MongoDB:ERROR:{e}",500
	except Exception as e:
		return f"MongoDB:ERROR:{e}",500

@app.get("/insert")
def insert():
	client = mongo_client()
	db = client["tp_docker"]
	col = db["test"]
	res = col.insert_one({"msg":"hello from flask"})
	return f"Inserted:{res.inserted_id}"

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000,debug=False)