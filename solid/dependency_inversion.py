"""
Abstractions should not depend upon details. Details should depend upon abstractions.
"""


# Bad approach. These 2 classes are dependant to each other. If we add method in backend get_data_from_other_db,
# we should also change frontend which violates the open-closed principle
from abc import ABC, abstractmethod


class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)


class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"


# good approach. we have separated the interfaces for getting data in
# frontend class by creating separate interface DataSource
class AFrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Database(DataSource):
    def get_data(self):
        return "Data from the database"


class API(DataSource):
    def get_data(self):
        return "Data from the API"
