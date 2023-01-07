# Elyadata Blogs Api

- Elyadata blogs api created with **Fastapi** and **Mongodb**

## Run the Api
- Clone the project
> git clone https://github.com/FahmiChaar/elyadata-blogs-api.git
- cd to project folder
> cd elyadata-blogs-api
- Setup your virtual envirment and activate
- Install requirments
> pip freeze > requirements.txt
- Run api
> uvicorn main:app --reload

## DB Configuration
- You can change db config in `config/db.py`
- The default db name is `elyadata`
- The default collection name is `blog`
- The default mongodb server port is `27017`