from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from laddr.db import get_db
from laddr.contacts import operations, schemas

contacts = APIRouter()


@contacts.get("/", response_model=List[schemas.Contact])
def read_contacts(db: Session = Depends(get_db)):
    return operations.get_contacts(db=db)


@contacts.get("/{contact_id}", response_model=schemas.Contact)
def read_contact(
    contact_id: int = Path(
        title="The ID of the contact to fetch",
        ge=1,
    ),
    db: Session = Depends(get_db),
):
    db_contact = operations.get_contact(db=db, contact_id=contact_id - 1)
    if not db_contact:
        raise HTTPException(404, "Contact does not exist.")
    return operations.get_contact(db=db, contact_id=contact_id - 1)


@contacts.post("/create", response_model=schemas.Contact)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    db_contact = operations.get_contact_by_email(db, email=contact.email)
    if db_contact:
        raise HTTPException(400, "Contact already exists under that email.")

    return operations.create_contact(db=db, contact=contact)
