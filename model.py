from app import db
from datetime import datetime


remarque_procpect = db.Table('remarque_procpect',
                                db.Column('procpect_id', db.Integer, db.ForeignKey('procpect.id'), primary_key=True),
                                db.Column('remarque_id', db.Integer, db.ForeignKey('remarque.id'), primary_key=True)
                                )



class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	login = db.Column(db.String)
	password = db.Column(db.String)


class Project(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	titre = db.Column(db.String)
	description = db.Column(db.String, nullable=False)
	wilaya = db.Column(db.String)
	ville = db.Column(db.String)
	visite_realisee = db.Column(db.String)
	achat_effectuee_chez_le_promoteur = db.Column(db.String)
	achat_efectue_ailleurs = db.Column(db.String)


class Procpect(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nom = db.Column(db.String)
	prenom = db.Column(db.String)
	tel = db.Column(db.Integer, nullable=False)
	email = db.Column(db.String)
	date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	status =db.Column(db.String)
	remarque = db.relationship("Remarque", secondary=remarque_procpect)


class Remarque(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String, nullable=False)
	date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
