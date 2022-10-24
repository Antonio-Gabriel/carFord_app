from typing import Type
from src.application.repositories.persons_repository import IPersonsRepository


class GetAllPersonsUsecase:
    """persons usecase"""

    def __init__(self, persons_repository: Type[IPersonsRepository]) -> None:
        self.__persons_repository = persons_repository

    async def execute(self) -> list:
        """return all persons"""
        return await self.__persons_repository.all()
