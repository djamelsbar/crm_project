from flask import Flask, session, redirect, url_for, request, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView, filters
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os


from forms import UserForm


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'admin.db')

app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app)
from modelView import *


@app.route('/', methods=['GET', 'POST'])
def login():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            us = User.query.filter_by(username=form.username.data).first()
            session['user'] = us.username
            return redirect(url_for('admin.index'))
    return render_template('login.html', form=form)


admin.add_view(AdminView(User, db.session))

admin.add_view(ProjectModelView(Project, db.session))

admin.add_view(ProspectModelView(Prospect, db.session))

admin.add_view(NoteModelView(Note, db.session))

admin.add_view(ProspectProjectModelView(ProspectProject, db.session))

