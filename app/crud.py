from app.models import BogieChecksheet
from datetime import date
import json

def serialize_dates(obj):
    """Convert date/datetime in nested JSON to string."""
    if isinstance(obj, dict):
        return {k: serialize_dates(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [serialize_dates(i) for i in obj]
    elif isinstance(obj, (date,)):
        return obj.isoformat()
    return obj

async def create_bogie_checksheet(db, data):
    # ✅ Convert nested JSON fields safely
    data["bmbcChecksheet"] = serialize_dates(data["bmbcChecksheet"])
    data["bogieChecksheet"] = serialize_dates(data["bogieChecksheet"])
    data["bogieDetails"] = serialize_dates(data["bogieDetails"])

    checksheet = BogieChecksheet(**data)
    db.add(checksheet)
    await db.commit()
    await db.refresh(checksheet)
    return checksheet
