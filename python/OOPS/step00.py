#this is how to create a class in python
#class Student():
    #name ="zain"
    #age = 20
#hthis is how to create an object of a class in python    
#s1 = Student()
#print(s1.name, s1.age)


# class Student():
#     #default constructor
#     def __init__ (self):
#         pass
#     #parameterized constructor
#     college_name = "ABC College" #class attribute
#     def __init__ (self, name, age):
#         #self is a reference to the current instance of the class
# 		#it is used to access variables that belong to the class
#         self.name = name #instance attribute / object attribute
#         self.age = age
        
# s1 = Student("zain", 20)
# print(s1.name, s1.age)

# s2 = Student("ali", 22)    
# print(s2.name, s2.age, )  
# print(Student.college_name)  

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
  
    def get_avg (self):
        sum = 0
        for i in self.marks:
            sum += i
            print("Hi", self.name, "your average is", sum/3)
  
  
s1 = Student("zain", [99, 98, 97])
s1.get_avg()