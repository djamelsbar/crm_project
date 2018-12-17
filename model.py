import enum

from app import db
from datetime import datetime


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	login = db.Column(db.String)
	password = db.Column(db.String)


class Status_type(enum.Enum):
	visit = "visit realized"
	purchase_sponsor = "purchase made at the promoter"
	purchase_other = "purchase made elsewhere"
	contact = "to recontact"


# class Status(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	status_type = db.Column(db.Enum(Status_type))


procpect_project = db.Table('procpect_project',
                                db.Column('procpect_id', db.Integer, db.ForeignKey('procpect.id'), primary_key=True),
                                db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True)
								,db.Column('status_type' , db.Enum(Status_type))

)


class Project(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String,nullable=False)
	description = db.Column(db.String, nullable=False)
	wilaya = db.Column(db.String)
	city = db.Column(db.String)

# class Status(db.Model) :
# 	id = db.Column(db.Integer, primary_key=True)
# 	description = db.Column(db.String, nullable=False)
# 	procpect_id = db.Column(db.Integer, db.ForeignKey('procpect.id'), nullable=False)
# 	procpect = db.relationship('Procpect', backref=db.backref('status', lazy=True))
# 	project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
# 	project = db.relationship('Project', backref=db.backref('status', lazy=True))


class Procpect(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String,nullable=False)
	last_name = db.Column(db.String)
	phone = db.Column(db.Integer, nullable=False)
	email = db.Column(db.String)
	date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	project = db.relationship("Project", secondary=procpect_project )





class Note(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String, nullable=False)
	date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	procpect_id = db.Column(db.Integer, db.ForeignKey('procpect.id'), nullable=False)
	procpect = db.relationship('Procpect', backref=db.backref('note', lazy=True))



