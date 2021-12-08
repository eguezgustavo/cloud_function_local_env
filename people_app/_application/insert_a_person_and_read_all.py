import typing

from .. import _domain


class UseCase:
    def __init__(self, people_repository: _domain.PeopleRepository) -> None:
        self.people_repository = people_repository

    def insert_a_person_and_read_all_people(
        self, name: str, last_name: str
    ) -> typing.List[_domain.Person]:
        current_people = self.people_repository.get_all()
        created_user = self.people_repository.create(name, last_name)
        return [
            *current_people,
            created_user
        ]
