from sqlalchemy import Column, String, Date, JSON, Integer
from app.database import Base

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheet"

    id = Column(Integer, primary_key=True, index=True)  
    formNumber = Column(String)
    inspectionBy = Column(String)
    inspectionDate = Column(Date)
    bmbcChecksheet = Column(JSON)
    bogieChecksheet = Column(JSON)
    bogieDetails = Column(JSON)

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"
    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String)
    submittedBy = Column(String)
    submittedDate = Column(String)
    wheelDetails = Column(JSON)