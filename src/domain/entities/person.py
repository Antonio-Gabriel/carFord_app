from typing import Type
from uuid import uuid4
from dataclasses import dataclass

from cerberus import Validator
from ..validators.schemas.schemas import person_validator_schema


@dataclass
class PersonProps:
    """props to person"""

    name: str
    email: str
    is_admin: bool = 0


class Person:
    """person entity"""

    def __init__(self, person_props: Type[PersonProps], _id: str = None) -> None:
        self.person_props = person_props
        self.__id = _id if _id is not None else str(uuid4())

    @property
    def get_id(self) -> str:
        """get person id"""
        return self.__id

    def validate(self) -> (bool and dict):
        """person validator"""

        validador = Validator()
        result = validador.validate({
            "name": self.person_props.name,
            "email": self.person_props.email,
            "is_admin": self.person_props.is_admin
        }, person_validator_schema)

        return result, validador.errors

    def __repr__(self) -> str:
        return f"Person(id={self.get_id}, name={self.person_props.name}, \
                 email={self.person_props.email}, is_admin={self.person_props.is_admin})"
