from sqlalchemy.orm import Session

from laddr.contacts import models, schemas


def get_contacts(db: Session):
    return db.query(models.Contact).all()


def get_contact(db: Session, contact_id: int):
    db_contact = db.query(models.Contact).filter_by(id=contact_id).first()
    return db_contact


def get_contact_by_email(db: Session, email: str):
    db_contact = db.query(models.Contact).filter_by(email=email).first()
    return db_contact


def create_contact(db: Session, contact: schemas.ContactCreate):
    contact: dict = contact.dict()
    career_progression: list[schemas.CareerStepCreate] = contact.pop("career_progression", [])
    db_contact = models.Contact(**contact)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)

    for step in career_progression:
        db_step = models.CareerStep(**step, contact_id=db_contact.id)
        db.add(db_step)
    db.commit()

    return db_contact


def get_career(db: Session, contact_id: int):
    db_career = db.query(models.CareerStep).filter_by(contact_id=contact_id).all()
    return db_career
