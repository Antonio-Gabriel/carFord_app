from typing import List
from abc import ABC, abstractmethod

from ...domain.entities.person import Person


class IPersonsRepository(ABC):
    """persons repository interface"""

    @abstractmethod
    async def sign_in_to_admin(self, email: str) -> dict:
        """sign in to is_admin person"""

        raise NotImplementedError('Method not implemented')

    @abstractmethod
    async def create(self, person: Person) -> Person:
        """create new person"""

        raise NotImplementedError('Method not implemented')

    @abstractmethod
    async def all(self) -> List[Person]:
        """get persons"""

        raise NotImplementedError('Method not implemented')

    @abstractmethod
    async def find_person_by_email(self, email: str) -> list:
        """get person by email"""

        raise NotImplementedError('Method not implemented')

    @abstractmethod
    async def find_person_by_id(self, person_id: str) -> list:
        """get person by id"""

        raise NotImplementedError('Method not implemented')

    @abstractmethod
    async def edit(self, person_id: str, name: str):
        """edit a person"""

        raise NotImplementedError('Method not implemented')
