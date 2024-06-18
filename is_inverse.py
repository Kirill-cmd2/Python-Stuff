import math

# there could be any mathematical function
# represented in Pythonic statement
# log(x - 2) - base 'e', as an example
def f(x):
    return math.log(x - 2)

# e**x + 2
def g(x):
    return math.exp(x) + 2

test_values = [2,4,6,8,5]

# giving a function value from another function
# and getting given value
# indicates that these functions are inverse of each other
# ---variables below will contain list of bools---
inverse_check_f_g = [math.isclose(f(g(x)), x) for x in test_values]
inverse_check_g_f = [math.isclose(g(f(x)), x) for x in test_values]
