import sqlite3
import json
from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import Response

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Our_data.db'
print ('Database opened')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/home")
def hello_world():
    allUsers = User.query.all()
    Users = [i.serialize() for i in allUsers] 
    return jsonify(
        Users
    )

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    divisao = db.Column(db.String(128))
    stars = db.Column(db.Integer)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'divisao': self.divisao,
            'stars': self.stars,
        }



class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }



User.query.all()
