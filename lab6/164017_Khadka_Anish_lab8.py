# Anish Khadka
# 164017
# oct 09 2025 7:03 pm
# 164017_Khadka_Anish_lab8.py

from abc import ABC, abstractmethod
from typing import List

# Abstract class
class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

# Abstract company class
class AbstractCompany(Displayable):
    _max_num_employees = 10  

    @abstractmethod
    def get_employee_name_list(self) -> List[str]:
        pass

# Employee class
class Employee(Displayable):
    def __init__(self, emp_id: int, name: str, salary: float) -> None:
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    @property
    def emp_id(self):
        return self.__emp_id

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    def display(self) -> None:
        print(f"Employee ID: {self.__emp_id}, Name: {self.__name}, Salary: {self.__salary}")

# Company class
class Company(AbstractCompany):
    def __init__(self, comp_name: str) -> None:
        self.__comp_name = comp_name
        self.__employees: List[Employee] = []

    @property
    def comp_name(self):
        return self.__comp_name

    @property
    def employees(self):
        return self.__employees

    def add_employee(self, employee: Employee) -> None:
        if len(self.__employees) < self._max_num_employees:
            self.__employees.append(employee)
        else:
            print("Maximum number of employees reached. Cannot add more.")

    def get_employee_name_list(self) -> List[str]:
        return [emp.name for emp in self.__employees]

    def display(self) -> None:
        print(f"Company Name: {self.__comp_name}")
        print(f"Number of Employees: {len(self.__employees)}")
        for emp in self.__employees:
            emp.display()

# TradingCompany class
class TradingCompany(Company):
    def __init__(self, comp_name: str, product_type: str, num_of_offices: int) -> None:
        super().__init__(comp_name)
        self.__product_type = product_type
        self.__num_of_offices = num_of_offices

    @property
    def product_type(self):
        return self.__product_type

    @property
    def num_of_offices(self):
        return self.__num_of_offices

    def get_employees_high_salary(self, bench_salary: float) -> List[Employee]:
        return [emp for emp in self.employees if emp.salary > bench_salary]

    def display(self) -> None:
        super().display()
        print(f"Product Type: {self.__product_type}")
        print(f"Number of Offices: {self.__num_of_offices}")

# Main function to test TradingCompany
def main():
    emp1 = Employee(1, "Anish", 50000)
    emp2 = Employee(2, "Khadka", 70000)
    emp3 = Employee(3, "Python", 500)

    trading_company = TradingCompany("PythonLab", "Software", 3)

    trading_company.add_employee(emp1)
    trading_company.add_employee(emp2)
    trading_company.add_employee(emp3)

    print("\nTrading Company Info:\n")
    trading_company.display()

    print("\nEmployee Names:\n")
    for name in trading_company.get_employee_name_list():
        print(name)

    print("\nEmployees with salary more than 4000:\n")
    for emp in trading_company.get_employees_high_salary(4000):
        emp.display()

if __name__ == "__main__":
    main()