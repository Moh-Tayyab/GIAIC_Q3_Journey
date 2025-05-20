# SRP: Single Responsibillity Principle
# Definition: A class should have only one reason to change, meaning it should have only one job or responsibility.

class User():
    def __init__ (self, name):
        self.name
        
class UserRepository():
    def save_to_file(self, user):
        with open("user.txt", "w") as f:
            f.write(user.name)         
            
            