#!/usr/bin/python3
"""class inheritance"""
from models.base import Base


class Rectangle(Base):
    """class that inherits from another"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
