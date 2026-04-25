from fastapi import APIRouter, HTTPException , status
from app.models.Actors import Actors
from sqlmodel import Session, select

router = APIRouter(prefix="/Actors", tags=["Actors"])
from ..database import engine

@router.get("/", summary="Get all Actors")
async def get_all():
    with Session(engine) as session:
        statement = select(Actors)
        results = session.exec(statement).all()
        return results



@router.post("/", summary="Create a new Actors", status_code=status.HTTP_201_CREATED)
async def create_item(_Actors : Actors):
    with Session(engine) as session:
        session.add(_Actors)
        session.commit()
        session.refresh(_Actors)
        return _Actors


@router.get("/{item_id}", summary="Get Actors by ID")
async def get_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Actors, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Actors not found")
        return item



@router.put("/{item_id}", summary="Update Actors")
async def update_item(_Actors : Actors , item_id: int):
    with Session(engine) as session:

        item = session.get(Actors, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Actors not found")

        for key, value in _Actors.model_dump(exclude_unset=True).items():
            setattr(item, key, value)

        session.add(item)
        session.commit()
        session.refresh(item)
        return item


@router.delete("/{item_id}", summary="Delete Actors" ,status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):

    with Session(engine) as session:
        item = session.get(Actors, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Actors not found")

        session.delete(item)
        session.commit()
        return None
