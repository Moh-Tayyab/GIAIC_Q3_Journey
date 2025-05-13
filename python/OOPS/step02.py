#Inheritance
#Ek class doosri class ki cheezen use kar sakti hai

class Animal():
    def speak (self):
        print("Animal is Speaking")
        
class Dog(Animal):
    def bark (self):
        print("Dog is barking")   
        
class Cat(Animal):
    def walk (self):
        print("Cat is Walking")   
        
c1 = Cat()       
c1.walk()      
c1.speak()

d = Dog()
d.speak()
d.bark()



      
        
        