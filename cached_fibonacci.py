# a dict to save key-value pairs of n and the value of nth fibonacci number
numandret = dict()

def cache_fib_func(func):
    def wrapper(given_num: int):
        given_num_str = str(given_num)

        # retrieving value of nth fibonacci number
        # none, if the nth number is still not saved in dict
        retval = numandret.get(given_num_str)

        if retval:
            return retval
        else:
            fibval = func(given_num)
            numandret[given_num_str] = fibval
            return fibval

    return wrapper


@cache_fib_func
def fibonacci(n: int):
    """Get the nth fibonacci number fast!"""
    if n < 1:
        raise ValueError("Given argument must be greater than 0.")
    
    if n == 1 or n == 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

