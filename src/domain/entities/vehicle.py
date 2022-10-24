# pylint: disable=E1101,W0703,W0212
from uuid import uuid4
from typing import Type
from datetime import datetime
from dataclasses import dataclass

from cerberus import Validator

from ..enums import Color, Model
from ..validators.schemas.schemas import vehicle_validator_schema


@dataclass
class VehicleProps:
    """props to vehicle entity"""

    model: Type[Model]
    color: Type[Color]
    person_id: str
    created_at: datetime
    updated_at: datetime


class Vehicle:
    """vehicle entity"""

    def __init__(self, vehicle_props: Type[VehicleProps], _id: str | None = None) -> None:
        self.vehicle_props = vehicle_props
        self.__id = _id if _id is not None else str(uuid4())

    @property
    def get_id(self) -> str:
        """get vehicle id"""
        return self.__id

    def validate(self) -> (bool and dict):
        """vehicle validator"""

        validador = Validator()
        result = validador.validate({
            # "model": self.vehicle_props.model._value_,
            # "color": self.vehicle_props.color._value_,
            "person_id": self.vehicle_props.person_id
        }, vehicle_validator_schema)

        return result, validador.errors

    def __repr__(self) -> str:
        return f"Vehicle(id={self.get_id}, model={self.vehicle_props.model}, \
                 color={self.vehicle_props.color}, \
                 person_id={self.vehicle_props.person_id}, \
                 created_at={self.vehicle_props.created_at}, updated_at={self.vehicle_props.updated_at})"
