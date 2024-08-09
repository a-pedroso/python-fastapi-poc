from pydantic import BaseModel, EmailStr, constr
#from datetime import datetime

class UserDTO(BaseModel):
    id: int 
    username: str
    email: EmailStr
    #created_at: datetime