# pylint: disable=E1101,W0703,W0212
import os
from sqlalchemy import select, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from src.domain.entities.vehicle import Vehicle
from src.application.repositories.vehicles_repository import IVehiclesRepository

from ..models.models import VehicleModel, PersonModel


class VehiclesRepository(IVehiclesRepository):
    """vehicles repository of infra"""
    
    DATABASE_URL = os.getenv("DB_URL")

    def __init__(self) -> None:
        self.__engine = create_async_engine(
            self.DATABASE_URL, future=True, echo=True)
        self.__session: AsyncSession = sessionmaker(
            bind=self.__engine, expire_on_commit=False, class_=AsyncSession)

    async def register_vehicle_to_person(self, vehicle: Vehicle):
        """register a vehicle to a person method"""
        vehicle_model = VehicleModel(id=vehicle.get_id, person_id=vehicle.vehicle_props.person_id,
                                     model=vehicle.vehicle_props.model, color=vehicle.vehicle_props.color)

        async with self.__session() as session:
            session.add(vehicle_model)
            await session.commit()
        return vehicle

    async def find_vehicles_by_person(self, person_id: str) -> list:
        """get all vehicles related to a specific person"""
        async with self.__session() as session:
            query = select(VehicleModel, PersonModel).where(and_(
                VehicleModel.person_id == person_id
            )).join(PersonModel)

            result = await session.execute(query)
        return result.fetchall()

    async def get_all_vehicles(self) -> list:
        """get all vehicles related to persons"""
        query = select(VehicleModel, PersonModel)\
            .join(PersonModel)

        async with self.__session() as session:
            result = await session.execute(query)
        return result.fetchall()
