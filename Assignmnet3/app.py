import pymongo
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import json
import os

load_dotenv()

app = Flask(__name__)

# ----- MongoDB Atlas Connection -----
MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.my_database
collection = db.users


# ----- API Route (Reads from file and returns JSON) -----
@app.route("/api", methods=["GET"])
def api():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ----- Home Page (Form) -----
@app.route("/", methods=["GET"])
def home():
    return render_template("form.html")


# ----- Form Submission -----
@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form["name"]
        email = request.form["email"]

        if not name or not email:
            return render_template("form.html", error="All fields are required!")

        # Insert into MongoDB
        collection.insert_one({
            "name": name,
            "email": email
        })

        return render_template("success.html")

    except Exception as e:
        return render_template("form.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)
