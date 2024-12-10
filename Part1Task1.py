#Advanced Operations on Python Lists
#Task 1 square a list using n number

import time

def square_numbers(n):
    start_time=time.time()
    for i in range(1, n+1):
        square = i ** 2
        print(i, '\t',  square)
    end_time=time.time()
    square_time=end_time-start_time
    print(f"Time to complete square of numbers is {square_time:.7f} seconds")   
square_numbers(10)
