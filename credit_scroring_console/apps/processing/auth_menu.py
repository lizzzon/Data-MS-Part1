from pydantic.error_wrappers import ValidationError

from apps.processing.abc_menu import ABCMenu
from apps.templates.menu_templates import START_APP_MESSAGE, LOGIN_MSG, REGISTER_MSG

from apps.models.database_models import UserModel

from apps.commands.user.user_commands import UserCommands
from apps.config.config import current_user

class LoginMenu(ABCMenu):

    def menu(self):
        dict_model = UserModel().dict(include={'username', 'user_password'})
        print(LOGIN_MSG, [k for k in dict_model.keys()])

        while True:
            for k in dict_model.keys():
                dict_model[k] = input(f"Введите {k}: ")
            try:
                user = UserModel(**dict_model)
            except ValidationError as ex:
                print(f'\nВозникла ошибка:\n{ex}\n Попробуем еще раз :D \n')
                continue

            user_from_db = UserCommands.select_user(user.username)

            if not user_from_db:
                print(f'Пользователь {user.username} не найден!')
                continue

            if user.user_password != user_from_db.user_password:
                print('Пароли не совпадают!')
                continue

            current_user.set(user)
            print('Успешный вход!')
            break

        return RegisterMenu

    def next(self):
        pass

    def back(self):
        pass


class RegisterMenu(ABCMenu):

    def menu(self):
        dict_model = UserModel().dict(exclude={'id', 'is_active', 'is_login'})
        print(REGISTER_MSG, [k for k in dict_model.keys()])

        while True:
            for k in dict_model.keys():
                dict_model[k] = input(f"Введите {k}: ")
            try:
                user = UserModel(**dict_model)
            except ValidationError as ex:
                print(f'\nВозникла ошибка:\n{ex}\n Попробуем еще раз :D \n')
                continue

            user_from_db = UserCommands.select_user(user.username)

            if user_from_db:
                print(f'Пользователь {user.username} уже существует!')
                continue

            UserCommands.insert_user()

            print('Успешная регистрация!')
            break

        return LoginMenu


class ExitMenu(ABCMenu):

    def menu(self):
        print('Досвидули, всего хорошего!')
        exit(0)

class StartMenu(ABCMenu):

    _choices = {
        1: LoginMenu,
        2: RegisterMenu,
        0: ExitMenu,
    }

    def menu(self):
        print(START_APP_MESSAGE)

        while True:
            choice = int(input('Ваш выбор: '))

            if choice in self._choices:
                break

            print(f'Нет выбора с пунктом {choice}\n')
        return self._choices[choice]

