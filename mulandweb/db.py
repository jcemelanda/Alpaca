# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text
from geoalchemy2 import Geometry

engine = create_engine('postgresql://leandro:manhangis@colby/leandro')
Base = declarative_base()

class Zones(Base):
    __tablename__ = 'zones'
    id = Column(Integer, primary_key=True)
    area = Column(Geometry('POLYGON', srid=900913, spatial_index=True))
    info = Column(Text)
