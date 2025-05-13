from abc import ABC, abstractmethod
# Abstract class

class Appliance():
    @abstractmethod 
    def turn_on(self):
       pass
        
class Fan(Appliance):
    def turn_on(self):
        print("Fan is turned on")	
        
class TV(Appliance):
    def turn_on(self):
        print("TV is turned on")    
        
            			        
fan = Fan()
fan.turn_on()                       