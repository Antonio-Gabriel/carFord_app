#pylint: disable=W0702
from functools import wraps

import os
import jwt
from flask import request, jsonify


def auth_middleware(func):
    """authentication middleware"""
    @wraps(func)
    async def decotared(*args, **kwargs):
        """auth decorator"""

        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({
                "auth-error": {
                    "message": "Token is missing!!"
                }
            }), 401

        try:
            data = jwt.decode(token, os.getenv(
                'SECRET_KEY'), algorithms=["HS256"])                 
        except:
            return jsonify({
                "auth-error": {
                    "message": "Token is invalid!!!"
                }
            }), 401

        return await func(data, *args, **kwargs)

    return decotared
