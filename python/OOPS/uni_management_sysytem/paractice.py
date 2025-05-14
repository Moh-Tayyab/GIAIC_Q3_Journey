from abc import ABC, abstractmethod

# ————————— Person Base Class —————————
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"


# ————————— Student Class —————————
class Student(Person):
    def __init__(self, name: str, age: int, roll_number: int):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.courses: list[str] = []

    def register_course(self, course_name: str) -> list[str]:
        self.courses.append(course_name)
        return self.courses


# ————————— Instructor Class —————————
class Instructor(Person):
    def __init__(self, name: str, age: int, salary: float, courses: list[str] = None):
        super().__init__(name, age)
        self.salary = salary
        self.courses: list[str] = courses or []

    def assign_course(self, course_name: str) -> list[str]:
        self.courses.append(course_name)
        return self.courses


# ————————— Course Class —————————
class Course:
    def __init__(
        self,
        course_id: int,
        name: str,
        instructors: list[Instructor] = None,
        students: list[Student] = None,
    ):
        self.id = course_id
        self.name = name
        # Use the passed lists (or default to empty)
        self.instructors: list[Instructor] = instructors or []
        self.students:   list[Student]    = students   or []

    def add_student(self, student: Student) -> list[Student]:
        self.students.append(student)
        return self.students

    def set_instructor(self, instructor: Instructor) -> list[Instructor]:
        self.instructors.append(instructor)
        return self.instructors


# ————————— Department Class —————————
class Department:
    def __init__(self, name: str):
        self.name = name
        self.courses: list[Course] = []

    def add_course(self, course: Course) -> list[Course]:
        self.courses.append(course)
        return self.courses


# ————————— Example Usage —————————
# Students and Instructors
s1 = Student("Tayyab", 19, 1)
s2 = Student("Ali",   20, 2)
i1 = Instructor("Umar", 30, 10000.0)

# Register students & assign instructor
print(s1.register_course("Python Programming"))
print(i1.assign_course("Python Programming"))

# Create a Course, add them
c1 = Course(1, "Python Programming")
c1.add_student(s1)
c1.add_student(s2)
c1.set_instructor(i1)

# Department
d1 = Department("Computer Science")
d1.add_course(c1)

# Outputs
print([stu.name for stu in c1.students])        # ['Tayyab', 'Ali']
print([inst.name for inst in c1.instructors])   # ['Umar']
print([c.name for c in d1.courses])             # ['Python Programming']
