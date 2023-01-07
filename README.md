# Elyadata Blogs Api

- Elyadata blogs api created with **Fastapi** and **Mongodb**

## Run the Api
- Clone the project
```properties
git clone https://github.com/FahmiChaar/elyadata-blogs-api.git
```
- cd to project folder
```properties
cd elyadata-blogs-api
```
- Setup your virtual envirment and activate
```properties
python3 -m venv env
source env/bin/activate
```
- Install requirments
```properties
pip install -r requirements.txt
```
- Run api
```properties
uvicorn main:app --reload
```

## DB Configuration
- You can change db config in `config/db.py`
- The default db name is `elyadata`
- The default collection name is `blog`
- The default mongodb server port is `27017`

## CORS
- Only this url is allowed `http://localhost:4200/` if you can change it in `main.py`