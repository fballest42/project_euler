#!/usr/bin/env python3
""" My own version of map()

"""
def testt(i):
    try:
        if i == 1:
            yield "Hola"
    except:
        print("ADIOS")
    return None

def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Returns:
        An iterable.
        None if the iterable can not be used by the function.
    """
    try:
        if isinstance(iterable, (list, tuple)):
            print("HOLA")
            for i in iterable:
                yield function_to_apply(i)
        else:
            return None
    except Exception as exc: 
        print(exc)

x = {1, 2, 3, 4, 5}
print(list(testt(0)))
# print(ft_map(lambda dum: dum + 1, x))
