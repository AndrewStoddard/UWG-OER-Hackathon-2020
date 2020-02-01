from html_writer import Html
from typing import List, Dict


class WebGenerator:
    def __init__(self):
        self.__head = Html()
        self.__body = Html()

    def __generate_html_header(self):
        self.__head.self_close_tag('meta', attributes=dict(charset='utf-8'))
        self.__head.tag_with_content("Photo Stack Testing...", name='title')
        self.__head.self_close_tag('link', attributes=dict(href="/style.css", rel="stylesheet", type="text/css"))

    def generate_index(self, previous_search: str = "") -> str:
        self.__head = Html()
        self.__body = Html()
        self.__generate_html_header()
        self.__generate_body_header()
        self.__generate_index_search_form(previous_search)
        return Html.html_template(self.__head, self.__body).to_raw_html(indent_size=2)

    def __generate_body_header(self):
        header_tag_type = 'h4'
        with self.__body.tag('div', id_='"header"'):
            with self.__body.tag('a',  attributes=dict(href="/?search=")):
                self.__body.tag_with_content("HEADER", header_tag_type)

    def __generate_index_search_form(self, previous_search):
        with self.__body.tag('div', id_='"search"'):
            with self.__body.tag('form', attributes=dict(action="")):
                self.__body.self_close_tag('input', attributes=dict(type="text", value=previous_search,
                                                                    placeholder="search...", name="search"))
                self.__body.tag_with_content("Search", 'button', attributes=dict(type="submit", text="search"))

if __name__ == '__main__':
    print(WebGenerator().generate_index())