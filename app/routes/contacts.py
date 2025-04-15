from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from ..models import Contact, ContactCreate, ContactWithDetails, Phone, Tag
from ..crud import (
    create_contact, get_contact, get_contacts, 
    update_contact, delete_contact,
    get_contact_phones, get_contact_tags
)

router = APIRouter(prefix="/contacts", tags=["contacts"])

@router.post("/", response_model=Contact, status_code=201)
async def create_new_contact(contact: ContactCreate):
    db_contact = create_contact(contact.model_dump())
    if db_contact is None:
        raise HTTPException(status_code=400, detail="Contact could not be created")
    return db_contact

@router.get("/", response_model=List[Contact])
async def read_contacts(skip: int = 0, limit: int = 100, search: Optional[str] = None):
    contacts = get_contacts(skip=skip, limit=limit, search=search)
    return contacts

@router.get("/{contact_id}", response_model=ContactWithDetails)
async def read_contact(contact_id: int):
    db_contact = get_contact(contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    phones = get_contact_phones(contact_id)
    tags = get_contact_tags(contact_id)
    
    return ContactWithDetails(
        **db_contact,
        phone_numbers=phones,
        tags=tags
    )

@router.put("/{contact_id}", response_model=Contact)
async def update_existing_contact(contact_id: int, contact: ContactCreate):
    db_contact = update_contact(contact_id, contact.model_dump())
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@router.delete("/{contact_id}", status_code=204)
async def delete_existing_contact(contact_id: int):
    success = delete_contact(contact_id)
    if not success:
        raise HTTPException(status_code=404, detail="Contact not found")
    return None
