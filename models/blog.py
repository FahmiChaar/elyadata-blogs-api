from mongoengine import Document, StringField, IntField
from pydantic import BaseModel
from typing import Optional

class Blog(Document):
    title = StringField()
    content = StringField()
    author = StringField()
    upvote = IntField()
    downvote = IntField()

class BlogSchema(BaseModel):
    title: str
    content: str
    author: str
    upvote: Optional[int]
    downvote: Optional[int]

class VoteSchema(BaseModel):
    voteType: str