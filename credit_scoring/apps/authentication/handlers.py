from django.http.request import HttpRequest
from django.contrib.auth import login, logout


from django.contrib.auth.hashers import make_password, check_password


from apps.authentication.forms import LoginForm, RegisterForm
from apps.orm.models_orm import User
from django.conf import settings


class AuthenticationHandler:

    @staticmethod
    def login_handler(request: HttpRequest, login_form: LoginForm) -> bool:
        request_username = login_form.cleaned_data['username']
        request_password = login_form.cleaned_data['password']

        user = User.objects.raw(settings.TQS.select(table='users', where_values=f"username='{request_username}'"))[0]

        if not user:
            return False

        if not check_password(request_password, user.user_password):
            print('Error password')
            return False

        login(request, user)

        print(user.is_active())
        logout(user)

        return True

    @staticmethod
    def register_handler(request: HttpRequest, register_form: RegisterForm) -> bool:
        request_email = register_form.cleaned_data['email']
        request_username = register_form.cleaned_data['username']

        user = User.objects.raw(settings.TQS.select(table='users', where_values=f"username='{request_username}' OR email='{request_email}'"))

        if user:
            return False

        insert_data = register_form.cleaned_data
        insert_data['user_password'] = make_password(insert_data['password'])
        insert_data.pop('password')
        insert_data.pop('repeat_password')

        cursor = settings.TQS.create_cursor()
        cursor.execute(settings.TQS.insert(table='users', insert_value=insert_data))

        return True
