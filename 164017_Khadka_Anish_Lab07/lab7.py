# Anish Khadka
# 164017
# Lab 07 - Academic Record System
class Student:
    def __init__(self, student_id: int, name: str, program: str)->None:
        self.__student_id: int=student_id
        self.__name: str=name
        self.__program: str=program
        self.__scores: list[Score]=[]
    @property
    def student_id(self)->int:
        return self.__student_id
    @property
    def name(self)->str:
        return self.__name

    @property
    def program(self)->str:
        return self.__program

    def add_score(self, score: 'Score')->None:
        self.__scores.append(score)

    def get_all_scores(self)->list['Score']:
        return self.__scores


class Course:
    def __init__(self, course_code: str, course_name: str, instructor_name: str)->None:
        self.__course_code: str=course_code
        self.__course_name: str=course_name
        self.__instructor_name: str=instructor_name
    @property
    def course_code(self)->str:
        return self.__course_code
    @property
    def course_name(self)->str:
        return self.__course_name

    @property
    def instructor_name(self)->str:
        return self.__instructor_name


class Score:
    def __init__(self, student: Student, course: Course, marks: list[int])->None:
        self.__student: Student=student
        self.__course: Course=course
        self.__marks: list[int]=marks

    @property
    def student(self)->Student:
        return self.__student
    @property
    def course(self)->Course:
        return self.__course
    @property
    def marks(self)->list[int]:
        return self.__marks

    def average_score(self)->float:
        if not self.__marks:
            return 0.0
        total: int=0
        for mark in self.__marks:
            total += mark
        return total / len(self.__marks)

    def highest_score(self)->int:
        if not self.__marks:
            return 0
        high: int=self.__marks[0]
        for mark in self.__marks:
            if mark > high:
                high=mark
        return high
class AcademicRecordSystem:
    def __init__(self)->None:
        self.__students: list[Student]=[]
        self.__courses: list[Course]=[]
        self.__scores: list[Score]=[]

    def add_student(self, student_id: int, name: str, program: str)->None:
        self.__students.append(Student(student_id, name, program))

    def add_course(self, course_code: str, course_name: str, instructor_name: str)->None:
        self.__courses.append(Course(course_code, course_name, instructor_name))

    def add_score(self, student_id: int, course_code: str, marks: list[int])->None:
        student: Student | None=None
        for s in self.__students:
            if s.student_id==student_id:
                student=s
                break

        course: Course | None=None
        for c in self.__courses:
            if c.course_code==course_code:
                course=c
                break
        if student is not None and course is not None:
            score: Score=Score(student, course, marks)
            self.__scores.append(score)
            student.add_score(score)

    def view_all_students(self)->None:
        if not self.__students:
            print("No students in the system.")
            return
        for student in self.__students:
            print()
            print("Student ID:", student.student_id)
            print("Name:", student.name)
            print("Program:", student.program)
            print("Scores:")
            student_scores: list[Score]=student.get_all_scores()
            if not student_scores:
                print("No scores recorded.")
            else:
                for sc in student_scores:
                    print("  Course:", sc.course.course_code, "Marks: ", sc.marks)

    def calculate_highest_score(self, course_code: str)->int:
        highest: int=0
        for score in self.__scores:
            if score.course.course_code==course_code:
                h: int=score.highest_score()
                if h > highest:
                    highest=h
        return highest

    def calculate_average_score(self, course_code: str)->float:
        total_avg: float=0.0
        count: int=0
        for score in self.__scores:
            if score.course.course_code==course_code:
                total_avg += score.average_score()
                count += 1
        if count==0:
            return 0.0
        return total_avg / count
    
    def display_course_statistics(self, course_code: str)->None:
        highest: int=self.calculate_highest_score(course_code)
        average: float=self.calculate_average_score(course_code)
        print(f"\nCourse: {course_code}")
        print(f"Highest Score: {highest}")
        print(f"Average Score: {average:.2f}")
    
    def get_student_total_marks_list(self, student_id: int) -> dict[str, list[int]]:
        student: Student | None = None
        for s in self.__students:
            if s.student_id == student_id:
                student = s
                break

        if student is None:
            return {}
        total_marks_list: dict[str, list[int]] = {}
        for score in student.get_all_scores():
            course_code: str = score.course.course_code
            marks: list[int] = score.marks
            total_marks_list[course_code] = marks
        return total_marks_list
def parse_marks(marks_str: str)->list[int]:
    marks: list[int]=[]
    current: str=""
    for ch in marks_str + " ":
        if ch==" ":
            if current != "":
                num: int=int(current)
                marks.append(num)
                current=""
        else:
            current += ch
    return marks

def main():
    system = AcademicRecordSystem()

    system.add_student(101, "Anish Khadka", "Computer Science")
    system.add_student(102, "Leo Messi", "Computer Science")
    system.add_student(103, "Luis Suarez", "Computer Science")

    system.add_course("C101", "Mathematics", "Dr. Smith")
    system.add_course("C102", "Physics", "Dr. Johnson")
    system.add_course("C103", "English", "Dr. Williams")

    system.add_score(101, "C101", [88])
    system.add_score(101, "C102", [92])
    system.add_score(101, "C103", [85])

    system.add_score(102, "C101", [75])
    system.add_score(102, "C102", [81])
    system.add_score(102, "C103", [78])

    system.add_score(103, "C101", [91])
    system.add_score(103, "C102", [87])
    system.add_score(103, "C103", [90])

    print("\n=== Students and Scores ===")
    system.view_all_students()

    print("\n=== Statistics ===")
    system.display_course_statistics("C101")
    system.display_course_statistics("C102")
    system.display_course_statistics("C103")

    while True:
        print("\n====Academic Record System====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enter Student Score")
        print("4. View All Students and Scores")
        print("5. Calculate Highest Score for a Course")
        print("6. Calculate Average Score for a Course")
        print("7. View specific Student's Total Marks List")
        print("8. Exit")
        choice: str=input("Enter your choice: ")
        if choice=="1":
            student_id: int=int(input("Enter student ID: "))
            name: str=input("Enter student name: ")
            program: str=input("Enter program name: ")
            system.add_student(student_id, name, program)
            print("Student added successfully.")
        elif choice=="2":
            course_code: str=input("Enter course code: ")
            course_name: str=input("Enter course name: ")
            instructor_name: str=input("Enter instructor name: ")
            system.add_course(course_code, course_name, instructor_name)
            print("Course added successfully.")
        elif choice=="3":
            student_id: int=int(input("Enter student ID: "))
            course_code: str=input("Enter course code: ")
            marks_input: str=input("Enter marks separated by spaces: ")
            marks: list[int]=parse_marks(marks_input)
            system.add_score(student_id, course_code, marks)
            print("Score added successfully.")
        elif choice=="4":
            system.view_all_students()

        elif choice=="5":
            course_code: str=input("Enter course code: ")
            highest: int=system.calculate_highest_score(course_code)
            print(f"\nHighest Score for course {course_code} is {highest}")

        elif choice=="6":
            course_code: str=input("Enter course code: ")
            average: float=system.calculate_average_score(course_code)
            print(f"\nAverage Score for course {course_code} is {average:.2f}")
        elif choice == "7":
            student_id: int = int(input("Enter student ID: "))
            marks_list = system.get_student_total_marks_list(student_id)
            if not marks_list:
                print(f"No record found for student ID {student_id}")
            else:
                print(f"\nTranscript for Student ID {student_id}:")
                for course, marks in marks_list.items():
                    print(f"  {course}: {marks}")
        elif choice=="8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__=="__main__":
    main()