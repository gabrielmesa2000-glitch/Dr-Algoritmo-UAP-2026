from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    visits = relationship('Visit', back_populates='patient')
    events = relationship('Event', back_populates='patient')

class Visit(Base):
    __tablename__ = 'visits'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    date = Column(String, index=True)
    description = Column(String)

    patient = relationship('Patient', back_populates='visits')

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    event_type = Column(String)
    date = Column(String, index=True)

    patient = relationship('Patient', back_populates='events')
