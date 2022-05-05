import pytest
# from person.person import Person

@pytest.mark.skip
def test_creating_a_person():
    # given
    person = Person("Mark", "McNair")

    # then
    assert person.first_name == "Mark"
    assert person.last_name == "McNair"

@pytest.mark.skip
def test_person_full_name():
    person = Person("Mark", "McNair")

    assert person.full_name() == "Mark McNair"

@pytest.mark.skip
def test_person_formal_name():
    person = Person("Mark", "McNair")

    assert person.formal_name() == "McNair, Mark"
