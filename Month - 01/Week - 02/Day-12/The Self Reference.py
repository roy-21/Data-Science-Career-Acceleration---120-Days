'''
12.2 - The Self Reference
Goal: Explain why def method(self) is required. 
Deep Dive: Python passes the in-stance object as the first argument 
automatically. user.login()→ User login (user). Without self, the method 
doesn't know which user's data to access.
'''

class Car:
    def __init__(self):
        self.speed = 0

    def drive(self):
        self.speed = 100


#use 
my_car = Car()
my_car.drive()

print(my_car.speed)

