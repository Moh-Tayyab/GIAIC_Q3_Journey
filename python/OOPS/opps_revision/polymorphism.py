class Vehicle():
    def start_engine(self):
        print("Starting engine of vehicle")

class Car(Vehicle):
    def start_engine(self):
        print("Starting engine of car")    

class Bike(Vehicle):
	def start_engine(self):
		print("Starting engine of bike")            
  
 
def engine_test(vehicle):
	vehicle.start_engine()  
 
 
car = Car()
bike = Bike() 