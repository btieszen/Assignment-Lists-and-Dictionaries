#reverse a list

import time

def reverse_numbers():
    
    start_time=time.time()
    a=[1,2,3,4,5,6,7,8,10,11,23,45,34,243,23,23,22,1,2,3,4,5,6,7,89,9]
    print(a)
    a.reverse()
    print(a)
    end_time=time.time()
    reverse_time=end_time-start_time
    print(f"Time to reverse list is {reverse_time:.7f} seconds")
reverse_numbers()