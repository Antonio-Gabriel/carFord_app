# pylint: disable=E1101,W0703,W0212
from src.domain.enums import Color


def get_color_type_by_request(color: str):
    """resolve color enum"""

    colors: dict = {
        Color.YELLOW._value_: Color.YELLOW._value_,
        Color.BLUE._value_  : Color.BLUE._value_,
        Color.GRAY._value_  : Color.GRAY._value_
    }

    return colors.get(color, None)

