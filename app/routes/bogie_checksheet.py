from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import BogieChecksheet
from app.schemas import BogieChecksheetCreate
from sqlalchemy.future import select

router = APIRouter()

@router.post("/forms/bogie-checksheet")
async def create_bogie_checksheet(data: BogieChecksheetCreate, db: AsyncSession = Depends(get_db)):
    new_entry = BogieChecksheet(**data.dict())
    db.add(new_entry)
    await db.commit()
    await db.refresh(new_entry)
    return new_entry

@router.get("/forms/bogie-checksheet")
async def get_bogie_checksheet(formNumber: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(BogieChecksheet).where(BogieChecksheet.formNumber == formNumber))
    return result.scalar_one_or_none()