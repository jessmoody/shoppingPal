from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/inventory", methods=["POST"])
def inventory():
    return render_template('inventory.html')
 

@app.route("/lists/tasklist/tasks", methods=["POST"]) #Add task
def insert():
    return render_template('list.html')

@app.route("/lists/tasklist/tasks/task", methods=["PUT"]) #Update task
def update():
    return render_template('list.html')

@app.route("/lists/tasklist/tasks/task", methods=["DELETE"])
def delete():
    return render_template('list.html')