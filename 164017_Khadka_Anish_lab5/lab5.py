from typing import Optional


class Person:
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return f"name = {self.name}"

    def display(self) -> None:
        print(self)

    def dowork(self) -> None:
        print(f"Person {self.name} is doing nothing.")


class Programmer(Person):
    def __init__(self, name: str, skills: str, salary: float) -> None:
        super().__init__(name)
        self.__skills = skills
        self.__salary = salary

    @property
    def skills(self) -> str:
        return self.__skills

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, value: float) -> None:
        self.__salary = value

    def get_annual_income(self) -> float:
        return self.salary * 12

    def __str__(self) -> str:
        return f"name = {self.name}\nskills = {self.skills}\nsalary = {self.salary}"

    def display(self) -> None:
        print(self)

    def dowork(self) -> None:
        print(f"Programmer {self.name} is writing a program.")


class Manager(Programmer):
    def __init__(self, name: str, skills: str, salary: float, bonus: float) -> None:
        super().__init__(name, skills, salary)
        self.__bonus = bonus

    @property
    def bonus(self) -> float:
        return self.__bonus

    @bonus.setter
    def bonus(self, value: float) -> None:
        self.__bonus = value

    def get_annual_income(self) -> float:
        return (self.salary * 12) + self.bonus

    def __str__(self) -> str:
        return f"name = {self.name}\nskills = {self.skills}\nsalary = {self.salary}\nbonus = {self.bonus}"

    def display(self) -> None:
        print(self)

    def dowork(self) -> None:
        print(f"Manager {self.name} is supervising a team of programmers.")


class Project:
    def __init__(self, projname: str, budget: float = 0.0, active: bool = False) -> None:
        self.__projname = projname
        self.__budget = budget
        self.__active = active

    @property
    def projname(self) -> str:
        return self.__projname

    @property
    def budget(self) -> float:
        return self.__budget

    @property
    def active(self) -> bool:
        return self.__active

    def __str__(self) -> str:
        return f"projname = {self.projname}\nbudget = {self.budget}\nactive = {self.active}"

    def display(self) -> None:
        print(self)


class Group:
    def __init__(self, groupname: str) -> None:
        self.__groupname = groupname
        self.__members: list[Person] = []

    def add_member(self, member: Programmer) -> None:
        self.__members.append(member)

    def remove_member(self, name: str) -> None:
        self.__members = [m for m in self.__members if m.name != name]

    def ask_anyone_dowork(self) -> None:
        for m in self.__members:
            m.dowork()

    def ask_manager_dowork(self) -> None:
        for m in self.__members:
            if isinstance(m, Manager):
                m.dowork()

    def get_allMembers_morethan(self, income: float) -> list[Programmer]:
        return [m for m in self.__members if isinstance(m, Programmer) and m.get_annual_income() > income]

    def display(self) -> None:
        print("The group has these members:")
        for m in self.__members:
            m.display()


class ITGroup(Group):
    def __init__(self, groupname: str) -> None:
        super().__init__(groupname)
        self.__projects: list[Project] = []

    def add_project(self, project: Project) -> None:
        self.__projects.append(project)

    def find_largest_project(self) -> Optional[Project]:
        if not self.__projects:
            return None
        return max(self.__projects, key=lambda p: p.budget)

    def get_active_projects(self) -> list[Project]:
        return [p for p in self.__projects if p.active]

    def display(self) -> None:
        super().display()
        print("The group has these projects:")
        for p in self.__projects:
            p.display()


# === Testing with provided main() ===
def main() -> None:
    p1: Programmer = Programmer("Lily", "C++, Java", 10000)
    p2: Programmer = Programmer("Judy", "Python, Java", 18000)
    m: Manager = Manager("Peter", "Management", 20000, 20000)

    proj1: Project = Project("MAX-5", 200000, True)
    proj2: Project = Project("FOX-4", 100000, False)
    proj3: Project = Project("FOX-XP", 500000, True)

    itgrp: ITGroup = ITGroup("ATX Group")
    itgrp.add_member(p1)
    itgrp.add_member(p2)
    itgrp.add_member(m)

    itgrp.add_project(proj1)
    itgrp.add_project(proj2)
    itgrp.add_project(proj3)

    itgrp.display()

    p3: Programmer = Programmer("Jone", "Python, Java", 1118000)
    itgrp.add_member(p3)

    itgrp.ask_anyone_dowork()
    print()
    itgrp.ask_manager_dowork()

    print("\nGet the largest project...")
    maxProj: Optional[Project] = itgrp.find_largest_project()
    if maxProj is not None:
        maxProj.display()

    print("\nGet the acive projects...")
    projects: list[Project] = itgrp.get_active_projects()
    for proj in projects:
        proj.display()

    print()
    itgrp.display()

    itgrp.remove_member(p3.name)

    print("\nGet the members with high income...")
    members: list[Programmer] = itgrp.get_allMembers_morethan(200000)
    for member in members:
        member.display()
    print()


if __name__ == "__main__":
    main()
