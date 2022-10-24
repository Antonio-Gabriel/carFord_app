from typing import Type

from ...repositories.vehicles_repository import IVehiclesRepository


class GetVehiclesByPerson:
    """vehicle usecase"""

    def __init__(self, vehicles_repositry: Type[IVehiclesRepository]) -> None:
        self.__vehicles_repositry = vehicles_repositry

    async def execute(self, person_id: str) -> list:
        """get all vehicles by person"""
        return await self.__vehicles_repositry\
            .find_vehicles_by_person(person_id=person_id)
