class calculator:
    """class that allow the use of operator on vector"""

    def __init__(self, vector):
        """Init the calculator with a vector"""
        self.vector = vector

    def __add__(self, object) -> None:
        """add an object to the vector"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """multiply an object to the vector"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """substract an object to the vector"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """divide an object to the vector"""
        assert object != 0, "division by zero"
        self.vector = [x / object for x in self.vector]
        print(self.vector)
