person_validator_schema: dict = {
    "name": {
        "type": "string",
        "required": True,
        "min": 3,
    },
    "email": {
        "type": "string",
        "required": True,
        "regex": r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
    },
    "is_admin": {
        "type": "boolean",
    }
}

authentication_validator_schema: dict = {
    "email": {
        "type": "string",
        "required": True,
        "regex": r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
    },
    "password": {
        "type": "string",
        "required": True,
    }
}

vehicle_validator_schema: dict = {
    # "model": {
    #     "type": "string",
    #     "required": True,
    #     "allowed": ["hatch", "sedan", "convertible"]
    # },
    # "color": {
    #     "type": "string",
    #     "required": True,
    #     "allowed": ["yellow", "blue", "gray"]
    # },
    "person_id": {
        "type": "string",
        "required": True,
    }
}
