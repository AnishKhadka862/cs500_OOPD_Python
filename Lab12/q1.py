from __future__ import annotations
from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self, content: str, attributes: dict[str, str]) -> None:
        self.__content = content
        self.__attributes = attributes
        self.__children: list[Node] = []
        
    def append_child(self, child: Node) -> None:
        self.__children.append(child)
        
    def html(self) -> str:
        output = "<" + self.createTag()
        for k, v in self.attributes.items():
            output += ' ' + k + '="' + v + '"'
        output += ">"
        output += self.content
        
        for child in self.children:
            output += child.html()
            
        output += "</" + self.createTag() + ">"
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
    

class Div(Node):
    def createTag(self) -> str:
        return "div"

    def html(self) -> str:
        output = "<div"
        
        for k, v in self.attributes.items():
            output += ' ' + k + '="' + v + '"'
        output += ">"
        
        for child in self.children:
            output += child.html()
        
        output += self.content
        output += "</div>"
        return output

class B(Node):
    def createTag(self) -> str:
        return "b"
    
class Body(Node):
    def createTag(self) -> str:
        return "body"

class Title(Node):
    def createTag(self) -> str:
        return "title"

class Head(Node):
    def createTag(self) -> str:
        return "head"
    
class Html(Node):
    def createTag(self) -> str:
        return "html"
    
    def html(self) -> str:
        output = "<!DOCTYPE html>" + super().html()
        return output
        

def main():
    divAtts = {}
    divAtts['id'] = 'first'
    divAtts['class'] = 'foo'
    divA = Div('This is a test A', divAtts)
    divAtts = {}
    divAtts['id'] = 'second'
    divAtts['class'] = 'bar'
    divB = Div('This is a test B', divAtts)
    divAtts = {}
    divAtts['id'] = 'third'
    divAtts['class'] = 'dump'
    divC = Div('This is a test C', divAtts)

    b = B('This is a simple HTML file', {})
    divC.append_child(b)
    body = Body('', {})
    body.append_child(divA)
    body.append_child(divB)
    body.append_child(divC)
    title = Title('Example', {})
    head = Head('', {})
    head.append_child(title)
    htmlAtts = {}
    htmlAtts['lang'] = 'en'
    html = Html('', htmlAtts)
    html.append_child(head)
    html.append_child(body)
    print(html.html())
    
    
if __name__ == "__main__":
    main()
