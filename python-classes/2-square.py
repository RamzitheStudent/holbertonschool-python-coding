#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    This class defines a square with a private size attribute.
    """

    def __init__(self, size=0):
        """
        Initialize the square.

        Args:
            size (int): Size of the square (default: 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Return the area of the square.

        Returns:
            int: Current square area.
        """
        return self.__size * self.__size
