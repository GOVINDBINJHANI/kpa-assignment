from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import WheelSpecification
from app.schemas import WheelSpecificationCreate
from sqlalchemy.future import select

router = APIRouter()

@router.post("/forms/wheel-specifications")
async def create_wheel_spec(data: WheelSpecificationCreate, db: AsyncSession = Depends(get_db)):
    entry = WheelSpecification(**data.dict())
    db.add(entry)
    await db.commit()
    await db.refresh(entry)
    return entry

@router.get("/forms/wheel-specifications")
async def get_wheel_spec(formNumber: str, submittedBy: str = None, submittedDate: str = None, db: AsyncSession = Depends(get_db)):
    stmt = select(WheelSpecification).where(WheelSpecification.formNumber == formNumber)
    if submittedBy:
        stmt = stmt.where(WheelSpecification.submittedBy == submittedBy)
    if submittedDate:
        stmt = stmt.where(WheelSpecification.submittedDate == submittedDate)
    result = await db.execute(stmt)
    return result.scalars().all()