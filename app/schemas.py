from pydantic import BaseModel
from typing import Optional

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
    # CHANGE THIS LINE: 
    # Instead of va_name: Optional[str], use:
    voice_actor: Optional[dict] = None 

    class Config:
        from_attributes = True