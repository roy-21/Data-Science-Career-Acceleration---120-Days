'''
12.6 - Class Variables vs Instance Variables
Goal: Set species "Human" on the Class. Set name "A" on the Instance. 
Change species and see who is affected. Deep Dive: Class Variables are 
shared by ALL instances (Memory Optimization). Instance variables are 
unique to the object.
'''

class Human:
    species = "Human"   

    def __init__(self, name):
        self.name = name


#two instances
h1 = Human("A")
h2 = Human("B")

#starting 
print(h1.species)
print(h2.species)

#class variable change
Human.species = "Alien"

# who is affected?
print(h1.species)
print(h2.species)

#instance variable change
print(h1.name)  # A
print(h2.name)  # B


