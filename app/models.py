from .database import Base
from sqlalchemy import Column, PrimaryKeyConstraint, String, Boolean, Integer, DateTime
from sqlalchemy.sql import func




class Images_info(Base):
    __tablename__ = 'images_info'
    id = Column(Integer, primary_key= True, autoincrement = True)
    image_url = Column(String)
    image_sha1 = Column(String)
    image_type = Column(String)
    local_url = Column(String)
    image_height = Column(Integer)
    image_width = Column(Integer)
    time_add = Column(DateTime(timezone=True), server_default=func.now())

    