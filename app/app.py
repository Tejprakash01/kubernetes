from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_uri = os.getenv(
    "MONGO_URI",
    "mongodb://mongo:27017/"
)

client = MongoClient(mongo_uri)

db = client["mydatabase"]
collection = db["users"]


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form.get("name")

        if name:
            collection.insert_one({
                "name": name
            })

        return redirect("/")

    users = list(collection.find())

    return render_template(
        "index.html",
        users=users
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )