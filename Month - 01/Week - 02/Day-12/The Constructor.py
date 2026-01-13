'''
12.1 - The Constructor
Goal: Create a class User. Ensure every user starts with is_active True. 
Deep Dive: The__init_ method is the "Constructor". Python calls it 
automatically immedi-ately after memory allocation to initialize the
object's state.
'''

# define user class
class User:
    def __init__(self, username):
        self.name = username
        self.is_active = True

user1 = User("Sojib")

print(user1.name)       
print(user1.is_active)
