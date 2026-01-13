'''
12.3 - The String Representation
Goal: Make print (user) show "User: [Name]" instead of memory address. 
Deep Dive: Override_str (for end-users) and repr 
(for developers/debugging).
'''

class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"

    def __repr__(self):
        return f"User(name='{self.name}')"


user = User("Sojib")
print(user)

user_list = [user]
print(user_list)