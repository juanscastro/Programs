# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.

def sum_mix(arr):
    return sum(map(int, arr))

# map() function returns a map object(which is an iterator) of the results after applying the
# given function to each item of a given iterable (list, tuple etc.)
# Syntax :
# map(fun, iter)
