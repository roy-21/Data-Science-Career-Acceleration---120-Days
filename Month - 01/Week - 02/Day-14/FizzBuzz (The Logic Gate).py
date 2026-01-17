'''
DEEP DIVE: 14.5 Capstone: FizzBuzz (The Logic Gate)
Goal: Print 1-100. Div by 3 "Fizz", by 5 "Buzz", both "FizzBuzz". 
Deep Dive: Order matters! Check % 15 (both) FIRST. If you check 3 first,
"FizzBuzz" numbers will just print "Fizz".
'''

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
