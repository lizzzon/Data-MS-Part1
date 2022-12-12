# Все меню в одном файле чтобы избежать циркуляции импортов
from typing import Optional
from pydantic.error_wrappers import ValidationError

from apps.commands.sql import SQLCommands
from apps.models.database_models import UserModel
from apps.templates.menu_templates import START_APP_MESSAGE, LOGIN_MSG, REGISTER_MSG

from apps.processing.abstract_menu import ABCMenu
from apps.templates.menu_templates import BASE_MSG

from apps.config.config import current_user
from apps.models.database_models import UserRoleEnum


def _is_agan():
    return input('Попробуем еще разок?\n1 - Да\n0 - Нет\n') == '0'


class LogoutMenu(ABCMenu):

    def menu(self):
        print(f'Успешный выход {current_user.get().username}!')
        current_user.set(None)
        return StartMenu

# ------------------------ START BASE ------------------------------

class ClientMenu(ABCMenu):

    @classmethod
    def _fill_information_about_yourself(cls):
        pass

    _choices = {
        1: _fill_information_about_yourself,
        2: 1,
        0: LogoutMenu,
    }

    def menu(self):
        user = current_user.get()
        while True:
            choice = int(input('Ваш выбор: '))

            if choice not in (1, 0) and not user.is_active:
                print('Сначала необходимо добавить информацию о себе!')
                continue

            if choice == 0:
                return self._choices[choice]

            self._choices[choice]()



class BaseMenu(ABCMenu):

    def menu(self):
        print(current_user.get())
        role = current_user.get().user_role
        print(BASE_MSG, f'ваша роль: {role}\n')

        if role == UserRoleEnum.client.name:
            return ClientMenu
        if role == UserRoleEnum.company.name:
            return BaseMenu
        if role == UserRoleEnum.staff.name:
            return BaseMenu
# ------------------------ END BASE ------------------------------

# ------------------------ START AUTH ------------------------------

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
                print(f'\nВозникла ошибка:\n{ex}\n')
                if _is_agan():
                    return StartMenu
                continue

            user_from_db: Optional[UserModel] = SQLCommands.select_one_execute(
                table='users',
                where_str=f"username = '{user.username}'",
                model=UserModel,
            )

            if not user_from_db:
                print(f'Пользователь {user.username} не найден!')
                if _is_agan():
                    return StartMenu
                continue

            if user.user_password != user_from_db.user_password:
                print('Пароли не совпадают!')
                if _is_agan():
                    return StartMenu
                continue

            user_from_db.is_login = True
            current_user.set(user_from_db)
            print('Успешный вход!')
            break

        return BaseMenu


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
                print(f'\nВозникла ошибка:\n{ex}\n')
                if _is_agan():
                    return StartMenu
                continue

            user_from_db: Optional[UserModel] = SQLCommands.select_one_execute(
                table='users',
                where_str=f"username = '{user.username}'",
                model=UserModel,
            )

            if user_from_db:
                print(f'Пользователь {user.username} уже существует!')
                if input('Попробуем еще раз?\n1 - Да\n0 - Нет') == '0':
                    return StartMenu
                continue

            SQLCommands.insert_execute(
                table='users',
                dict_model=dict_model,
            )

            print('Успешная регистрация!')
            break

        return LoginMenu


class ExitMenu(ABCMenu):

    def menu(self):
        print('Досвидули, всего хорошего!')
        exit(0)

# ------------------------ END AUTH ------------------------------

# ------------------------ START START ------------------------------
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
# ------------------------ END START ------------------------------
