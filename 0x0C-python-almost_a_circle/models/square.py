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

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the attribute size in width"""
        return self.width

    @size.setter
    def size(self, value):
        """sets value for height & width
        Aegs:
            value: object width in int
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method assigms an argument to each attribut

        args:
            *args: multiple non keyword arguments
        """
        if args and len(args) != 0:
            for arg in args:
                if len(args) == 1:
                    self.id = args[0]
                elif len(args) == 2:
                    self.id = args[0]
                    self.size = args[1]
                elif len(args) == 3:
                    self.id = args[0]
                    self.size = args[1]
                    self.x = args[2]
                elif len(args) == 4:
                    self.id = args[0]
                    self.size = args[1]
                    self.x = args[2]
                    self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for key, arg in kwargs.items():
                if key == 'id':
                    self.id = arg
                elif key == 'size':
                    self.size = arg
                elif key == 'x':
                    self.x = arg
                elif key == 'y':
                    self.y = arg

    def __str__(self):
        """informal string representation of the object"""
        return ("[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id, self.x, self.y,
            self.size))
