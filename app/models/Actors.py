from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from . import Characters

class Actors(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    language: str
    
    # Use "Characters" as a string here.
    characters: List["Characters"] = Relationship(back_populates="voice_actor")
