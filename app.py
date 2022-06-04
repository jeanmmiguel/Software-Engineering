import sqlite3
import json
from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime

from flask import Response

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cm_agenda.db'
print ('Database opened')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
         
        }



class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    duration_time = db.Column(db.DateTime(timezone=True))
    price = db.Column(db.Float)
    status = db.Column(db.Boolean)
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'duration_time': self.duration_time,
            'price': self.price,
            'status': self.status,
            
        }


class Prefeitura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
        
    def serialize(self):
        return {
            'id': self.id,
         
        }




@app.route("/Home")
def Mostrar_Eventos():
    allEvents = Event.query.all()
    Events = [i.serialize() for i in allEvents] 
    return jsonify(
        Events

    )


@app.route("/Admin")
def Adm_Eventos():
    Administrador = Prefeitura.query.all()
    Administradores = [i.serialize() for i in Administrador] 
    return jsonify(
        Administradores
        
    )


@app.route("/Usuarios")
def hello_world():
    allUsers = User.query.all()
    Users = [i.serialize() for i in allUsers] 
    return jsonify(
        Users
    )

User.query.all()
Event.query.all()
Prefeitura.query.all()