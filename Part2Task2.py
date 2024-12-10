#Find common keys in 2 dictionaries and combine values

import time

def common_dictionary():
    
    start_time=time.time()
    
    a1 = {'a': 1, 'b': 2,'x':9, 'c': 3,'d':4}
    a2 = {'b':5,'w':5,'x':6,'y': 7, 'z': 8}
    print(f"First Dictionary: {a1}")
    print(f"Second Dictionary: {a2}")
    c1 = a1 | a2
    #print(f"Combined Dictionaries: {c1}")
    print("Common Keys and new Dictionary with combined values:")
    for key in a1:
        if key in a2:
            print(key, end=" ")
            
    
            for key, in a2:
                if key in a1:
          
                    c1[key] = a2[key] + a1[key]
            
        else:
            pass

    print(c1)
    end_time=time.time()
    common_time=end_time-start_time
    print(f"Time to find common key: {common_time:.7f} seconds")
common_dictionary()