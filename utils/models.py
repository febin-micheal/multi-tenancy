import re
from datetime import date, datetime

from sqlalchemy import Integer, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, declared_attr, declarative_base


def resolve_table_name(name):
    """Resolves table names to their mapped names."""
    names = re.split("(?=[A-Z])", name)  # noqa
    return "_".join([x.lower() for x in names if x])


class CustomBase:
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    __name__: str

    @declared_attr
    def __tablename__(self):
        return resolve_table_name(self.__name__)

    created_by_id: Mapped[int] = mapped_column(Integer, nullable=True)
    # created_on: Mapped[date] = mapped_column(DateTime, nullable=True, default=datetime.utcnow)
    # updated_by_id: Mapped[int] = mapped_column(Integer, nullable=True)
    # updated_on: Mapped[date] = mapped_column(DateTime, nullable=True, onupdate=datetime.utcnow)
    # tenant_id: Mapped[int] = mapped_column(Integer, nullable=True)
    # is_active: Mapped[bool] = mapped_column(Boolean, nullable=True, default=True)
    # is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=True, default=False)


Base = declarative_base(cls=CustomBase)
