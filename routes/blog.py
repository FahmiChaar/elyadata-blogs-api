from fastapi import APIRouter
from models.blog import Blog, BlogSchema
import json

blogs = APIRouter()

@blogs.get('/blogs')
async def get_blogs():
    return json.loads(Blog.objects().to_json())

@blogs.get('/blogs/{blog_id}')
async def get_blog(blog_id: str):
    return json.loads(Blog.objects().get(id=blog_id).to_json())

@blogs.post('/blogs')
async def create_blog(data: BlogSchema):
    blog = Blog(
        title = data.title,
        content = data.content,
        author = data.author,
        upvote = data.upvote or 0,
        downvote = data.downvote or 0
    )
    blog.save()
    return json.loads(blog.to_json())