'''
12.7 - Inheritance
Goal: Create Admin (User). Add a method delete_db() only for Admin. 
Deep Dive: The child class inherits all attributes of the parent. 
It checks its own namespace first, then the parent's. This follows 
the "MRO (Method Resolution Order)
'''

class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} logged in")


class Admin(User):
    def delete_db(self):
        print("Database deleted by Admin")


user = User("Sojib")
admin = Admin("Root")

user.login()        
admin.login()      
admin.delete_db()  
