import pytest

from src.infra.repositories.persons_repository import PersonsRepository
from src.infra.repositories.vehicles_repository import VehiclesRepository
from src.application.usecases.vehicle.add_vehicle_to_person_usecase import AddVehicleToPersonUsecase


@pytest.mark.asyncio
async def test_create_vehicle_to_person():
    """associate vehicle to a person"""

    person_repository = PersonsRepository()
    vehicle_repository = VehiclesRepository()
    vehicle_usecase = AddVehicleToPersonUsecase(
        vehicle_repository, person_repository)

    result = await vehicle_usecase.execute("hatch", "gray", "d1b16a36-f6a1-4256-adba-36788da751c4")        

    assert result != None    
