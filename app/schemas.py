from pydantic import BaseModel
from datetime import date
from typing import Dict

class BogieChecksheetCreate(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: date
    bmbcChecksheet: Dict
    bogieChecksheet: Dict
    bogieDetails: Dict

class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    wheelDetails: Dict