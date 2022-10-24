from uuid import uuid4


class Admin:
    """admin of carFord company"""

    def __init__(self, person_id: str, password: str, _id: str | None = None) -> None:
        self.person_id = person_id
        self.password = password
        self.__id = _id if _id is not None else str(uuid4())

    @property
    def get_id(self) -> str:
        """get person id"""
        return self.__id
