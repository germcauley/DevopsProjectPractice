from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField('Username', [
        DataRequired()])
    # email = StringField('Song', [
    #     DataRequired()])
    body = TextField('Message', [
        DataRequired(),
        Length(min=4, message=('Your message is too short.'))])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')