from pydantic import BaseModel, Field
from typing import List, Optional

# User Schemas
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

# Recipe Schemas
class RecipeBase(BaseModel):
    title: str
    description: str

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(RecipeBase):
    title: Optional[str] = Field(None, example="Updated Recipe Title")
    description: Optional[str] = Field(None, example="Updated Recipe Description")

class RecipeResponse(RecipeBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# Search Schema
class RecipeSearchResponse(BaseModel):
    recipes: List[RecipeResponse]
    total: int

    class Config:
        orm_mode = True