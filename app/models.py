from sqlalchemy import Column, Integer, String
from database import base


class Images(base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
