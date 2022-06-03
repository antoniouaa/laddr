from typing import List, Optional

from sqlalchemy.orm import Session

from laddr.contacts import models, schemas


def get_contacts(db: Session) -> List[models.Contact]:
    return db.query(models.Contact).all()


def get_contact(db: Session, contact_id: int) -> models.Contact:
    return db.query(models.Contact).filter_by(id=contact_id).first()


def get_contact_by_email(db: Session, email: str) -> Optional[models.Contact]:
    db_contact = db.query(models.Contact).filter_by(email=email).first()
    return db_contact


def create_contact(db: Session, contact: schemas.ContactCreate) -> models.Contact:
    contact.career_progression = contact.career_progression or []
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact
