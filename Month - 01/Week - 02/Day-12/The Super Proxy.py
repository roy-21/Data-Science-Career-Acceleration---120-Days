'''
12.8 - The Super Proxy
Goal: Override_init in Admin, but still run the User setup. 
Deep Dive: Use super().__init__(). This calls the parent method, 
ensuring base initialization logic isn't lost.
'''

class User:
    def __init__(self, username):
        self.username = username
        self.is_active = True

    def login(self):
        print(f"{self.username} logged in")


class Admin(User):
    def __init__(self, username, level):
        super().__init__(username)
        self.level = level

    def delete_db(self):
        print(f"Database deleted by Admin {self.username}")

user = User("Sojib")
admin = Admin("Root", "Super")

print(user.username)  
print(user.is_active) 

print(admin.username)  
print(admin.is_active) 
print(admin.level)     

admin.login()          
admin.delete_db()     
