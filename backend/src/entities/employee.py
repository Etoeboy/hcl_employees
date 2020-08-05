from sqlalchemy import Column, String
from marshmallow import Schema, fields
from .entity import Entity, Base


class Employee(Entity, Base):
    __tablename__ = 'employees'

    full_name = Column(String(length=256))
    phone_number = Column(String(length=15))

    def __init__(self, full_name, phone_number, created_by):
        Entity.__init__(self, created_by)
        self.full_name = full_name 
        self.phone_number = phone_number

class EmployeeSchema(Schema):
    id = fields.Number()
    full_name = fields.Str()
    phone_number = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()