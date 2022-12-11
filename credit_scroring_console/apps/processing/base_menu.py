from apps.processing.abc_menu import ABCMenu


class BaseMenu(ABCMenu):

    def menu(self):
        print('base')
        pass
