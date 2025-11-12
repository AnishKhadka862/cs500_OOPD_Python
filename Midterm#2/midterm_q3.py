# Anish Khadka
# 164017
# Midterm Question 3

""""
Following the question 2, add the followings:
ConstructionCompanyType Enum
ConstructionCompany class
find_largest_building(building) -> Optional[Building]
get_building_by_type() -> dict[BuildingType,list[Building]
assign_employee_to_building(employee_id, building_type) -> None
Note that the same employee can be assigned to one or more buildings
Additionally, include a method in the ConstructionCompany class that returns a list of buildings assigned to a specified employee.
find_employee_buildings(employee_id) -> list[Building]:
Enhance your main method to test all these new functions
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional

# Abstract base class
class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass


# Enum for BuildingType
class BuildingType(Enum):
    MANUFACTURING_BUILDING = "Manufacturing Building"
    WAREHOUSE = "Warehouse"
    DISTRIBUTION_CENTER = "Distribution Center"
    FLEX_SPACE = "Flex Space"


# Employee class
class Employee(Displayable):
    def __init__(self, employee_id: int, employee_name: str, annual_income: float):
        self._employee_id = employee_id
        self._employee_name = employee_name
        self._annual_income = annual_income

    # Public properties
    @property
    def employee_id(self):
        return self._employee_id

    @property
    def employee_name(self):
        return self._employee_name

    @property
    def annual_income(self):
        return self._annual_income

    def __str__(self):
        return f"Employee[ID= {self._employee_id}, Name= {self._employee_name}, Income= ${self._annual_income}]"

    def display(self):
        print(self.__str__())


# Company class
class Company(Displayable):
    def __init__(self, company_name: str):
        self._company_name = company_name
        self._employees = []

    @property
    def company_name(self):
        return self._company_name

    @property
    def employees(self):
        return self._employees

    def add_employee(self, employee: Employee):
        self._employees.append(employee)
        
    def get_employee(self, employee_id: int):
        for emp in self._employees:
            if emp.employee_id == employee_id:
                return emp
        return None
    
    def get_top_five_employees(self) -> list[Employee]:
        top_five = []  # List to hold top five employees
        for emp in self._employees:
            inserted = False
            index = 0
            while index < len(top_five):
                # Insert in sorted order
                if emp.annual_income > top_five[index].annual_income:
                    top_five.insert(index, emp)
                    inserted = True
                    break
                index += 1
            if not inserted:
                # Append to the end if not inserted yet
                top_five.append(emp)
            if len(top_five) > 5:
                top_five.pop()  # keep only 5
        return top_five

    def __str__(self):
        return f"Company[Name= {self._company_name}, Employees= {len(self._employees)}]"

    def display(self):
        print(self.__str__())
        for emp in self._employees:
            emp.display()


# Building class
class Building(Displayable):
    def __init__(self, building_name: str, area: float, stories: int, btype: BuildingType):
        self._building_name = building_name
        self._area = area
        self._stories = stories
        self._type = btype
        self._employees = []

    @property
    def building_name(self):
        return self._building_name

    @property
    def area(self):
        return self._area

    @property
    def stories(self):
        return self._stories

    @property
    def type(self):
        return self._type

    @property
    def employees(self):
        return self._employees

    def add_employee(self, employee: Employee):
        self._employees.append(employee)
        
    def remove_employee(self, employee_name: str):
        i = 0
        while i < len(self._employees):
            if self._employees[i].employee_name == employee_name:
                self._employees[i] = self._employees[-1]
                self._employees.pop()
            else:
                i += 1

    def __str__(self):
        return f"Building[Name= {self._building_name}, Area= {self._area} sqft, Stories={self._stories}, Type={self._type.value}]"

    def display(self):
        print(self.__str__())
        for emp in self._employees:
            emp.display()


# Enum for ConstructionCompanyType
class ConstructionCompanyType(Enum):
    GENERAL_CONTRACTOR = "General Contractor"
    SUBCONTRACTOR = "Subcontractor"
    CONSTRUCTION_MANAGER = "Construction Manager"


# ConstructionCompany class
class ConstructionCompany(Displayable):
    def __init__(self, category: ConstructionCompanyType):
        self._category = category
        self._buildings = []

    @property
    def category(self):
        return self._category

    @property
    def buildings(self):
        return self._buildings

    def add_building(self, building: Building):
        self._buildings.append(building)

    def find_largest_building(self) -> Building | None:
        if not self._buildings:
            return None
        largest = self._buildings[0]
        for b in self._buildings:
            if b.area > largest.area:
                largest = b
        return largest

    def get_building_by_type(self) -> dict[BuildingType, list[Building]]:
        result = {}
        for b in self._buildings:
            if b.type not in result:
                result[b.type] = []
            result[b.type].append(b)
        return result

    def assign_employee_to_building(self, employee_id: int, building_type: BuildingType, company: Company):
        emp = company.get_employee(employee_id)
        if not emp:
            print(f"Employee ID {employee_id} not found in company.")
            return
        for b in self._buildings:
            if b.type == building_type:
                b.add_employee(emp)

    def find_employee_buildings(self, employee_id: int) -> list[Building]:
        assigned = []
        for b in self._buildings:
            for emp in b.employees:
                if emp.employee_id == employee_id:
                    assigned.append(b)
                    break
        return assigned

    def __str__(self):
        return f"ConstructionCompany[Category= {self._category.value}, Buildings= {len(self._buildings)}]"

    def display(self):
        print(self.__str__())
        for b in self._buildings:
            b.display()


# Main method to test
def main():
    # Create Employees
    emp1 = Employee(1, "Anish", 50000)
    emp2 = Employee(2, "Khadka", 60000)
    emp3 = Employee(3, "Python", 75000)
    emp4 = Employee(4, "Mid", 90000)
    emp5 = Employee(5, "Term", 80000)
    emp6 = Employee(6, "Anish", 50000)  # duplicate name for removal test

    # Create a Company and add employees
    company = Company("Python Lab")
    for emp in [emp1, emp2, emp3, emp4, emp5, emp6]:
        company.add_employee(emp)

    # --- Company Tests ---
    print("\n--- Company Information ---")
    company.display()

    print("\nGet employee with ID=3:")
    found_emp = company.get_employee(3)
    if found_emp:
        print(found_emp)
    else:
        print("Employee not found.")

    print("\nTop 5 Employees by Income:")
    for emp in company.get_top_five_employees():
        print(emp)

    # --- Building Tests ---
    building = Building("Headquarter", 5000.0, 3, BuildingType.FLEX_SPACE)
    building.add_employee(emp1)
    building.add_employee(emp2)
    building.add_employee(emp3)
    building.add_employee(emp6)

    print("\n--- Building Information (before removal) ---")
    building.display()

    print("\nRemoving employees named 'Anish' from Building...")
    building.remove_employee("Anish")

    print("\n--- Building Information (after removal) ---")
    building.display()

    # --- ConstructionCompany Tests ---
    # Create Buildings
    b1 = Building("ManufacturingPlant", 12000.0, 2, BuildingType.MANUFACTURING_BUILDING)
    b2 = Building("Warehouse A", 8000.0, 1, BuildingType.WAREHOUSE)
    b3 = Building("Distribution Hub", 15000.0, 4, BuildingType.DISTRIBUTION_CENTER)
    b4 = Building("Flex Tower", 5000.0, 3, BuildingType.FLEX_SPACE)

    # Create Construction Company
    ccompany = ConstructionCompany(ConstructionCompanyType.GENERAL_CONTRACTOR)
    for b in [b1, b2, b3, b4]:
        ccompany.add_building(b)

    print("\n--- Construction Company Info ---")
    ccompany.display()

    print("\nLargest Building:")
    largest = ccompany.find_largest_building()
    if largest:
        print(largest)

    print("\nBuildings grouped by type:")
    grouped = ccompany.get_building_by_type()
    for btype, blist in grouped.items():
        print(f"{btype.value}: {[b.building_name for b in blist]}")

    print("\nAssign employee ID=3 (Python) to all WAREHOUSE buildings...")
    ccompany.assign_employee_to_building(3, BuildingType.WAREHOUSE, company)

    print("\nAssign employee ID=4 (Mid) to all FLEX_SPACE buildings...")
    ccompany.assign_employee_to_building(4, BuildingType.FLEX_SPACE, company)

    print("\nBuildings assigned to employee ID=3:")
    buildings_for_emp3 = ccompany.find_employee_buildings(3)
    for b in buildings_for_emp3:
        print(b)

    print("\nBuildings assigned to employee ID=4:")
    buildings_for_emp4 = ccompany.find_employee_buildings(4)
    for b in buildings_for_emp4:
        print(b)
        
if __name__ == "__main__":
    main()

