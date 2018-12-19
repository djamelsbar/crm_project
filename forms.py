from wtforms import SubmitField, StringField, PasswordField
from wtforms import validators
from flask_wtf import FlaskForm


class UserForm(FlaskForm):
    username = StringField("username", [validators.DataRequired("Please enter username.")])
    password = PasswordField("password", [validators.DataRequired("Repeat Password")])
    submit = SubmitField("Submit")

    def validate(self):
        from model import User
        if not super(UserForm,self).validate():
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False
        if user.password == self.password.data :
            return True
        else :
            return False


