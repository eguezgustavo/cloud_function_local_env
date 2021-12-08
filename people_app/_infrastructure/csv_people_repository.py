import csv
import typing
import os

from .. import _domain

_CSV_FILENAME = '/tmp/people.csv'


class CSVPeopleRepository(_domain.PeopleRepository):
    def get_all(self) -> typing.List[_domain.Person]:
        self.__create_file_if_not_exists()
        with open(_CSV_FILENAME, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            return [
                _domain.Person(id=row[0], name=row[1], last_name=row[2])
                for row in csv_reader
            ]
    
    def create(self, name: str, last_name: str) -> _domain.Person:
        self.__create_file_if_not_exists()
        last_index = 0

        with open(_CSV_FILENAME, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                last_index = row[0]
        
        last_index = int(last_index) + 1

        with open(_CSV_FILENAME, 'a') as csv_file:
            csv_file.writelines([f'{last_index},{name},{last_name}'])
            return _domain.Person(
                id=last_index,
                name=name,
                last_name=last_name
            )

    def __create_file_if_not_exists(self):
        if not os.path.exists(_CSV_FILENAME):
            with open(_CSV_FILENAME, 'w') as csv_file:
                csv_file.write('')
