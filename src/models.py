import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True)
    email = Column(String(120),unique=True,nullable = False)
    password = Column(String(120),unique=False,nullable = False)
    is_active = Column(Boolean(),unique=False, nullable=False)

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(20), nullable=False)
    height = Column(String(20), nullable=True)
    mass = Column(String(20), nullable=True)
    hair_color = Column(String(250), nullable=True)
    skin_color = Column(String(250), nullable=True)
    homeworld_id = Column(Integer, ForeignKey("planets.id"))
    people = relationship("Films")
    vehicles = relationship("Vehicles")

class Films(Base):
    __tablename__ = 'films'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    director = Column(String(100))
    episode_id = Column(String(100),nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'))
    Cast = relationship ("cast")
    Vehicles = relationship ("vehicles")

class Cast(Base):
    __tablename__ = 'cast'
    id= Column(Integer, primary_key=True)
    film_id= Column(Integer, ForeignKey("films.id"))
    film=relationship("Films", backref= "cast")
    people_id=Column(Integer,ForeignKey("people.id"))
    people=relationship("Planets",backref="people")
    planet_id=relationship(Integer,ForeignKey("planet.id"))
    planet=relationship("Planets",backref="cast") 
    
class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    model= Column(String(250), nullable=False)
    vehicle_class= Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    films_id = Column(Integer, ForeignKey('films.id')) 
    pilots_id = Column(Integer, ForeignKey('people.id'))
    Cast = relationship ("cast")

class Planets(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    climate= Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    people = relationship ("people")
    Cast = relationship ("cast")

class Favorites(Base):
    __tablename__= 'favorites'
    id = Column(Integer,primary_key=True)
    type = Column(String(20), nullable=False)
    element_id = Column(Integer, nullable=False)
    user_id=Column(Integer, ForeignKey("users.id"))
    user = relationship(User)
    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship(Films)
    person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship(People)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship(Vehicles)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    


def to_dict(self):
 return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
