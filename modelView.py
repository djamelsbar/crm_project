import wtf as wtf
from flask import url_for,redirect,request,session
from flask_admin.contrib.sqla import ModelView
from model import *



class AdminView(ModelView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.static_folder = 'static'

    def is_accessible(self):
        return session.get('user') == 'admin'

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('home', next=request.url))


class ProspectModelView(ModelView):
    inline_models = (Note, ProspectProject)
    column_filters = ('name', 'phone','email','date')
    column_searchable_list = ('name', 'phone','email','last_name')
    form_excluded_columns = ['projects']


class NoteModelView(ModelView):
    form_excluded_columns = ['prospect']
    can_create = False
    can_edit = False
    can_delete = False
    column_filters = ('description', 'date', 'prospect.id')
    column_searchable_list = ('description', 'prospect.id')


class ProjectModelView(AdminView):
    form_excluded_columns = ['prospects']


class ProspectProjectModelView(ModelView):
    column_filters = ('status', 'prospect.name','project.title','date')
    can_create = False
    can_edit = False
    can_delete = False
    column_searchable_list = ('status', 'prospect.name', 'project.title')


