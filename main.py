from fastapi import FastAPI
from config.db import *
from routes.blog import blogs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(blogs)

origins = [ "http://localhost:4200" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)