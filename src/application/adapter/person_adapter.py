from ...domain.entities.person import Person, PersonProps


class PersonAdapter:
    """person adapter"""
    @staticmethod
    def create(name: str, email: str, is_admin: bool = False, _id: str | None = None) -> Person:
        """create an adapter to person"""
        return Person(PersonProps(
            name=name,
            email=email,
            is_admin=is_admin,
        ), _id)
    