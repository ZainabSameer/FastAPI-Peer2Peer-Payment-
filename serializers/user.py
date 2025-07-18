from pydantic import BaseModel , ConfigDict

class UserSchema(BaseModel):
    username: str
    email: str
    password_hash: str

    '''model_config = ConfigDict(
        from_attributes=True  
    )'''

    class Config:
        orm_mode = True

class UserResponseSchema(BaseModel):
    username: str
    email: str

class UserLogin(BaseModel):
    username: str
    password_hash: str  
class UserToken(BaseModel):
    token: str
    message: str

    model_config = ConfigDict(
        from_attributes=True  
    )
