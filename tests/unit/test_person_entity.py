from src.domain.entities.person import Person, PersonProps


def test_person_entity():
    """should be return email"""

    person = Person(PersonProps(
        name="António Gabriel",
        email="antoniogabriel@gmail.com",
        is_admin=1
    ))

    assert person.person_props.email == "antoniogabriel@gmail.com"


def test_person_validator():
    """should be return true"""

    person = Person(PersonProps(
        name="António Gabriel",
        email="antoniogabriel@gmail.com",
        is_admin=False
    ))

    result, err = person.validate()
    if err:
        print(err)

    assert result == True


def test_bad_person_validator():
    """should be return false"""

    person = Person(PersonProps(
        name="António Gabriel",
        email="antonio",
        is_admin="1"
    ))

    result, err = person.validate()
    if err:
        print(err)

    assert result == False
    assert len(err) == 2
