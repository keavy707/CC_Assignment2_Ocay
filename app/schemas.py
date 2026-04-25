from pydantic import BaseModel
from typing import Optional

class ActorSchema(BaseModel):
    id: int
    name: str
    language: str

    class Config:
        from_attributes = True

class CharacterList(BaseModel):
    name: str
    class Config:
        from_attributes = True

class CharacterDetail(BaseModel):
    id: int
    name: str
    path: str
    element: str
    description: str
    # Replace [dict] with [ActorSchema]
    voice_actor: Optional[ActorSchema] = None 

    class Config:
        from_attributes = True