# from abc import ABC, abstractmethod
# class Auth(ABC):
#     @abstractmethod
#     def login(self):
#         pass
#     @abstractmethod
#     def singup(self): 
#        pass 

# class LoginPassword(Auth):
#     def login(self, email, password): 
#         print("Login Successfuly")
        
# # class GoogleAuth(Auth):
# #     def login(self, email, password):
# #         print("Google login link")
          
# # class FacebookAuth(Auth):
# #     #def welcome():
# #     def login(self, email, password):
# #         print("Facebook login link")
                  
# user1 = LoginPassword()
# user1.login(email = "abc@gmail.com", password="1243")        
        
class Engine():
    def start(self):
        print("Engine starts") 
       
class Car():
    def __init__(self):
        self.engine = Engine()   
        
                    