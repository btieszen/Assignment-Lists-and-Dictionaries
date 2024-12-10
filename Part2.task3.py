#Counts frequency of a list

import time

start_time=time.time()
def count_freq():
    a = ['apple','grape', 'banana', 'apple', 'orange', 'banana', 'banana']

    b = {}


    for c in a:

        b[c] = b.get(c, 0) + 1
    print(f"Original List: {a}")
    print("Count of each item in the list:")
    print(b)
    end_time=time.time()
    count_time=end_time-start_time
    print(f"Time to count each item in list: {count_time:.7f}")
count_freq()