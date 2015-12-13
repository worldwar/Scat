from flask import Flask, render_template, request, redirect, url_for
import hashlib

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def index():
    error = None
    source = request.args.get('source', '')
    if request.method == "GET":
        return render_template("login.html", error=error, source=source)
    elif request.method == "POST":
        if valid_login(request.form["username"], request.form["password"]):
            return redirect(url_for("index"))
        else:
            error = "wrong username/password combination"
            return render_template("login.html", error=error, source=source)
    else:
        return redirect(url_for("/"))
        
@app.route('/auth', methods=["POST"])
def auth():
    source=request.form["source"]
    print "source is " + source
    if valid_login(request.form["username"], request.form["password"]):
        return redirect(source, code=302)
    else:
        error = "wrong username/password combination"
        return render_template("login.html", error=error, source=source)

def valid_login(username, password):
    return username == "zhuran" and MD5_HEX(password) == "E10ADC3949BA59ABBE56E057F20F883E"

def MD5_HEX(source):
    print "haha"
    return hashlib.md5(source).hexdigest().upper()
if __name__ == "__main__":
    app.run(debug=True, port=5414)