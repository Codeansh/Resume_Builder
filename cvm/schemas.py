from pydantic import BaseModel,EmailStr

class UserData(BaseModel):
    name : str
    phone : str
    email : EmailStr
    skills : str
    about  :str
    interests : str
    #
    # class Config :
    #     orm_mode = True