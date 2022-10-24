import pytest
from faker import Faker
from src.infra.repositories.persons_repository import PersonsRepository
from src.application.usecases.person.create_person_usecase import (
    CreatePersonUsecase
)

faker = Faker()
faker_name = faker.name()
faker_email = faker.email()


@pytest.mark.asyncio
async def test_person_usecases_integration():
    """create person usecase integration"""

    person_repository = PersonsRepository()
    person_usecase = CreatePersonUsecase(person_repository)
    result = await person_usecase.execute(faker_name, faker_email)

    assert result.person_props.email == faker_email

