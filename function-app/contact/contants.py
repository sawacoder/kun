from collections import namedtuple
from enum import Enum


class Phonetype(Enum):
    HOME = 'home'
    WORK = 'work'
    OTHER = 'other'
    EMAIL = 'email'

    @classmethod
    def choises(cls):
        return [(item.name, item.value) for item in cls]

    @staticmethod
    def proccess():
        sh = namedtuple('a', 'name value')
        _ = list()
        for item in Phonetype:
            _.append(sh(item.name, item.value))
        return _
