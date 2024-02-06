from S1E9 import Character


class Baratheon(Character):
    """Ours is the fury"""

    def __init__(self, first_name, is_alive=True):
        """Init the character"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Make the character die"""
        self.is_alive = False

    def __str__(self):
        """Return a string representation of the character"""
        return f"{self.first_name} Baratheon"

    def __repr__(self):
        """Return a complex string representation of the character"""
        vector = [self.family_name, self.eyes, self.hairs]
        vector = "\', \'".join(vector)
        vector = "Vector: (\'" + vector + "\')"
        return vector


class Lannister(Character):
    """A Lanister always pays his debt"""

    def __init__(self, first_name, is_alive=True):
        """Init the character"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Make the character die"""
        self.is_alive = False

    def __str__(self):
        """Return a string representation of the character"""
        return f"{self.first_name} Lanister"

    def __repr__(self):
        """Return a complex string representation of the character"""
        vector = [self.family_name, self.eyes, self.hairs]
        vector = "\', \'".join(vector)
        vector = "Vector: (\'" + vector + "\')"
        return vector

    def create_lannister(first_name, is_alive):
        """Create a Lannister"""
        return Lannister(first_name, is_alive)
