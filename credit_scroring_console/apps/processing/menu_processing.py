from apps.processing.menu import StartMenu


class Menu:

    def __init__(self):
        self._current_menu = StartMenu

    def processing(self):
        while True:
            self._current_menu = self._current_menu().menu()

