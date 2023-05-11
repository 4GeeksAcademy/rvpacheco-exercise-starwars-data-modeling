import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'People'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(20), nullable=False)
    height = Column(String(20), nullable=True)
    mass = Column(String(20), nullable=True)
    hair_color = Column(String(250), nullable=True)
    skin_color = Column(String(250), nullable=True)
    homeworld = Column(String(250), nullable=True)
    planet = relationship("Planets")
    films = relationship("Films")

class Cast(Base):
    __tablename__ = 'cast'
    id= Column(Integer, primary_key=True)
    film_id= Column(Integer, ForeignKey("films.id"))
    film=relationship("Films", backref= "cast")
    people_id=Column(Integer,ForeignKey("people.id"))
    planet=relationship("Planets") 

class Films(Base):
    __tablename__ = 'Films'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    episode_id = Column(Integer, primary_key=True)
    producer = Column(String(250),nullable=True)
    release_date = Column(Integer, nullable=True)
    title = Column(String(100),nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
