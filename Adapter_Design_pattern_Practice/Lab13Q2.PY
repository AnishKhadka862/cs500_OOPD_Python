# Lab13Q2.py
# Adapter Design Pattern Example for Shape Area and Perimeter Calculation
class LegacyRectangle:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        
    def get_width(self) -> int:
        return self.__width
    
    def get_height(self) -> int:
        return self.__height        
    
class ModernShape:
    def __init__(self, area: int, perimeter: int) -> None:
        self.__area = area
        self.__perimeter = perimeter

    def get_area(self) -> int:
        return self.__area

    def get_perimeter(self) -> int:
        return self.__perimeter
        
class RectangleAdapter(ModernShape):
    def __init__(self, obj: LegacyRectangle) -> None:
        self.__obj = obj
        
    def get_area(self) -> int:
        return self.__obj.get_width() * self.__obj.get_height()
    
    def get_perimeter(self) -> int:
        return 2 * (self.__obj.get_width() + self.__obj.get_height())
    
class ShapeFactory:
    @staticmethod
    def get_shape() -> ModernShape:
        #return ModernShape(100, 40)  # Using factory to return modern shape
        return RectangleAdapter(LegacyRectangle(10, 10))  # Using adapter to return adapted shape
    
def main():
    shape = ShapeFactory.get_shape()
    print(shape.get_area())          # Should print area
    print(shape.get_perimeter())  # Should print perimeter
    
if __name__ == "__main__":
    main()

        
        
        