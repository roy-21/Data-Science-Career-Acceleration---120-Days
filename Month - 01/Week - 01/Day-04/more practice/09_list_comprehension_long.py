# List comprehension example
numbers = list(range(1, 21))

even_squares = [n*n for n in numbers if n % 2 == 0]

print("Even squares:", even_squares)
