from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Visit(Base):
    __tablename__ = 'visits'

    id = Column(Integer, primary_key=True, index=True)
    vital_sign_id = Column(Integer, ForeignKey('vital_signs.id'))
    condition_id = Column(Integer, ForeignKey('conditions.id'))
    heart_failure_id = Column(Integer, ForeignKey('heart_failure.id'))
    treatment_id = Column(Integer, ForeignKey('treatment.id'))
    score_id = Column(Integer, ForeignKey('scores.id'))

    vital_sign = relationship('VitalSign', back_populates='visits')
    condition = relationship('Condition', back_populates='visits')
    heart_failure = relationship('HeartFailure', back_populates='visits')
    treatment = relationship('Treatment', back_populates='visits')
    score = relationship('Score', back_populates='visits')

    # Add additional fields for the Visit model as necessary
