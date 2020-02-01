import os
from typing import Tuple
from urllib.parse import unquote
from WebGenerator import WebGenerator
from ResourceManager import ResourceManager


class QueryHandler:

    def __init__(self):
        self.__web_generator = WebGenerator()
        self.__resource_manager = ResourceManager()
        self.__encoding = "UTF-8"

    def handle_get_request(self, request: str) -> Tuple[str, bytes]:
        if request == "/style.css":
            return 'text/css', read_file_bytes("/" + "style/style.css")
        if request.startswith("/images"):
            return '', read_file_bytes(request)
        if request == "/all":
            return 'text/html', self.__handle_resources_request()
        if request == "/add":
            return 'text/html', read_file_bytes("/add.html")
        else:
            return 'text/html', read_file_bytes("/index.html")

    def __handle_index_request(self) -> bytes:
        return bytes(self.__web_generator.generate_index(), self.__encoding)

    def __handle_resources_request(self) -> bytes:
        return bytes(self.__web_generator.generate_resources_page(self.__resource_manager.get_all_resources()), self.__encoding)

    def handle_post_request(self, request: str, post_data: str) -> Tuple[str, bytes]:
        if post_data.startswith("subject"):
            search_query = post_data.split("=")[1].split("&")[0]
            return 'text/html', self.__handle_search_request(search_query)
        else:
            vars = post_data.split("&")
            resource_data = {}
            for var in vars:
                var_data = var.split("=")
                resource_data[var_data[0]] = var_data[1].replace("+", " ")
            self.__resource_manager.add_resource(resource_data)
            return 'text/html', read_file_bytes("/add.html")

    def __handle_search_request(self, search_query: str) -> bytes:
        return bytes(self.__web_generator.generate_resources_page(self.__resource_manager.search(search_query)), self.__encoding)

def read_file_bytes(file_path: str) -> bytes:
    try:
        with open(os.getcwd() + file_path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(file_path + " not a file.")
        return None
    except IsADirectoryError:
        print(file_path + " is a dir.")
        return None

if __name__ == '__main__':
    QueryHandler()
