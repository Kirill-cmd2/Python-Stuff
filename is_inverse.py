import math
import random

def is_inverse(function_f, function_g,
               numberOfTestValues:int = 5,
               startingRange:int = 0, endingRange:int = 100):
    """
    Find out is two functions are inverse of each other

    Parameters:
    function_f: function object (pointer to function)
    function_g: function object (pointer to function)
    numberOfTestValues (int): how many test value needed
    startingRange (int): minimum value for test cases
    endingRange (int): maximum value for test cases

    Returns:
    Boolean value
    """

    if numberOfTestValues < 1:
        raise ValueError("Number of test cases should be at least 1")
    
    if (startingRange > endingRange):
        raise ValueError("endingRange should be greater than startingRange")

    # test_values = [randint(startingRange, endingRange) for _ in range(numberOfTestValues - 1)]
    test_values = random.sample(range(startingRange, endingRange + 1), numberOfTestValues)

    # giving a function value from another function
    # and getting given value
    # indicates that these functions are inverse of each other
    # ---variables below will contain list of bools---
    inverse_check_f_g = [math.isclose(function_f(function_g(x)), x) for x in test_values]
    inverse_check_g_f = [math.isclose(function_g(function_f(x)), x) for x in test_values]

    if all(inverse_check_f_g) and all(inverse_check_g_f):
        return True
    
    return False


# there could be any mathematical function
# represented in Pythonic statement
# log(x - 2) - base 'e', as an example
def f(x):
    return math.log(x)

# e**x + 2
def g(x):
    return math.exp(x) + 2

print(is_inverse(f, g))