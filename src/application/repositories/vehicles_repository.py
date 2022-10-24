from abc import ABC, abstractmethod

from ...domain.entities.vehicle import Vehicle


class IVehiclesRepository(ABC):
    """vehicles repository interface"""

    @abstractmethod
    async def register_vehicle_to_person(self, vehicle: Vehicle):
        """register a vehicle to a person method"""

        raise NotADirectoryError("Method not implemented")

    @abstractmethod
    async def get_all_vehicles(self) -> list:
        """get all vehicles related to persons"""

        raise NotADirectoryError("Method not implemented")

    @abstractmethod
    async def find_vehicles_by_person(self, person_id: str) -> list:
        """get all vehicles related to a specific person"""

        raise NotADirectoryError("Method not implemented")
