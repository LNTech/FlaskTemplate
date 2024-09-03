from flask import Flask, render_template
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == '__main__':    
    app.run(debug=True)