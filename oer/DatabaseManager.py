import sqlite3
from sqlite3 import OperationalError
from typing import List, Dict
from Resource import Resource
from ResourceTableManager import ResourceTableManager

class DatabaseManager:

    def __init__(self, database_name: str):
        self.__conn = sqlite3.connect(database_name)
        self.__cursor = self.__conn.cursor()
        self.__resource_manager = ResourceTableManager(self.__conn, self.__cursor)
        self.__create_database()

    def __create_database(self):
        try:
            self.__resource_manager.create_table()
            self.__conn.commit()
        except OperationalError:
            pass

    def get_next_resource_id(self) -> int:
        return self.__resource_manager.get_next_id()

    def add_resource(self, resource: Resource):
        self.__resource_manager.add_resource(resource)
        self.__conn.commit()

    def get_all_resources(self) -> List[Resource]:
        return self.__resource_manager.get_all_resources()