from typing import List
from src.domain.entities.person import Person
from src.application.repositories.persons_repository import IPersonsRepository


class PersonsRepositoryFaker(IPersonsRepository):
    """person repository infra"""

    def __init__(self) -> None:
        self.__persons_repository: List[Person] = []

    async def sign_in_to_admin(self, email: str, password: str) -> dict:
        """sign in to is_admin person"""

        print("hi")

    async def create(self, person: Person) -> Person:
        """create new person"""

        self.__persons_repository.append(person)

        return person

    async def all(self) -> List[Person]:
        """get persons"""

        return self.__persons_repository

    async def find_person_by_email(self, email: str) -> List[Person]:
        """get person by email"""

        print("hi")

    async def find_person_by_id(self, person_id: str) -> list:
        """get person by id"""

        print("hi")

    async def edit(self, person_id: str, name: str):
        """edit a person"""

        print("yh")
