#lab4q3.py
# Employee Management System

# Employee class
class Employee:
    """Represents an employee with basic information."""

    def __init__(self, name: str, emp_id: str, department: str, age: int):
        self._name = name
        self._emp_id = emp_id
        self._department = department
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def emp_id(self):
        return self._emp_id

    @property
    def department(self):
        return self._department

    @property
    def age(self):
        return self._age

    def __repr__(self):
        return f"Employee(Name: {self._name}, ID: {self._emp_id}, Dept: {self._department}, Age: {self._age})"

    def __str__(self):
        return f"{self._name} | ID: {self._emp_id} | Dept: {self._department} | Age: {self._age}"


# Company class
class Company:
    """Represents a company that manages employees."""

    def __init__(self, name: str):
        self._name = name
        self._employees = []

    def add_employee(self, employee: Employee):
        """Add a new employee to the company."""
        self._employees.append(employee)

    def display_all_employees(self):
        """Display all employees in the company."""
        if not self._employees:
            print("No employees in the company yet.")
        else:
            print(f"\nEmployees at {self._name}:")
            for emp in self._employees:
                print(emp)

    def search_employee(self, name: str):
        """Search for an employee by name."""
        for emp in self._employees:
            if emp.name.lower() == name.lower():
                return emp
        return None


# Main menu
def main():
    company = Company("TechCorp")

    while True:
        print("\n--- Employee Management Menu ---")
        print("e - Enter a new employee's information")
        print("a - Display all employees information")
        print("d - Display an employee's information")
        print("q - Quit")

        choice = input("Choose an option: ").lower()

        if choice == "e":
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            department = input("Enter department: ")
            age = int(input("Enter age: "))
            new_emp = Employee(name, emp_id, department, age)
            company.add_employee(new_emp)
            print(f"Employee {name} added successfully!")

        elif choice == "a":
            company.display_all_employees()

        elif choice == "d":
            name = input("Enter part of the employee's name to search: ")
            results = company.search_employee(name)
            if results:
                print("Employee(s) found:")
                for emp in results:
                    print(emp)
            else:
                print("Employee not found.")
                add_new = input("Would you like to add this employee? (y/n): ").lower()
                if add_new == "y":
                    emp_id = input("Enter employee ID: ")
                    department = input("Enter department: ")
                    age = int(input("Enter age: "))
                    new_emp = Employee(name, emp_id, department, age)
                    company.add_employee(new_emp)
                    print(f"Employee {name} added successfully!")

        elif choice == "q":
            print("Exiting program!!!")
            break

        else:
            print("Invalid option. Please try again.")


# Run the program
if __name__ == "__main__":
    main()