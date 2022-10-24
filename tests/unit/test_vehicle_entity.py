# pylint: disable=E1101,W0703
from uuid import uuid4
from datetime import datetime

from src.domain.enums import Model, Color
from src.domain.entities.vehicle import Vehicle, VehicleProps


def test_vehicle_entity():
    """should be return a model"""
    vehicle = Vehicle(VehicleProps(
        model=Model.HATCH,
        color=Color.BLUE,
        person_id=str(uuid4()),
        created_at=datetime.now,
        updated_at=datetime.now
    ))

    assert vehicle.vehicle_props.model == Model.HATCH
    assert isinstance(vehicle.get_id, str)


def test_vehicle_validator():
    """should be return true"""
    vehicle = Vehicle(VehicleProps(
        model=Model.HATCH,
        color=Color.BLUE,
        person_id=str(uuid4()),
        created_at=datetime.now,
        updated_at=datetime.now
    ))

    result, err = vehicle.validate()
    if err:
        print(err)

    assert result == True


def test_vehicle_bad_validator():
    """should be return false"""
    vehicle = Vehicle(VehicleProps(
        model=Model.HATCH,
        color=Color.BLUE,
        person_id=123,
        created_at=datetime.now,
        updated_at=datetime.now
    ))

    result, err = vehicle.validate()
    if err:
        print(err)

    assert result == False
    assert len(err) == 1
