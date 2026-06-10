from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed  # ← добавить эту строку
from wtforms import StringField, PasswordField, SelectField, TextAreaField, DateField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from datetime import date

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    full_name = StringField('ФИО', validators=[DataRequired(), Length(min=2, max=200)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Телефон', validators=[DataRequired(), Length(min=10, max=20)])
    group_id = SelectField('Группа', coerce=int, validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])

class ForgotPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Новый пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])

class ProfileForm(FlaskForm):
    full_name = StringField('ФИО', validators=[DataRequired(), Length(min=2, max=200)])
    phone = StringField('Телефон', validators=[DataRequired(), Length(min=10, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    current_password = PasswordField('Текущий пароль')
    new_password = PasswordField('Новый пароль', validators=[Length(min=6)])
    confirm_new_password = PasswordField('Подтвердите новый пароль', validators=[EqualTo('new_password')])

class EventForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(), Length(max=200)])
    event_date = DateField('Дата', validators=[DataRequired()])
    event_time = StringField('Время', validators=[DataRequired(), Length(max=10)])
    place = StringField('Место', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Описание')
    image = FileField('Изображение мероприятия', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Только изображения!')])

class JournalSelectForm(FlaskForm):
    group_id = SelectField('Группа', coerce=int, validators=[DataRequired()])
    subject_id = SelectField('Дисциплина', coerce=int, validators=[DataRequired()])
    lesson_date = DateField('Дата занятия', validators=[DataRequired()], default=date.today)

class SubjectForm(FlaskForm):
    name = StringField('Название дисциплины', validators=[DataRequired(), Length(max=200)])
    teacher_id = SelectField('Преподаватель', coerce=int, validators=[DataRequired()])

class GroupForm(FlaskForm):
    name = StringField('Название группы', validators=[DataRequired(), Length(max=100)])

class TeacherForm(FlaskForm):
    full_name = StringField('ФИО', validators=[DataRequired(), Length(max=200)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])

class CertificateRequestForm(FlaskForm):
    certificate_type = SelectField('Тип справки', choices=[
        ('study', 'Справка об обучении'),
        ('payment', 'Справка об оплате обучения'),
        ('military', 'Справка по форме Приложения №4 (для военкомата)')
    ], validators=[DataRequired()])