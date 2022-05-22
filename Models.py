
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TrackedTime(Base):
    __tablename__ = "tracked_time"
    task_id = Column(Integer, primary_key=True)
    date = Column(Date)
    title = Column(String)
    description = Column(String)
    tracked_seconds = Column(Integer)