from fastapi import FastAPI
from routes import users, transactions

app = FastAPI()

app.include_router(users.router, prefix="/users")
app.include_router(transactions.router, prefix="/transactions")
