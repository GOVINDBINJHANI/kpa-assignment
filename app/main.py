from fastapi import FastAPI
from app.routes import bogie_checksheet, wheel_specifications
from app.database import engine, Base

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(bogie_checksheet.router)
app.include_router(wheel_specifications.router)