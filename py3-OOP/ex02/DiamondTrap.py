from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The king of the seven kingdoms"""

    def __init__(self, first_name, is_alive=True):
        """Init the king"""
        self = Baratheon.__init__(self, first_name, is_alive)

    def set_eyes(self, eyes):
        """Set the eyes color"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set the hairs color"""
        self.hairs = hairs

    def get_eyes(self):
        """Return the eyes color"""
        return self.eyes

    def get_hairs(self):
        """Return the hairs color"""
        return self.hairs
