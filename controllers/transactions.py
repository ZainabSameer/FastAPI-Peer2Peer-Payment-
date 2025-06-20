from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.transaction import TransactionModel
from models.user import UserModel
from models.account import AccountModel
from serializers.transaction import TransactionSchema
from database import get_db

router = APIRouter()

@router.post("/transactions", response_model=TransactionSchema)
def create_transaction(transaction: TransactionSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    sender_account = db.query(AccountModel).filter(AccountModel.user_id == current_user.id).first()
    receiver_account = db.query(AccountModel).filter(AccountModel.user_id == transaction.receiver_id).first()

    if not receiver_account:
        raise HTTPException(status_code=404, detail="Receiver account not found")
    
    if sender_account.balance < transaction.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    new_transaction = TransactionModel(sender_id=current_user.id, receiver_id=transaction.receiver_id, amount=transaction.amount)
    db.add(new_transaction)

    sender_account.balance -= transaction.amount
    receiver_account.balance += transaction.amount

    db.commit()

    return new_transaction