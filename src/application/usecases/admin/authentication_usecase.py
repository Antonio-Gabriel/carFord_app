from typing import Type
from datetime import datetime, timedelta

import os
import jwt

from flask import jsonify
from cerberus import Validator
from src.domain.validators.schemas.schemas import authentication_validator_schema

from ...security.password import check_password
from ...repositories.persons_repository import IPersonsRepository


class AuthenticationUsecase:
    """admin usecase"""

    def __init__(self, persons_repository: Type[IPersonsRepository]) -> None:
        self.__persons_repository = persons_repository

    async def execute(self, email: str, password: str):
        """create an admin"""

        validador = Validator()
        _ = validador.validate({
            "email": email,
            "password": password,
        }, authentication_validator_schema)

        if validador.errors:
            raise Exception(validador.errors, 400)

        admin = await self.__persons_repository\
            .sign_in_to_admin(
                email=email)

        if not admin:
            raise Exception("Could not verify", 401)

        if check_password(admin[1].password.encode('utf-8'), password.encode('utf-8')):
            token = jwt.encode({
                'usr': {
                    "person_id": admin[0].id,
                    "email": admin[0].email
                },
                'exp': datetime.utcnow() + timedelta(minutes=30)
            }, os.getenv('SECRET_KEY'))

            return jsonify({
                'msg': 'Authentication success',
                'token': token
            }), 201

        raise Exception('Invalid email or password', 401)
