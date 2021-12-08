import typing

from .. import entities


class PeopleRepository:
    def get_all(self) -> typing.List[entities.Person]:
        raise NotImplementedError()
    
    def create(self, name: str, last_name: str) -> entities.Person:
        raise NotImplementedError()
