from html_writer import Html
from typing import List, Dict
from Resource import Resource


class WebGenerator:
    def __init__(self):
        self.__head = Html()
        self.__body = Html()

    def __generate_html_header(self):
        self.__head.self_close_tag('meta', attributes=dict(charset='utf-8'))
        self.__head.tag_with_content("", name='title')
        self.__head.self_close_tag('link', attributes=dict(href="/style.css", rel="stylesheet", type="text/css"))
        with self.__head.tag('div', id_="header"):
            self.__head.self_close_tag('img', attributes=dict(src="images/word_logo.png"))
            with self.__head.tag('div', id_="nav"):
                with self.__head.tag('ul'): 
                    with self.__head.tag('li'):
                        self.__head.tag_with_content("Search", 'a', attributes=dict(href="/index.html"))
                    with self.__head.tag('li'):
                        self.__head.tag_with_content("All", 'a', attributes=dict(id="active", href="/all"))
                    with self.__head.tag('li'):
                        self.__head.tag_with_content("Add", 'a', attributes=dict(href="/add"))

    def generate_index(self, previous_search: str = "") -> str:
        self.__head = Html()
        self.__body = Html()
        self.__generate_html_header()
        self.__generate_body_header()
        self.__generate_index_search_form(previous_search)
        return Html.html_template(self.__head, self.__body).to_raw_html(indent_size=2)

    def __generate_body_header(self):
        pass

    def __generate_index_search_form(self, previous_search):
        pass

    def generate_resources_page(self, resources: List[Resource]):
        self.__head = Html()
        self.__body = Html()
        self.__generate_html_header()
        self.__generate_resources_body(resources)
        return Html.html_template(self.__head, self.__body).to_raw_html(indent_size=2)


    def __generate_resources_body(self, resources: List[Resource]):
        with self.__body.tag('div', id_='"results"'):
            for resource in resources:
                with self.__body.tag('div'):
                    self.__body.self_close_tag('img', attributes=dict(src="images/shield.png"))
                    self.__body.tag_with_content(resource.title, "h6")
                    self.__body.tag_with_content(resource.author, "h6")
                    self.__body.tag_with_content(resource.isbn, "h6")
                    self.__body.tag_with_content(resource.type.value, "h6")
                    self.__body.tag_with_content(resource.subject, "h6")


    def generate_add_page (self):
        self.__head = Html()
        self.__body = Html()
        self.__generate_html_header()

        self.__body.tag('div', id_='"buffer"')
        self.__generate_lib_logo()
        with self.__body.tag('div', id_='"form"'):
            with self.__body.tag('form', classes=["add-form"]):
                with self.__body.tag('div', id_='"title-div"'):
                    self.__body.self_close_tag('input', attributes=dict(id='"title-field"', type="text", placeholder="Title..."))
                with self.__body.tag('div', id_='"author-div"'):
                    self.__body.self_close_tag('input', attributes=dict(id='"author-field"', type="text", placeholder="Author..."))
                with self.__body.tag('div', id_='"isbn-div"'):
                    self.__body.self_close_tag('input', attributes=dict(id='"isbn-field"', type="text", placeholder="ISBN..."))
                with self.__body.tag('div', id_='"subject-div"'):
                    self.__body.self_close_tag('input', attributes=dict(id='"subject-field"', type="text", placeholder="Subject..."))
                with self.__body.tag('div', id_='"link-div"'):
                    self.__body.self_close_tag('input', attributes=dict(id='"link-field"', type="text", placeholder="Link..."))
                with self.__body.tag('div', id_='"type-div"'):
                    self.__body.tag('select', id_='"type-add-field"')
                with self.__body.tag('div', id_='"submit-div"'):
                    self.__body.tag_with_content("Add", 'button', attributes=dict(id='"add-submit"', type="button"))
        return Html.html_template(self.__head, self.__body).to_raw_html(indent_size=2)
    
    def __generate_lib_logo(self):
        with self.__body.tag('div', id_='"library-logo"'):
            self.__body.self_close_tag('img', attributes=dict(src="images/banner-ingram-library.png"))
    


if __name__ == '__main__':
    print(WebGenerator().generate_add_page())