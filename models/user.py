

'''
from sqlalchemy import Column, Integer, String , ForeignKey
from .base import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
import jwt
from config.environment import secret
from sqlalchemy.orm import relationship 


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserModel(BaseModel):


    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=True)

    def set_password(self, password: str):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password_hash)

    def generate_token(self):
        payload = {
            "exp": datetime.now(timezone.utc) + timedelta(days=1),
            "iat": datetime.now(timezone.utc),
            "sub": str(self.id)
        }
        token = jwt.encode(payload, secret, algorithm="HS256")
        return token
    

class UserModel(BaseModel):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    account = relationship("Account", back_populates="user")

'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from passlib.context import CryptContext
from database import Base 

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String, nullable=False)

    account = relationship("AccountModel", back_populates="user")

    def set_password(self, password: str):
        self.password_hash = CryptContext(schemes=["bcrypt"]).hash(password)

    def verify_password(self, password: str) -> bool:
        return CryptContext(schemes=["bcrypt"]).verify(password, self.hashed_password)