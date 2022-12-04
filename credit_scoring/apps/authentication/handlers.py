from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.http.request import HttpRequest
from django.contrib.auth.models import User as DJUser

from apps.authentication.forms import LoginForm, RegisterForm
from apps.orm.models_orm import User


class AuthenticationHandler:

    @classmethod
    def _login(cls, request: HttpRequest, user: User):
        user.is_login = True

        cursor = settings.TQS.create_cursor()
        cursor.execute(settings.TQS.update(table='users', set_value={'is_login': 'true'}, where_values=f'id={user.pk}'))

        login(request, DJUser.objects.get(username=user.username))

    def logout_handler(self, request: HttpRequest, user: User) -> bool:
        user.is_login = False

        cursor = settings.TQS.create_cursor()
        cursor.execute(settings.TQS.update(table='users', set_value={'is_login': 'false'}, where_values=f'id={user.pk}'))
        logout(request)

        print('Success logout')

        return True

    def login_handler(self, request: HttpRequest, login_form: LoginForm) -> bool:
        request_username = login_form.cleaned_data['username']
        request_password = login_form.cleaned_data['password']

        user = User.objects.raw(settings.TQS.select(table='users', where_values=f"username='{request_username}'"))

        if not user:
            print('User not found!')
            return False

        user = user[0]

        if not check_password(request_password, user.user_password):
            print('Error password!')
            return False

        self._login(request, user)

        print('Success login')

        return True

    def register_handler(self, register_form: RegisterForm) -> bool:
        request_email = register_form.cleaned_data['email']
        request_username = register_form.cleaned_data['username']

        user = User.objects.raw(settings.TQS.select(table='users', where_values=f"username='{request_username}' OR email='{request_email}'"))

        if user:
            print('User already exists!')
            return False

        insert_data = register_form.cleaned_data
        dj_user = DJUser(
            username=insert_data['username'],
            password=insert_data['password'],
        )
        dj_user.save()

        insert_data['user_password'] = make_password(insert_data['password'])
        insert_data.pop('password')
        insert_data.pop('repeat_password')

        cursor = settings.TQS.create_cursor()
        cursor.execute(settings.TQS.insert(table='users', insert_value=insert_data))

        print('Success register')

        return True
