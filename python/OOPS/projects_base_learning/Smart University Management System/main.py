# Smart University Management System (SUMS)
# 🎓 For Students, Teachers, and Admins

# 🏗️ Class Structure Design:
# 🔹 Person (Base Class)
# Attributes: name, email, national_id

# Method: display_info()

# 🔹 Student(Person)
# Attributes: student_id, courses, grades (dictionary)

# Methods:

# enroll_course(course_name)

# add_grade(course_name, grade)

# calculate_gpa()

# display_info() (override with role info)

# 🔹 Teacher(Person)
# Attributes: employee_id, subject, assigned_students (list)

# Methods:

# assign_student(student_obj)

# grade_student(student_obj, course_name, grade)

# display_info() (override)

# 🔹 Admin(Person)
# Attributes: admin_code

# Method:

# remove_student(student_id)

# view_all_users() (composition: takes user list)

# Solution:
class Person():
    def __init__(self, name, email, national_id):
        self.name = name 
        self.email = email
        self.national_id = national_id
        
    def display_info(self): 
        print(f"Name: {self.name}, Email: {self.email}, National ID: {self.national_id}")


class Student(Person):
    def __init__(self, name, email, national_id, student_id):
        super().__init__(name, email, national_id)
        self.student_id = student_id
        self.courses = []
        self.grades = {}

    def enroll_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"{self.name} is enrolled in {course_name}")
        else:
            print(f"{self.name} is already enrolled in {course_name}")

    def add_grade(self, course_name, grade):
        self.grades[course_name] = grade

    def calculate_gpa(self):
        points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
        total_points = 0
        for grade in self.grades.values():
            total_points += points.get(grade.upper(), 0)
        return round(total_points / len(self.grades), 2) if self.grades else 0.0

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Courses: {self.courses}")
        print(f"Grades: {self.grades}")
        print(f"GPA: {self.calculate_gpa()}")


class Teacher(Person):
    def __init__(self, name, email, national_id, employee_id, subject):
        super().__init__(name, email, national_id)
        self.employee_id = employee_id  
        self.subject = subject
        self.assigned_students = []

    def assign_student(self, student_obj):
        self.assigned_students.append(student_obj)
        print(f"Student {student_obj.name} assigned to {self.name}")

    def grade_student(self, student_obj, course_name, grade):
        student_obj.add_grade(course_name, grade)
        print(f"{self.name} graded {student_obj.name} in {course_name}: {grade}")

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}, Subject: {self.subject}")
        print("Assigned Students:", [s.name for s in self.assigned_students])


class Admin(Person):
    def __init__(self, name, email, national_id):
        super().__init__(name, email, national_id)
        self.students = []
        self.teachers = []

    def add_student(self, student_obj):
        self.students.append(student_obj)
        print(f"Student {student_obj.name} added to system")

    def add_teacher(self, teacher_obj):
        self.teachers.append(teacher_obj)
        print(f"Teacher {teacher_obj.name} added to system")

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]
        print(f"Student with ID {student_id} removed")

    def view_all_users(self):
        print("\n--- Students ---")
        for s in self.students:
            s.display_info()
            print()
        print("--- Teachers ---")
        for t in self.teachers:
            t.display_info()
            print()


# -------------------------- Testing the System --------------------------

# Create Admin
admin = Admin("Tayyab", "admin@uni.com", "12345")

# Create Students
s1 = Student("Ali", "ali@student.com", "001", "S001")
s2 = Student("Sara", "sara@student.com", "002", "S002")

# Create Teacher
t1 = Teacher("Sir Ameen", "ameen@uni.com", "T001", "EMP101", "OOP")

# Admin adds users
admin.add_student(s1)
admin.add_student(s2)
admin.add_teacher(t1)

# Students enroll
s1.enroll_course("OOP")
s2.enroll_course("OOP")

# Teacher assigns and grades
t1.assign_student(s1)
t1.grade_student(s1, "OOP", "A")

t1.assign_student(s2)
t1.grade_student(s2, "OOP", "B")

# Admin views all users
admin.view_all_users()
