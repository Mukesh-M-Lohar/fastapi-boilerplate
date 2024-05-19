import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, SQLModel


class TimestampMixin(SQLModel):
    created_at: datetime = Field(
        sa_column=Column(
            DateTime,
            default=func.now(),
            nullable=False,
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime,
            default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )
    )


class UUIDMixin(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)


class StatusMixin(SQLModel):
    status: str
