#!/usr/bin/python3
"""class inheritance"""
from models.base import Base

class Rectangle(Base):
    """class that inherits from another"""
    def __init__(self, width, height, x=0, y=0, id=None):
        
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise(TypeError("width must be an integer"))
        if value <= 0:
            raise(ValueError("width must be > 0"))
        self.width = value
    
    @property
    def height(self):
        """height getter"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise(TypeError("height must be an integer"))

        if value <= 0:
            raise(ValueError("height must be > 0"))
        self._height = value
    

    
