from typing import Type

from ...repositories.vehicles_repository import IVehiclesRepository


class GetAllVehiclesUsecase:
    """vehicle usecase"""

    def __init__(self, vehicles_repositry: Type[IVehiclesRepository]) -> None:
        self.__vehicles_repositry = vehicles_repositry

    async def execute(self) -> list:
        """get all vehicles relateds to a person"""
        return await self.__vehicles_repositry.get_all_vehicles()
