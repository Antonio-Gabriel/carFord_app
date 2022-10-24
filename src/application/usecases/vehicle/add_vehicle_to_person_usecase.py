from typing import Type

from ...adapter.vehicle_adapter import VehicleAdapter
from ...repositories.persons_repository import IPersonsRepository
from ...repositories.vehicles_repository import IVehiclesRepository
from ...utils import get_model_type_by_request, get_color_type_by_request


class AddVehicleToPersonUsecase:
    """vehicle usecase"""

    def __init__(self, vehicles_repositry: Type[IVehiclesRepository], persons_repository: Type[IPersonsRepository]) -> None:
        self.__vehicles_repository = vehicles_repositry
        self.__persons_repository = persons_repository

    async def execute(self, model: str, color: str, person_id: str):
        """add vehicle to a person"""

        if not get_model_type_by_request(model) or not get_color_type_by_request(color):
            raise Exception(
                f'Please verify your model: {["hatch", "sedan", "convertible"]} or color: {["yellow", "blue", "gray"]}!')

        vehicle = VehicleAdapter.create(get_model_type_by_request(
            model), get_color_type_by_request(color), person_id)

        _, err = vehicle.validate()

        if err:
            raise Exception(err)

        persons_dont_exists = await self.__persons_repository\
            .find_person_by_id(person_id=person_id)

        if not persons_dont_exists:
            raise Exception("Persons don't exist")

        vehicles_joined_to_person = await self.__vehicles_repository\
            .find_vehicles_by_person(person_id=person_id)

        if len(vehicles_joined_to_person) == 3:
            raise Exception(
                "Sorry, you cannot add a new vehicle to this user because already have the limit of cars [3]")

        result = await self.__vehicles_repository\
            .register_vehicle_to_person(vehicle=vehicle)

        if result:
            return result
