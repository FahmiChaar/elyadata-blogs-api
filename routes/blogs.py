from fastapi import APIRouter
from models.blogs import Blogs, BlogSchema
import json

blogs = APIRouter()

@blogs.get('/blogs')
async def get_blogs():
    return json.loads(Blogs.objects().to_json())

@blogs.post('/blogs')
async def create_blog(data: BlogSchema):
    blog = Blogs(
        title = data.title,
        content = data.content,
        upvote = data.upvote or 0,
        downvote = data.downvote or 0
    )
    blog.save()
    return json.loads(blog.to_json())