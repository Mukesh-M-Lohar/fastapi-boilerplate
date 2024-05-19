import sqlmodel
from pydantic import BaseModel, Field


class Common(sqlmodel.SQLModel):
    city: str = Field(description="city")
    pin_code: str = Field(description="pin_code")
    email: str = Field(
        description="email", pattern="/^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$/gm"
    )
    phone_number: str = Field(
        description="phone_number", pattern="/^[0-9]{3}-[0-9]{3,4}-[0-9]{4}$/gm"
    )
    address: str = Field(description="address", max_length=100, nullable=True)
    country: str = Field(description="country")
    state: str = Field(description="state")

    class config:
        orm_mode = True
        arbitrary_types_allowed = True


class ModifyBy(BaseModel):
    modified_by: str = Field(description="modified_by")
