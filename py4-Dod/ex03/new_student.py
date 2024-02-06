import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate an id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(default="", init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        if not self.login:
            self.login = self.name[0] + self.surname
