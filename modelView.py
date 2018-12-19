from flask import url_for,redirect,request,session
from flask_admin.contrib.sqla import ModelView, filters

from model import *


class AdminView(ModelView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.static_folder = 'static'

    def is_accessible(self):
        return session.get('user') == 'Administrator'

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('home', next=request.url))


class ProspectModelView(ModelView):
    # adm =AdminView(Project, db.session)
    inline_models = (Note,)
    column_filters = ('name', 'phone','email')
    form_excluded_columns = ['projects']


class NoteModelView(ModelView):
    form_excluded_columns = ['prospect']


class ProjectModelView(AdminView):
    form_excluded_columns = ['prospects']


class ProspectProjectModelView(ModelView):
    column_filters = ('status', 'prospect.name','project.title','date')

