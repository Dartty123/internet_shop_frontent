from flask_wtf import FlaskForm
import wtforms


class SignUp(FlaskForm):
    first_name = wtforms.StringField("Ім'я")
    last_name = wtforms.StringField("Призвіще")
    email = wtforms.EmailField("Електрона пошта", validators=[wtforms.validators.Email(), wtforms.validators.DataRequired()])
    password = wtforms.PasswordField("Пароль"), validators=[wtforms.validators.length(6)]