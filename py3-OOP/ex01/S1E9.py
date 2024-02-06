from abc import ABC, abstractmethod


class Character(ABC):
    """a class that define a character"""

    @abstractmethod
    def die(self):
        pass

    def __init__(self, first_name, is_alive=True):
        """Init the character with a first name and a boolean
        to know if he is alive or not"""
        self.first_name = first_name
        self.is_alive = is_alive

    first_name = None
    is_alive = True


class Stark(Character):
    """winter is coming"""
    def die(self):
        """Make the character die"""
        self.is_alive = False
