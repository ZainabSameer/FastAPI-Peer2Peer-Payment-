from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class TransactionModel(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

    sender = relationship("UserModel", foreign_keys=[sender_id])
    receiver = relationship("UserModel", foreign_keys=[receiver_id])