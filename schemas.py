from pydantic import BaseModel


# This class Helps you show Data to user that you want not more...
class UserBase(BaseModel): 
    email : str
    name : str
    family : str


class UserCreate(UserBase):
    password : str


class User(UserBase):
    id : int 

    class Config : 
        orm_mode = True
