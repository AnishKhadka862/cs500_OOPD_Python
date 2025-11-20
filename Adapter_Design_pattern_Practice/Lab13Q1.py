# Lab13Q1.py
# Adapter Design Pattern Example for Two Incompatible Systems
class FirstSystem:
    def foo(self, x: int) -> str:
        return str(x)
    
class SecondSystem:
    def bar(self, y: str) -> int:
        return int(y)

class Adapter(FirstSystem):
    def __init__(self, obj: SecondSystem) -> None:
        self.__obj = obj
        
    def foo(self, x: int) -> str:
        return str(self.__obj.bar(str(x)))
    
class Factory:
    @staticmethod
    def get_system() -> FirstSystem:
        #return FirstSystem() ; using factory to return adapter
        return Adapter(SecondSystem()) # using adapter to return adapted system
    
def main():
    System = Factory.get_system()
    print(System.foo(123))  # Should print "123"
    
if __name__ == "__main__":
    main()