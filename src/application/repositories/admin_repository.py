from abc import ABC, abstractmethod

from ...domain.entities.person import Person


class IAdminRepository(ABC):
    """admin repository interface"""

    @abstractmethod
    async def create_admin(self, person_id: str, password: str) -> Person:
        """create an admin"""

        raise NotImplementedError("Method not implemented")
