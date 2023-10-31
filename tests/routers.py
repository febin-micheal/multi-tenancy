from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from tests import schemas, models

router = APIRouter(
    prefix="/tests",
    tags=["tests"],
)


@router.post("/company/")
def company_create(company: schemas.Company, db: Session = Depends(get_db)):
    data_dict = company.model_dump()
    company_instance = models.Company(**data_dict)
    db.add(company_instance)
    db.commit()
    db.refresh(company_instance)
    company_id = company_instance.id

    return {"id": company_id, "message": "Company created successfully"}


@router.get("/company/", response_model=List[schemas.CompanyList])
def company_list(skip: int = 0, limit: int = 100, name: str = None, code: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Company)

    if name:
        query = query.filter(models.Company.name.ilike(f"%{name}%"))
    if code:
        query = query.filter(models.Company.code.ilike(f"%{code}%"))

    return query.order_by(models.Company.id.desc()).offset(skip).limit(limit).all()


@router.post("/employee/")
def employee_create(employee: schemas.Employee, db: Session = Depends(get_db)):
    data_dict = employee.model_dump()
    employee_instance = models.Employee(**data_dict)
    db.add(employee_instance)
    db.commit()
    db.refresh(employee_instance)
    employee_id = employee_instance.id

    return {"id": employee_id, "message": "Employee created successfully"}


@router.get("/employee/", response_model=List[schemas.EmployeeList])
def employee_list(skip: int = 0, limit: int = 100, name: str = None, code: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Employee)

    if name:
        query = query.filter(models.Employee.name.ilike(f"%{name}%"))
    if code:
        query = query.filter(models.Employee.code.ilike(f"%{code}%"))

    return query.order_by(models.Employee.id.desc()).offset(skip).limit(limit).all()
