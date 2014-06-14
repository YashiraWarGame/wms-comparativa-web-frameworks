from __future__ import unicode_literals
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email

class IntroChallenge(Form):
    user = TextField("Usuario", validators=[DataRequired("Debe ingresar el nombre del usuario")])
    email = TextField("Correo", validators=[Email("Correo electr\u00f3nico con formato incorrecto")])
    answer = TextAreaField("Respuesta", validators=[DataRequired("Debe ingresar una respuesta")])
    submit = SubmitField("Enviar")
