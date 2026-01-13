'''
12.5 -The Property Decorator
Goal: Create a "fake" variable user age that is calculated from birth 
year when ac-cessed. 
Deep Dive: Use @property. It looks like a variable access, but runs a 
method behind the scenes. This is "Encapsulation"".
'''

class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @property
    def age(self):
        current_year = 2026
        return current_year - self.birth_year

user = User("Sojib", 2002)

print(user.age)