from typing import Type
from ...repositories.persons_repository import IPersonsRepository
from ...adapter.person_adapter import PersonAdapter, Person


class CreatePersonUsecase:
    """create person usecase"""

    def __init__(self, persons_repository: Type[IPersonsRepository]) -> None:
        self.__persons_repository = persons_repository

    async def execute(self, name: str, email: str, is_admin: bool = False):
        """execute usecase"""

        person = PersonAdapter.create(name, email, is_admin)

        _, err = person.validate()

        if err:
            raise Exception(err)

        person_already_exists = await self.__persons_repository\
            .find_person_by_email(
                email=email)

        if person_already_exists:
            raise Exception(f"The person {email} already exists!")

        result = await self.__persons_repository.create(person=person)
        if result:
            return person
