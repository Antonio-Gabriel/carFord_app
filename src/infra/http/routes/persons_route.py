from flask import request
from flask import Blueprint, jsonify

from src.infra.repositories.persons_repository import PersonsRepository

# Controllers
from src.infra.controllers.create_persons_controller import CreatePersonsController
from src.infra.controllers.update_persons_controller import UpdatePersonsController
from src.infra.controllers.authentication_controller import AuthenticationController

# usecases
from src.application.usecases.person.get_all_persons_usecase import GetAllPersonsUsecase

from .formatter.formatter_responses import format_persons_response
from ..middleware.auth_middleware import auth_middleware

persons_route = Blueprint('persons_route', __name__)


@persons_route.post('/auth')
async def auth():
    """authentication"""
    auth_controller = AuthenticationController()
    handler = await auth_controller.handler(request)
    return handler


@persons_route.get('/persons')
@auth_middleware
async def get_persons(_: str):
    """get all persons"""
    persons_repository = PersonsRepository()
    get_persons_usecase = GetAllPersonsUsecase(persons_repository)
    persons = await get_persons_usecase.execute()

    persons_formatter = format_persons_response(persons)

    return jsonify({"persons": persons_formatter})


@persons_route.post('/persons/create')
@auth_middleware
async def create_person(_: str):
    """create person endpoint"""
    create_person_controller = CreatePersonsController()
    handler = await create_person_controller.handler(request)
    return handler


@persons_route.put('/persons/update/<string:_id>')
@auth_middleware
async def update_person(_:str, _id: str):
    """update person endpoint"""
    update_person_controller = UpdatePersonsController()
    handler = await update_person_controller.handler(request, _id)
    return handler
