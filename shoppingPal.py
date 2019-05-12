from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("frontend.html")

    # first_item = request.form['item1']
    # return render_template("frontend.html", item1 = first_item)

# @app.route("/inventory", methods=["POST"])
# def inventory():
#     item = request.form['firstItem']
#     return render_template('submitPage.html', firstItem = item)

# @app.route("/lists/tasklist/tasks", methods=["POST"]) #Add task
# def insert():
#     return render_template('list.html')

# @app.route("/lists/tasklist/tasks/task", methods=["PUT"]) #Update task
# def update():
#     return render_template('list.html')

# @app.route("/lists/tasklist/tasks/task", methods=["DELETE"])
# def delete():
#     return render_template('list.html')


if __name__ == '__main__':
    app.run(debug=True)