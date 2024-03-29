""" My own version of filter()

"""
from collections.abc import Iterable

def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Returns:
        An iterable.
        None if the iterable can not be used by the function.
    """
    try:
        if isinstance(iterable, Iterable):
            for elem in [i for i in iterable if function_to_apply(i)]:
                yield elem
        else:
            return None
    except Exception as exc: 
        print(exc)
