from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class ContactBase(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    contact_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class PhoneBase(BaseModel):
    phone_type: str = "Mobile"
    number: str
    is_primary: bool = False

class PhoneCreate(PhoneBase):
    contact_id: int

class Phone(PhoneBase):
    phone_id: int
    
    class Config:
        from_attributes = True

class TagBase(BaseModel):
    name: str
    description: Optional[str] = None

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    tag_id: int
    
    class Config:
        from_attributes = True

class ContactWithDetails(Contact):
    phone_numbers: List[Phone] = []
    tags: List[Tag] = []
