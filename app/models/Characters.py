from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from . import Actors

class Characters(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    path: str
    element: str
    description: str
    
    actor_id: Optional[int] = Field(default=None, foreign_key="actors.id")
    
    # Use "Actors" as a string here. No import needed!
    voice_actor: Optional["Actors"] = Relationship(back_populates="characters")