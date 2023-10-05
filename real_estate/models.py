"""Pydantic models"""
from typing import Optional, Annotated
from datetime import datetime
from importlib.metadata import metadata

from pydantic import BaseModel, ConfigDict, StringConstraints, PositiveInt, NonNegativeInt, StrictBool, Field

from real_estate.enums import Provider, State, Council, Suburb


class Listing(BaseModel):
    """A real estate listing"""

    model_config = ConfigDict(from_attributes=True)

    id: str = Field(alias="_id")
    datetime: datetime
    provider: Provider
    rental: StrictBool
    price: PositiveInt
    address: str
    suburb: Suburb
    state: State
    postcode: Annotated[str, StringConstraints(pattern=r"^\d{4}$")]
    council: Council
    bed: PositiveInt
    bath: PositiveInt
    parking: NonNegativeInt
    area: Optional[PositiveInt] = None
    dwelling: str
    version: Optional[str] = metadata("real_estate").get("version")
