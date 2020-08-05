from sqlalchemy import Column, String

from .entity import Entity, Base


class Employee(Entity, Base):
    __tablename__ = 'employees'

    full_name = Column(String(length=256))
    phone_number = Column(String(length=15))

    def __init__(self, full_name, phone_number, created_by):
        Entity.__init__(self, created_by)
        self.full_name = full_name 
        self.phone_number = phone_number