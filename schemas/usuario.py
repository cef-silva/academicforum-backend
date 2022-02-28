from pydantic import BaseModel, Field


from typing import List, Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class UsuarioBase(BaseModel):
    _id: ObjectId
    name: str
    email: str
    password: str

class UsuarioDisplay(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: Optional[str]
    email: str
    profilePicture: Optional[str]
    about: Optional[str]
    profession: Optional[str]
    class Config():
        orm_mode=True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserAuth(BaseModel):
    email:str
    password:str