#pylint: disable=E0110
import pytest
from tests.unit.repositories.persons_repository_faker import PersonsRepositoryFaker
from src.application.usecases.person.get_all_persons_usecase import GetAllPersonsUsecase
from src.application.usecases.person.create_person_usecase import (
    CreatePersonUsecase
)


@pytest.mark.asyncio
async def test_person_usecases():
    """create person usecase"""

    person_repository = PersonsRepositoryFaker()
    person_usecase = CreatePersonUsecase(person_repository)
    persons = await GetAllPersonsUsecase(person_repository).execute()
    await person_usecase.execute(
        "António Gabriel", "antoniogabriel@gmail.com")
    await person_usecase.execute(
        "Kiala Daniel", "kialadaniel@gmail.com")

    assert len(persons) > 0
