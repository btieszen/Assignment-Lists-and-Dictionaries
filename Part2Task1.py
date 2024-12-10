#Merge two dictionaries

import time

def merge_dictionary():
    
    start_time=time.time()
    
    a1 = {'a': 1, 'b': 2, 'c': 3,'d':4}
    a2 = {'w':5,'x':6,'y': 7, 'z': 8}
    print(f"First Dictionary: {a1}")
    print(f"Second Dictionary: {a2}")
    c1 = a1 | a2
    print(f"Combined Dictionaries: {c1}")
    end_time=time.time()
    merge_time=end_time-start_time
    print(f"Time to merge the two Dictionaries: {merge_time:.7f}")
merge_dictionary()