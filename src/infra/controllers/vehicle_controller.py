# pylint: disable=E1101,W0703
from flask import request, make_response, jsonify

from src.infra.repositories.persons_repository import PersonsRepository
from src.infra.repositories.vehicles_repository import VehiclesRepository
from src.application.usecases.vehicle.add_vehicle_to_person_usecase import (
    AddVehicleToPersonUsecase
)


class VehicleController:
    """vehicle controller"""

    async def handler(self, req: request):
        """vehicle handler"""

        vehicle_body = req.get_json()

        vehicles_repository = VehiclesRepository()
        persons_repository = PersonsRepository()
        join_vehicle_usecase = AddVehicleToPersonUsecase(
            vehicles_repository, persons_repository)

        try:
            result = await join_vehicle_usecase.execute(
                vehicle_body.get('model'),
                vehicle_body.get('color'),
                vehicle_body.get('person_id')
            )

            if result is not None:
                return jsonify({
                    "msg": f"The vehicle was added to {vehicle_body.get('person_id')} with success!"
                })
        except Exception as ex:
            return make_response(
                {"error": {
                    "message": str(ex)
                }},
                400,
            )
