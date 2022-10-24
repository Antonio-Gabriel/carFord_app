import pytest
from src.infra.repositories.persons_repository import PersonsRepository
from src.application.usecases.person.get_all_persons_usecase import (
    GetAllPersonsUsecase)


@pytest.mark.asyncio
async def test_get_all_persons():
    """get all persons test"""

    person_repository = PersonsRepository()
    person_usecase = GetAllPersonsUsecase(person_repository)
    persons = await person_usecase.execute()

    assert isinstance(persons, list) == True