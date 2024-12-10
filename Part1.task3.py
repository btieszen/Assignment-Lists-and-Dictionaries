#Merge two list

import time

def merge_list():
    
    start_time=time.time()
    a=[1,2,3,4,5]
    print(f"First List: {a}")
    b=[6,7,8,9,10]
    print(f"Second list: {b}")
    c=a+b
    print(f"Combined List is{c}")
    end_time=time.time()
    merge_time=end_time-start_time
    print(f"Time to combined list is: {merge_time:.7f}")
merge_list()