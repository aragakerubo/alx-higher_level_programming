class Base:
    """My base class"""

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances


class User(Base):
    """My User class"""

    pass


u = User()
print(u.id)
#!/usr/bin/python3
"""Module for lookup method"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj)
