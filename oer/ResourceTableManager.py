import sqlite3
from typing import List, Tuple
from Resource import Resource


class ResourceTableManager:

    def __init__(self, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
        self.__conn = connection
        self.__cursor = cursor

    def create_table(self):
        self.__cursor.execute("""CREATE TABLE resourcedata (
                        id integer,
                        title text,
                        link text,
                        author text,
                        subject text,
                        type text,
                        isbn text
                    )""")

    def add_resource(self, resource: Resource):
        self.__cursor.execute("INSERT INTO resourcedata VALUES (?, ?, ?, ?, ?, ?, ?)",
                              (resource.id, resource.title, resource.link, resource.author, resource.subject, resource.type.value, resource.isbn))

    def find_resource(self, id: str) -> Resource:
        return create_resource(self.__cursor.execute("SELECT * FROM resourcedata WHERE id=?", (id,)).fetchone())


    def get_all_resources(self) -> List[Resource]:
        resource_list = []
        for resource_data in self.__cursor.execute("SELECT * FROM resourcedata").fetchall():
            resource_list.append(create_resource(resource_data))
        return resource_list
    
    def get_next_id(self) -> int:
        return len(self.__cursor.execute("SELECT * FROM resourcedata").fetchall()) + 1

def create_resource(resource_data: Tuple[str, str, str, str, str, str, str]) -> Resource:
    return Resource(int(resource_data[0]), resource_data[1], resource_data[2], 
        author=resource_data[3], subject=resource_data[4], resource_type=Resource.Type(resource_data[5]), isbn=resource_data[6])
