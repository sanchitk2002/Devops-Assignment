from flask import Flask, render_template

BACKEND_URL = 'http://0.0.0.0:90'

app = Flask(__name__)

# ----- Home Page (Form) -----
@app.route("/", methods=["GET"])
def home():
    return render_template("form.html")



if __name__ == "__main__":
        app.run(host="0.0.0.0", port=50, debug=True)