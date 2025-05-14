# create a university manage system using oops in python



class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    def getName(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
        
class Student(Person): 
    def __init__ (self, name,age,rollNum):
        super().__init__(name,age)
        self.rollNum = rollNum
        self.course = []
        
        
    def registerForCourses(self,course):
        self.course.append(course)
        return self.course
    
class Instructor(Person): 
    def __init__ (self, name,age,salary):
        super().__init__(name,age)
        self.salary = salary
        self.course = []
        
        
    def setCourses(self,course):
        self.course.append(course)
        return self.course
    
    
class Courses():
    students = []
    instructor = []
    def __init__(self, id, name ):
        self.id = id
        self.name = name
        
        
    def addStudent(self,stu_name):
        self.students.append(stu_name)
        return self.students 
    
    
class Department():
    def __init__(self, salary, courses):
        self.salary = salary
        self.courses = courses 
            
            
s1 = Student("Tayyab",19,1)
print(s1.registerForCourses("Python Programming"))
i1 = Instructor("Umar",19,10000)
print(i1.setCourses("Java Programming"))

		         
c1 = Courses("1","Ai")
print(c1.addStudent("Tayyab"))
print(c1.addStudent("Ahmed"))
print(c1.addStudent("Umar"))