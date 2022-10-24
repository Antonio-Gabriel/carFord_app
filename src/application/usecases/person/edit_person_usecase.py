from typing import Type
from ...repositories.persons_repository import IPersonsRepository


class EditPersonUsecase:
    """persons usecase"""

    def __init__(self, persons_repository: Type[IPersonsRepository]) -> None:
        self.__persons_repository = persons_repository

    async def execute(self, person_id: str, name: str):
        """edit persons data"""

        person = await self.__persons_repository\
            .find_person_by_id(person_id=person_id)

        if not person:
            raise Exception("Person don't exists")

        updated_person = await self.__persons_repository\
            .edit(person_id=person_id, name=name)

        if updated_person is True:
            return person
