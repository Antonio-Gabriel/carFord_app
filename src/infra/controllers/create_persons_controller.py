# pylint: disable=E1101,W0703
from flask import request, make_response, jsonify
from src.infra.repositories.persons_repository import PersonsRepository
from src.application.usecases.person.create_person_usecase import CreatePersonUsecase


class CreatePersonsController:
    """persons controller"""

    async def handler(self, req: request):
        """handler controller"""

        person_body = req.get_json()

        person_repository = PersonsRepository()
        person_usecase = CreatePersonUsecase(person_repository)

        try:
            result = await person_usecase.execute(person_body.get('name'),
                                                  person_body.get('email'))
            return jsonify({"person": {
                "id": result.get_id,
                "name": result.person_props.name,
                "email": result.person_props.email,
            }})
        except Exception as ex:
            return make_response(
                {"error": {
                    "message": str(ex)
                }},
                400,
            )


# karolina.cardoso@advicehealth.com.br (enviar o github)
