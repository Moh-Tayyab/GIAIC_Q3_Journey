class Person():
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
class Student(Person):
    def __init__ (self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade 
        
    def get_student(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")   
        
s1 = Student("John", 20, "A")
s2 = Student("Jane", 22, "B")
s1.get_student()
s2.get_student()              

class A():
    def show(self):
        print("Class A")
class B(A):
    def show(self):
       super().show()
       print("Class B")
class C(B):
	def show(self):
		super().show()
		print("Class C")
class D(C):
    def show(self):
        super().show()
        print("Class D") 
        
d = D()
d.show()                