from sqlalchemy import Column, Integer, String, Float, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class Survivor(Base):
    __tablename__ = 'survivors'
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()), nullable=False)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(1), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    infected = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()), nullable=False)
    survivor_id = Column(String(36), ForeignKey('survivor.id'))
    water = Column(Integer, default=0)
    food = Column(Integer, default=0)
    medication = Column(Integer, default=0)
    ammunition = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())

class Report(Base):
    __tablename__ = 'reports'
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()), nullable=False)
    infected_percentage = Column(Float)
    non_infected_percentage = Column(Float)
    avg_water = Column(Float)
    avg_food = Column(Float)
    avg_medication = Column(Float)
    avg_ammunition = Column(Float)
    points_lost = Column(Integer)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())
