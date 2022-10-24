from flask import Blueprint, request, jsonify

from src.infra.controllers.vehicle_controller import VehicleController
from src.infra.repositories.vehicles_repository import VehiclesRepository
from src.application.usecases.vehicle.get_vehicles_by_person import GetVehiclesByPerson
from src.application.usecases.vehicle.get_all_vehicles_usecase import GetAllVehiclesUsecase

from .formatter.formatter_responses import format_vehicles_response
from ..middleware.auth_middleware import auth_middleware

vehicles_route = Blueprint('vehicles_route', __name__)


@vehicles_route.post("/vehicle/join/person")
@auth_middleware
async def join_vehicle_to_person(_: str):
    """join cars to a person"""
    vehicle_controller = VehicleController()
    handler = await vehicle_controller.handler(request)
    return handler


@vehicles_route.get("/vehicles")
@auth_middleware
async def get_all_vehicles(_: str):
    """get all vehicles related to persons"""
    vehicles_repository = VehiclesRepository()
    get_vehicles_usecase = GetAllVehiclesUsecase(vehicles_repository)
    vehicles = await get_vehicles_usecase.execute()

    vehicles_formatter = format_vehicles_response(vehicles)

    return jsonify({"vehicles": vehicles_formatter})


@vehicles_route.get("/vehicles/<string:person_id>")
@auth_middleware
async def get_vehicle_by_person(_:str, person_id: str):
    """get all vehicles related to persons"""
    vehicles_repository = VehiclesRepository()
    vehicle_by_person = GetVehiclesByPerson(vehicles_repository)
    vehicles = await vehicle_by_person.execute(person_id)

    vehicles_formatter = format_vehicles_response(vehicles)

    return jsonify({"vehicles": vehicles_formatter})
