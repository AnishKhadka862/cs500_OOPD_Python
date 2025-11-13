# Anish Khadka
# 164017
# Lab 12 Question 2
from __future__ import annotations
from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self, content: str = "", attributes: dict[str, str] | None = None) -> None:
        self.__content = content
        self.__attributes = attributes if attributes is not None else {}
        self.__children: list[Node] = []

    def append_child(self, child: Node) -> None:
        self.__children.append(child)

    def html(self) -> str:
        output = "<" + self.createTag()
        for k, v in self.attributes.items():
            output += f' {k}="{v}"'
        output += ">"
        output += self.content
        for child in self.children:
            output += child.html()
        output += f"</{self.createTag()}>"
        return output

    @abstractmethod
    def createTag(self) -> str:
        pass

    @property
    def attributes(self) -> dict[str, str]:
        return self.__attributes

    @property
    def content(self) -> str:
        return self.__content

    @property
    def children(self) -> list[Node]:
        return self.__children


class Html(Node):
    def createTag(self) -> str:
        return "html"

    def html(self) -> str:
        return "<!DOCTYPE html>" + super().html()


class Head(Node):
    def createTag(self) -> str:
        return "head"


class Body(Node):
    def createTag(self) -> str:
        return "body"


class Title(Node):
    def createTag(self) -> str:
        return "title"


class Div(Node):
    def createTag(self) -> str:
        return "div"


class B(Node):
    def createTag(self) -> str:
        return "b"


# factory classes
class AbstractNodeFactory(ABC):
    @abstractmethod
    def makeNode(self, tag: str, content: str = "", attributes: dict[str, str] | None = None) -> Node:
        pass

# concrete factory to create standard HTML nodes
# instead of directly instantiating node classes, we use this factory to create nodes
class StandardNodeFactory(AbstractNodeFactory):
    def makeNode(self, tag: str, content: str = "", attributes: dict[str, str] | None = None) -> Node:
        tag = tag.lower()
        if tag == "html":
            return Html(content, attributes)
        elif tag == "head":
            return Head(content, attributes)
        elif tag == "body":
            return Body(content, attributes)
        elif tag == "title":
            return Title(content, attributes)
        elif tag == "div":
            return Div(content, attributes)
        elif tag == "b":
            return B(content, attributes)
        else:
            raise ValueError(f"Unknown tag type: {tag}")

# use of factory object to create HTML document
def main():
    factory = StandardNodeFactory()

    divAtts = {}
    divAtts['id'] = 'first'
    divAtts['class'] = 'foo'
    divA = factory.makeNode('div', 'This is a test A', divAtts)

    divAtts = {}
    divAtts['id'] = 'second'
    divAtts['class'] = 'bar'
    divB = factory.makeNode('div', 'This is a test B', divAtts)

    divAtts = {}
    divAtts['id'] = 'third'
    divAtts['class'] = 'dump'
    divC = factory.makeNode('div', 'This is a test C', divAtts)

    b = factory.makeNode('b', 'This is a simple HTML file')
    divC.append_child(b)

    body = factory.makeNode('body')
    body.append_child(divA)
    body.append_child(divB)
    body.append_child(divC)

    title = factory.makeNode('title', 'Example')
    head = factory.makeNode('head')
    head.append_child(title)

    htmlAtts = {}
    htmlAtts['lang'] = 'en'
    html = factory.makeNode('html', '', htmlAtts)
    html.append_child(head)
    html.append_child(body)

    print(html.html())


if __name__ == "__main__":
    main()