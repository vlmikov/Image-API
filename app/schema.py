from doctest import Example
from pydantic import BaseModel, Field
from typing import Optional


class Images_info(BaseModel):
    image_url: str
    
    class Config:
        orm_mode=True
   

    

class Images_info_full(Images_info):
    image_sha1: str
    image_type:str
    local_url:str
    image_height: int
    image_width : int

    class Config:
        orm_mode =True


class Image_delete(BaseModel):
    id:int = Field(...,example="Enter id")