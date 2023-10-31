from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from utils.models import Base


class Company(Base):
    name: Mapped[str] = mapped_column(String(255), nullable=True)
    code: Mapped[str] = mapped_column(String(25), nullable=True)

    employee: Mapped[List["Employee"]] = relationship(back_populates="company", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Company(id={self.id!r}, name={self.name!r}, code={self.code!r})"


class Employee(Base):
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"), nullable=True)
    company: Mapped["Company"] = relationship(back_populates="employee")
    name: Mapped[str] = mapped_column(String(255), nullable=True)
    code: Mapped[str] = mapped_column(String(25), nullable=True)

    def __repr__(self) -> str:
        return f"Employee(id={self.id!r}, name={self.name!r}, code={self.code!r})"
