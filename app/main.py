from fastapi import FastAPI
from app.routers import Characters
from app.routers import Actors
from contextlib import asynccontextmanager
from app.database import create_db_and_tables, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(Actors.router)
app.include_router(Characters.router)


@app.get("/")
async def root():
    return {"message": "HELLO HUMAN, IM A FISH"}
