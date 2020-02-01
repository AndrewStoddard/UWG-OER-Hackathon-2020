import os
from typing import Tuple
from urllib.parse import unquote
from web.WebGenerator import WebGenerator


class QueryHandler:

    def __init__(self):
        self.__web_generator = WebGenerator()
        self.__encoding = "UTF-8"

    def handle_get_request(self, request: str) -> Tuple[str, bytes]:
        if request == "/style.css":
            return 'text/css', read_file_bytes("/" + "style.css")
        else:
            return 'text/html', self.__handle_index_request()

    def __handle_index_request(self) -> bytes:
        return bytes(self.__web_generator.generate_index(), self.__encoding)

    def handle_post_request(self, request: str, post_data: str) -> Tuple[str, bytes]:
        return 'text/html', self.__handle_index_request()

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
