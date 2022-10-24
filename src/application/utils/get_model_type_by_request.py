# pylint: disable=E1101,W0703,W0212
from src.domain.enums import Model


def get_model_type_by_request(model: str):
    """resolve model enum"""

    models: dict = {
        Model.HATCH._value_ : Model.HATCH._value_,
        Model.SEDAN._value_ : Model.SEDAN._value_,
        Model.CONVERTIBLE._value_ : Model.CONVERTIBLE._value_
    }

    return models.get(model, None)
