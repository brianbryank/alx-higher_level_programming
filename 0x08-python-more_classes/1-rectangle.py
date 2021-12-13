#!/usr/bin/python3
""" defines a Rectangle class"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        """ Init Method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter def"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter def"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter def"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter def"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
