# pylint: disable=E1101
import os
from typing import List

from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, and_, update
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from src.domain.entities.person import Person
from src.application.repositories.persons_repository import IPersonsRepository

from ..models.models import PersonModel, AdminModel


class PersonsRepository(IPersonsRepository):
    """person repository of infra"""

    DATABASE_URL = os.getenv("DB_URL")

    def __init__(self) -> None:
        self.__engine = create_async_engine(
            self.DATABASE_URL, future=True, echo=True)
        self.__session: AsyncSession = sessionmaker(
            bind=self.__engine, expire_on_commit=False, class_=AsyncSession)

    async def sign_in_to_admin(self, email: str) -> dict:
        """sign in to is_admin person"""

        async with self.__session() as session:
            query = select(PersonModel, AdminModel).where(and_(
                PersonModel.email == email
            )).join(AdminModel)

            result = await session.execute(query)
        return result.fetchone()

    async def create(self, person: Person) -> Person:
        """create new person"""
        person_model = PersonModel(id=person.get_id, name=person.person_props.name,
                                   email=person.person_props.email, is_admin=person.person_props.is_admin)

        async with self.__session() as session:
            session.add(person_model)
            await session.commit()
        return person

    async def all(self) -> List[Person]:
        """get persons"""
        async with self.__session() as session:
            query = select(PersonModel)

            result = await session.execute(query)
        return result.fetchall()

    async def find_person_by_email(self, email: str) -> list:
        """get person by email"""
        async with self.__session() as session:
            query = select(PersonModel).where(and_(
                PersonModel.email == email
            ))

            result = await session.execute(query)
        return result.fetchone()

    async def find_person_by_id(self, person_id: str) -> list:
        """get person by id"""
        async with self.__session() as session:
            query = select(PersonModel).where(and_(
                PersonModel.id == person_id
            ))

            result = await session.execute(query)
        return result.fetchone()

    async def edit(self, person_id: str, name: str):
        """edit a person"""
        async with self.__session() as session:
            query = update(PersonModel).where(and_(
                PersonModel.id == person_id
            )).values(name=name)

            await session.flush()
            await session.execute(query)
            await session.commit()

            return True
