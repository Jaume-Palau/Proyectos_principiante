'''CREACION DE LAS TABLAS'''

# Importar las librerias para las tablas
from sqlalchemy import Column,Integer,String
from database import Base

# Crear las tablas
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True )
    name = Column(String(50),nullable=False)
    age = Column(Integer)