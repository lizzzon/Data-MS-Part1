from abc import ABC, abstractmethod


class ABCMenu(ABC):

    @abstractmethod
    def menu(self):
        raise NotImplementedError
