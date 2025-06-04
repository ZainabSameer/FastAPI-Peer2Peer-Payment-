from fastapi import FastAPI
from controllers import  users  # Adjust as needed

app = FastAPI()

app.include_router(users.router)

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}