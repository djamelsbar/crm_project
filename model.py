import enum

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship
from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)


class StatusType(enum.Enum):
    visit = "visit realized"
    purchase_sponsor = "purchase made at the promoter"
    purchase_other = "purchase made elsewhere"
    contact = "to recontact"


class ProspectProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    procpect_id = db.Column(db.Integer, db.ForeignKey('prospect.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    status = db.Column('status_type', db.Enum(StatusType))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    prospect = relationship('Prospect', back_populates='projects')
    project = relationship('Project', back_populates='prospects')

    __table_args__ = (db.UniqueConstraint('procpect_id','project_id',name='unique_constraint_prjctid_prcpctid'),)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    wilaya = db.Column(db.String)
    city = db.Column(db.String)
    prospects = relationship('ProspectProject', back_populates='project')
    def __repr__(self):
        return self.title


class Prospect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String, unique=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    projects = relationship('ProspectProject', back_populates='prospect')
    notes = db.relationship('Note', backref='prospect', lazy=True)

    def __repr__(self):
        return self.name


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    prospect_id = db.Column(db.Integer, db.ForeignKey('prospect.id'), nullable=False)


