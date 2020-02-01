from typing import Dict, List
from Resource import Resource
from DatabaseManager import DatabaseManager

class ResourceManager:
    def __init__(self):
        self.__database_manager = DatabaseManager("test.db")
        self.__resource_list = self.__database_manager.get_all_resources()

    def add_resource(self, resourceData: Dict):
        new_resource = Resource(
            self.__database_manager.get_next_resource_id(),
            resourceData["title"], 
            resourceData["link"], 
            author=resourceData["author"], 
            subject=resourceData["subject"], 
            resource_type=Resource.Type(resourceData["type"]), 
            isbn=resourceData["isbn"])
        self.__resource_list.append(new_resource)
        self.__database_manager.add_resource(new_resource)

    def get_all_resources(self):
        return self.__resource_list

    def search(self, subject: str) -> List[Resource]:
        new_resources = []
        for resource in self.__resource_list:
            if resource.subject == subject:
                new_resources.append(resource)
        return new_resources