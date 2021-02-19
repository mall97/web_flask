from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/racks")
def racks():
    return render_template("racks.html")

@app.route("/profile/<name>")
def profile(name):
    return render_template("first.html", name=name)
    
if __name__ == "__main__":
    app.run(debug=True)
