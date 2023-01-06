from fastapi import FastAPI
from config.db import *
from routes.blogs import blogs

app = FastAPI()

app.include_router(blogs)