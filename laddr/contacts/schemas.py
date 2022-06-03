import datetime
from typing import Optional, List

from pydantic import BaseModel


class CareerStep(BaseModel):
    job_title: str
    company: Optional[str]
    start: Optional[datetime.date]
    end: Optional[datetime.date]


class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str]
    phone_number: Optional[str]
    career_progression: Optional[List[CareerStep]]


class ContactCreate(ContactBase):
    pass


class Contact(ContactBase):
    id: int
    is_active: bool
    created_on: datetime.date

    class Config:
        orm_mode = True
