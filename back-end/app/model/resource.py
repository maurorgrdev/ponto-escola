from ..configuration import Base
from sqlalchemy import Column, Integer, String

class Resource(Base):
    __tablename__ = 'resource'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
