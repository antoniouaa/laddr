from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql.functions import now
from sqlalchemy.orm import relationship

from laddr.db import Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=True, unique=True, index=True)
    phone_number = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_on = Column(Date, server_default=now())

    career_progression = relationship("CareerStep", back_populates="contact")


class CareerStep(Base):
    __tablename__ = "careersteps"
    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String, nullable=False)
    company = Column(String, nullable=True)
    start = Column(DateTime, nullable=True)
    end = Column(DateTime, nullable=True)
    contact_id = Column(Integer, ForeignKey("contacts.id"))

    contact = relationship("Contact", back_populates="career_progression")
