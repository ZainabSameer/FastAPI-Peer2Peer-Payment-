
'''
from sqlalchemy import Column, Integer, String, DECIMAL, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from .user import UserModel
class AccountModel(BaseModel):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    balance = Column(DECIMAL(15, 2), default=0.00)
    currency = Column(String(3), default="USD")
    created_at = Column(TIMESTAMP, nullable=False)

    # Relationships
    user = relationship("UserModel", back_populates="account")


class AccountModel(BaseModel):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UserModel", back_populates="account")

    '''


from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class AccountModel(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    balance = Column(Float, default=0.0)

    user = relationship("UserModel", back_populates="account")