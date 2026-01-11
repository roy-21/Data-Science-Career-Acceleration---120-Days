'''
DEEP DIVE: 10.2 Micro-Challenge: The Syntax Sugar
Goal: Apply the wrapper using the @decorator syntax. 
Deep Dive: The @ symbol is "Syntactic Sugar". At compile time, Python 
reads this and automatically performs the 
re-assignment func decorator (func).
'''

def wrapper(func):
    def inner():
        print("Before Call")
        func()
        print("After Call")
    return inner


@wrapper
def process_data():
    print("Processing data...")

# Call the decorated function
process_data()