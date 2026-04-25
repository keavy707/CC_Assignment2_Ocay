from fastapi import APIRouter, HTTPException , status
from app.models.Characters import Characters
from sqlmodel import Session, select
from typing import List
from .. import schemas
from sqlalchemy.orm import joinedload

router = APIRouter(prefix="/Characters", tags=["Characters"])
from ..database import engine

@router.get("/", summary="Get all Characters", response_model=List[schemas.CharacterList])
async def get_all():
    with Session(engine) as session:
        statement = select(Characters)
        results = session.exec(statement).all()
        # Even though 'results' has all data, 
        # response_model=List[schemas.CharacterList] filters it to just names!
        return results

@router.get("/{item_id}", summary="Get Characters by ID", response_model=schemas.CharacterDetail)
async def get_item(item_id: int):
    with Session(engine) as session:
        # We add .options(joinedload(Characters.voice_actor)) here
        statement = select(Characters).where(Characters.id == item_id).options(joinedload(Characters.voice_actor))
        item = session.exec(statement).first()
        
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found")
        return item



@router.post("/", summary="Create a new Characters", status_code=status.HTTP_201_CREATED)
async def create_item(_Characters : Characters):
    with Session(engine) as session:
        session.add(_Characters)
        session.commit()
        session.refresh(_Characters)
        return _Characters


@router.get("/{item_id}", summary="Get Characters by ID")
async def get_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Characters, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Characters not found")
        return item



@router.put("/{item_id}", summary="Update Characters")
async def update_item(_Characters : Characters , item_id: int):
    with Session(engine) as session:

        item = session.get(Characters, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Characters not found")

        for key, value in _Characters.model_dump(exclude_unset=True).items():
            setattr(item, key, value)

        session.add(item)
        session.commit()
        session.refresh(item)
        return item


@router.delete("/{item_id}", summary="Delete Characters" ,status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):

    with Session(engine) as session:
        item = session.get(Characters, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Characters not found")

        session.delete(item)
        session.commit()
        return None
