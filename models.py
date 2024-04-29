from pydantic import BaseModel
from typing import Optional

    
 
class ProductModel(BaseModel):
    id:Optional[int]
    name:str
    price:float
    description:Optional[str]


