class Student():
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade
        
    def get_student(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Grade: {self.grade}")    
        
s1 = Student("John", 101, "A")
s2 = Student("Jane", 102, "B")

print(s1.get_student())    