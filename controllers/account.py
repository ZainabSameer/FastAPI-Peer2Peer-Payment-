from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.account import AccountModel
from models.user import UserModel
from serializers.account import AccountSchema
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.get("/accounts/me", response_model=AccountSchema)
def get_my_account(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    account = db.query(AccountModel).filter(AccountModel.user_id == current_user.id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account
