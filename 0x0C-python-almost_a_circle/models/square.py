#!/usr/bin/python3

"""Module creates the class Square which inherits from Rectangle
class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class is a special Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """method initialize the class objects

        Args:
            size: square size
            x: x coordinate
            y: y coordinate
            id: identifier
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """informal string representation of the object"""
        return ("[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id, self.x, self.y,
            self.height))
