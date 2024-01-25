from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, DateField, TimeField, TextAreaField
from wtforms.validators import DataRequired, Length

from app.model import User, CapsuleMessage


class RegisterForm(FlaskForm):
    username = StringField('Nome de usuário',
                           validators=[
                               DataRequired(),
                               Length(2, User.MAX_LENGTH['username'])
                           ])
    first_name = StringField('Primeiro nome',
                             validators=[
                                 DataRequired(),
                                 Length(2, User.MAX_LENGTH['first_name'])
                             ])

    last_name = StringField('Sobrenome',
                            validators=[
                                DataRequired(),
                                Length(2, User.MAX_LENGTH['last_name'])
                            ])

    password = PasswordField('Senha',
                             validators=[
                                 DataRequired(),
                                 Length(6, User.MAX_LENGTH['password'])
                             ])

    email = EmailField('E-mail',
                       validators=[
                           DataRequired(),
                           Length(max=User.MAX_LENGTH['email'])
                       ])

    submit = SubmitField('Confirmar')


class LoginForm(FlaskForm):
    email = EmailField('E-mail',
                       validators=[
                           DataRequired(),
                           Length(max=User.MAX_LENGTH['email'])
                       ])

    password = PasswordField('Senha',
                             validators=[
                                 DataRequired(),
                                 Length(max=User.MAX_LENGTH['password'])
                             ])

    submit = SubmitField('Confirmar')


class CapsuleMessageForm(FlaskForm):
    title = StringField('Título',
                        validators=[
                            DataRequired(),
                            Length(max=CapsuleMessage.MAX_LENGTH['title'])
                        ])

    content = TextAreaField('Conteúdo',
                            validators=[
                                DataRequired()
                            ])

    date_can_open = DateField('O dia e o horário em que a mensagem será liberada',
                              validators=[
                                  DataRequired()
                              ])

    time_can_open = TimeField(
        validators=[
            DataRequired()
        ])

    submit = SubmitField('Confirmar')


class EditCapsuleMessageTitleForm(FlaskForm):
    title = StringField('Insira o novo título',
                        validators=[
                            DataRequired(),
                            Length(max=CapsuleMessage.MAX_LENGTH['title'])
                        ])
    submit = SubmitField('Confirmar')