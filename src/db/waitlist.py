from sqlalchemy import Column, Integer, String, ForeignKey, UUID, JSON, DateTime, func, Double
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Waitlist(Base):
    __tablename__ = 'waitlist'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)

    def __repr__(self):
        return f'<Account {self.email}>'