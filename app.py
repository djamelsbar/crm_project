
from flask import Flask, render_template, request, flash,url_for,redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os



basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'admin.db')

app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)
admin = Admin(app)

from model import *


class UserView(ModelView):
    #can_delete = False
    pass


admin.add_view(UserView(User, db.session))

admin.add_view(ModelView(Project, db.session))

admin.add_view(ModelView(Procpect, db.session))

admin.add_view(ModelView(Note, db.session))

admin.add_view(ModelView(procpect_project, db.session))

