import re
from django import forms

from apps.orm.models_orm import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=64, required=True)
    username = forms.CharField(max_length=16, required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput, required=True)
    repeat_password = forms.CharField(max_length=32, widget=forms.PasswordInput, required=True)
    user_role = forms.ChoiceField(choices=User.ROLES)

    def clean(self):
        cleaned_data = super().clean()
        password_pattern = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'

        # if not re.match(password_pattern, cleaned_data.get('password')):
        #     self.add_error('password', 'Password error')
        # elif cleaned_data.get('password') != cleaned_data.get('repeat_password'):
        #     self.add_error('repeat_password', 'Passwords not equals!')
