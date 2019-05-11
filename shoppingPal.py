from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/inventory", methods=["POST"])
def inventory():
    return render_template('inventory.html')

@app.route("/list", methods=["POST"])
def shoppingList():
    return render_template('list.html')