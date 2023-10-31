from datetime import date
from typing import Optional

from pydantic import BaseModel


# class AbstractBaseModel(BaseModel):
#     created_by_id: Optional[int]
#     # created_on: date
#     # updated_by_id: int
#     # updated_on: date
#     # tenant_id: int
#     # is_active: bool
#     # is_deleted: bool

class Company(BaseModel):
    name: Optional[str]
    code: Optional[str]


class CompanyList(Company):
    id: int


class Employee(BaseModel):
    name: Optional[str]
    code: Optional[str]


class EmployeeList(Company):
    id: int
