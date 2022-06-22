import datetime
from typing import Optional, List

from pydantic import BaseModel


class CareerStepBase(BaseModel):
    job_title: str
    company: Optional[str]
    start: Optional[datetime.date]
    end: Optional[datetime.date]


class CareerStepCreate(CareerStepBase):
    pass


class CareerStep(CareerStepBase):
    id: int
    contact_id: int

    class Config:
        orm_mode = True


class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class ContactCreate(ContactBase):
    career_progression: List[CareerStepCreate] = []
    phone_number: Optional[str]


class Contact(ContactBase):
    id: int
    is_active: bool
    created_on: datetime.date
    career_progression: List[CareerStep]

    class Config:
        orm_mode = True
