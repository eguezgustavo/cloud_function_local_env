import typing

from ._domain import Person
from ._infrastructure import CSVPeopleRepository
from ._application import AddPersonUseCase


def add_user(name: str, last_name: str) -> typing.List[Person]:
    repository = CSVPeopleRepository()
    use_case = AddPersonUseCase(repository)
    return use_case.insert_a_person_and_read_all_people(name, last_name)
