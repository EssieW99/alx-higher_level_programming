#!/usr/bin/python3
"""
a file that contains the class definition of a State
and an instance Baase= declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


""" Create a declarative base instance"""
Base = declarative_base()


class State(Base):
    """a class on states that inherits the Base class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
