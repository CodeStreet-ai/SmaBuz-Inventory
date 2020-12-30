import os
from flask import Flask, render_template

port = int(os.environ.get('PORT', 5000))

app= Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tables")
def tables():
    return render_template("tables.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
