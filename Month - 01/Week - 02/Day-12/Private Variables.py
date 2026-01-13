'''
12.4  Private Variables
Goal: Prevent external code from changing user password. 
Deep Dive: Rename it to_password. Python performs ""Name Mangling** 
(User_password), making it harder (though not impossible) to access 
from outside.
'''

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  #private

    def check_password(self, password):
        return self.__password == password


user = User("Sojib", "12345")

print(user.check_password("12345"))

