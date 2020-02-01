from enum import Enum

class Resource:
    def __init__(self, resource_id: int, title: str, link: str, resource_type = None, author: str = None, subject: str = None, isbn: str = None):
        self.id = resource_id
        self.title = title
        self.link = link
        self.author = author
        self.subject = subject
        if resource_type == None:
            self.type = self.Type.OTHER
        else:
            self.type = resource_type
        self.isbn = isbn

    class Type(Enum):
        ARTICLE = "Article"
        TEXT_BOOK = "Text Book"
        JOURNAL = "Journal"
        CASE_STUDY = "Case Study"
        OTHER = "Other"

    def __repr__(self):
        return str(self.id) + " " + str(self.title) + " "+ str(self.link) + " "+ str(self.author) + " "+ str(self.subject) + " "+ str(self.type) + " "+ str(self.isbn) + " "
