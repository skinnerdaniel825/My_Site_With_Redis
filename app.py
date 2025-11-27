from flask import Flask, render_template, request
import os
import redis

app = Flask(__name__)

REDIS_URL = os.environ.get("REDIS_URL")
END_STATE_TEMP = "end.flag"
END_STATE_PERM = "end_state"

try:
    r = redis.from_url(REDIS_URL)
    r.ping()
except Exception as e:
    r = None
    print("ERROR:", e)

def solved():
    if r is None:
        return os.path.exists(END_STATE_TEMP)
    return r.get(END_STATE_PERM) == b"true"

@app.route("/")
def display_to_user():
    if solved():
        return render_template("end.html")
    else:
        return render_template("index.html")
    
@app.route("/check_password", methods=["POST"])
def check_password():
    password = request.form.get("password")
    if password == "password": #I think it was like, o0c7 'r smthn IDK
        return render_template("authorized.html")
    else:
        return render_template("index.html", error="ACCESS DENIED")

@app.route("/unlock", methods=["POST"])
def unlock():
    if r is None:
        with open(END_STATE_TEMP, "w") as endFile:
            endFile.write("true")
    else:
        r.set(END_STATE_PERM, "true")
    return render_template("end.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)