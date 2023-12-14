from typing import Union,Annotated
from pydantic import BaseModel,Field, constr
from typing import Optional

class User(BaseModel):
    name: Union[str,None]=None
    id: Annotated[Union[int,None],Field(default=100,ge=10,lt=200)]=None
    person: Union[str,None]=None
    day_list0: list
    day_list1:Union[list,None]=None
    day_list2:Union[list[int],None]=None


class Good(BaseModel):
    name:Union[str,None]=None
    description:Union[str,None]=None
    price:Union[float,None]=None
    nalog:Union[float,None]=None

class Person(BaseModel):
    name: str=Field(default="lastname",min_length=3,max_length=20)
    age:int=Field(default=100,ge=10,lt=200)

class Main_User(BaseModel):
    name: Union[str,None]=None
    id: Annotated[Union[int,None],Field(default=100,ge=1,lt=200)]=None

class Main_UserDB(BaseModel):
    id: int
    name: str
    password: Optional[constr(min_length=8)] = None

class New_Respons(BaseModel):
    message: str