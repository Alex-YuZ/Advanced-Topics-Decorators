import time

def my_timer1(orig_func):
    
    def wrapper(*args, **kwargs):
        
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in {} seconds.".format(orig_func.__name__, t2))
        
        return result
    
    return wrapper