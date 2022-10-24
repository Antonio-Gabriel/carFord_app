from typing import Type

from ...security.password import generate_password
from ...adapter.person_adapter import PersonAdapter
from ...repositories.admin_repository import IAdminRepository
from ...repositories.persons_repository import IPersonsRepository


class CreateAdminUsecase:
    """admin usecase"""

    def __init__(self, admin_repository: Type[IAdminRepository], persons_repository: Type[IPersonsRepository]) -> None:
        self.__admin_repository = admin_repository
        self.__persons_repository = persons_repository

    async def execute(self, name: str, email: str, password: str, is_admin: bool = True):
        """create an admin"""

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
            if person.person_props.is_admin is True:
                await self.__admin_repository\
                    .create_admin(person_id=person.get_id,
                                  password=generate_password(password))
