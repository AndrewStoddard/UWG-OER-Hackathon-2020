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
            self.__head.tag_with_content("Name Place Holder", 'h1')

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
                    self.__body.tag_with_content(resource.title, "h2")
                    self.__body.tag_with_content(resource.author, "h4")
                    self.__body.tag_with_content(resource.isbn, "h6")
                    self.__body.tag_with_content(resource.type.value, "h6")
                    self.__body.tag_with_content(resource.subject, "h6")


    def generate_add_page (self):
        self.__head = Html()
        self.__body = Html()
        self.__generate_html_header()

        self.__body.tag('div', id_='"buffer"'):
        self.__generate_lib_logo()
        self.__body.tag('div', id_='"form"'):
            with self.__body.tag('form', classes=["add-form"])
                self.__body.tag('div', id='"title-div"')
                    with self.__body.self_close_tag('input', attributes=dict(id='"title-field"', type="text", placeholder="Title..."))
                self.__body.tag('div', id='"author-div"')
                    with self.__body.self_close_tag('input', attributes=dict(id='"author-field"', type="text", placeholder="Author..."))
                self.__body.tag('div', id='"isbn-div"')
                    with self.__body.self_close_tag('input', attributes=dict(id='"isbn-field"', type="text", placeholder="ISBN..."))
                self.__body.tag('div', id='"subject-div"')
                    with self.__body.self_close_tag('input', attributes=dict(id='"subject-field"', type="text", placeholder="Subject..."))
                self.__body.tag('div', id='"link-div"')
                    with self.__body.self_close_tag('input', attributes=dict(id='"link-field"', type="text", placeholder="Link..."))
                self.__body.tag('div', id='"type-div"')
                    with self.__body.tag('select', id='"type-add-field"')
                        # with self.__body.tag_with_content() TODO
                self.__body.tag('div', id='"submit-div"')
                    with self.__body.tag_with_content("Add", 'button', attributes=dict(id='"add-submit"', type="button")

              
    

    def __generate_lib_logo(self):
        with self.__body.tag('div', id_='"library-logo"')
            self.__body.self_close_tag('img', attributes=dict(src="images/banner-ingram-library.png"))
    


if __name__ == '__main__':
    print(WebGenerator().generate_index())