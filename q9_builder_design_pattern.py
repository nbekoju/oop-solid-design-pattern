# [Builder Design Pattern] Design a document generator using the Builder Design Pattern. Create a DocumentBuilder that creates documents of various types (e.g., PDF, HTML, Plain Text). Implement the builder methods to format the document content and structure according to the chosen type. Demonstrate how the Builder Design Pattern allows for the creation of different document formats without tightly coupling the document generation logic.


from abc import ABC, abstractmethod


class Document:
    def __init__(self) -> None:
        self.content = ""

    def add_content(self, content):
        self.content += content + "\n"


class DocumentBuilder(ABC):
    @abstractmethod
    def create_document(self):
        pass

    @abstractmethod
    def add_content(self):
        pass

    @abstractmethod
    def get_document(self):
        pass
