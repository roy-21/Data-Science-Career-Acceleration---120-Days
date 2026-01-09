'''
DEEP DIVE: 9.3 Micro-Challenge: The Infinite Sequence
Goal: Write a while True generator that produces Fibonacci numbers 
forever. Deep Dive: This is impossible with a standard list 
(RAM would fill up). Generators allow Infinite Data Streams because 
they process one item at a time (Lazy Evaluation).
'''

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the infinite generator
fib = fibonacci()

# Print first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib))