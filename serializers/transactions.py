from pydantic import BaseModel
from datetime import datetime

class TransactionSchema(BaseModel):
    sender_id: int
    receiver_id: int
    amount: float
    timestamp: datetime

    class Config:
        orm_mode = True