from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime

class AccountSchema(BaseModel):
    id: int
    user_id: int
    balance: Decimal
    currency: str
    created_at: datetime

    class Config:
        orm_mode = True
