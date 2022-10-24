from datetime import datetime
from typing import Type
from ...domain.enums import Model, Color
from ...domain.entities.vehicle import Vehicle, VehicleProps


class VehicleAdapter:
    """vehicle adapter"""
    @staticmethod
    def create(model: Type[Model], color: Type[Color], person_id: str) -> Vehicle:
        """create an adapter to vehicle"""
        return Vehicle(VehicleProps(
            model=model,
            color=color,
            person_id=person_id,
            created_at=datetime.now,
            updated_at=datetime.now
        ))
