# pylint: disable=E1101,W0703
from flask import request, make_response, jsonify
from src.infra.repositories.persons_repository import PersonsRepository
from src.application.usecases.person.edit_person_usecase import EditPersonUsecase


class UpdatePersonsController:
    """persons controller"""

    async def handler(self, req: request, _id: str):
        """handler controller"""

        person_body = req.get_json()

        person_repository = PersonsRepository()
        person_usecase = EditPersonUsecase(person_repository)

        try:
            result = await person_usecase.execute(_id,
                                                  person_body.get('name'))
            return jsonify({
                "msg": "person updated",
                "person": {
                    "id": result[0].id,
                    "name": person_body.get('name'),
                    "email": result[0].email,
                }})
        except Exception as ex:
            return make_response(
                {"error": {
                    "message": str(ex)
                }},
                400,
            )
