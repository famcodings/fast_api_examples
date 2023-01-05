from pydantic import BaseModel
from typing import Optional


class Post(BaseModel):
    title: str
    content: str
    post_by: Optional[str] = None
    


class UpdatePost(BaseModel):
    title: str = None
    content: str = None
    post_by: Optional[str] = None