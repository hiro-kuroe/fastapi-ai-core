from sqlalchemy import Column, Integer, Text, String
from app.db.base import Base


class Document(Base):
    __tablename__ = "documents"

    id= Column(Integer, primary_key=True)
    content = Column(Text)
    source = Column(String)