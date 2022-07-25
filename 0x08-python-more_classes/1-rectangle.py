#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """Class to create a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle with `width` and `height`.

        args:
            width (int): width of rectangle with value >= 0.
            height (int): height of rectangle with value >= 0.
        """

        self.width = width
        self.height = height
    
    @property
    def height(self):
        """Getter function for `height` attribute.

        Returns: value of `height` attribute.
        """
         return self.__height

     @height.setter
     def height(self, value):
         """Setter function for `height` attribute.

         Args:
            value (int): value to use for `height`.

         Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0.
        """
        

