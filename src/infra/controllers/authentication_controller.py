# pylint: disable=E1101,W0703,E1136
from flask import request, make_response
from src.infra.repositories.persons_repository import PersonsRepository

from src.application.usecases.admin.authentication_usecase import AuthenticationUsecase


class AuthenticationController:
    """authentication controller"""

    async def handler(self, req: request):
        """auth handler"""

        auth_body = req.get_json()

        person_repository = PersonsRepository()
        auth_usecase = AuthenticationUsecase(person_repository)

        try:
            result = await auth_usecase.execute(auth_body.get('email'),
                                                auth_body.get('password'))
            return result
        except Exception as ex:
            return make_response(
                {"error": {
                    "message": ex.args[0]
                }},
                int(ex.args[1])
            )
