from fastapi import FastAPI
from controllers import  users 


app = FastAPI()

app.include_router(users.router)

@app.get("/")
def home():
    return {"Welcome to Zaianb Bank :)"}