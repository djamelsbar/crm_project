from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView, filters
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


class ProspectModelView(ModelView):
    inline_models = (Note,)
    column_filters = ('name', 'phone','email')
    form_excluded_columns = ['projects']


class NoteModelView(ModelView):
    form_excluded_columns = ['prospect']


class ProjectModelView(ModelView):
    form_excluded_columns = ['prospects']


class ProspectProjectModelView(ModelView):
    column_filters = ('status', 'prospect.name','project.title','date')


admin.add_view(ModelView(User, db.session))

admin.add_view(ProjectModelView(Project, db.session))

admin.add_view(ProspectModelView(Prospect, db.session))

admin.add_view(NoteModelView(Note, db.session))

admin.add_view(ProspectProjectModelView(ProspectProject, db.session))

