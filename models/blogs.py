from mongoengine import Document, StringField, IntField
from pydantic import BaseModel
from typing import Optional

class Blogs(Document):
    title = StringField()
    content = StringField()
    upvote = IntField()
    downvote = IntField()

class BlogSchema(BaseModel):
    title: str
    content: str
    author: str
    upvote: Optional[int]
    downvote: Optional[int]