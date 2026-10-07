def square(x: int | float) -> int | float:
    """Return x squared. Raise TypeError if x is not an int or a float."""
    if isinstance(x, (int, float)):
        return x ** 2
    else:
        raise TypeError("Input must be an int or float")


def pow(x: int | float) -> int | float:
    """Return x raised to the power x. Raise TypeError if x is not a number."""
    if isinstance(x, (int, float)):
        return x ** x
    else:
        raise TypeError("Input must be an int or float")


def outer(x: int | float, function) -> object:
    """Return a function that applies `function` to x again on every call.

    Args:
        x: the starting value.
        function: the function applied to the current value on each call.

    Returns:
        The inner function, which updates and returns the value.
    """
    count = 0

    def inner() -> float:
        """Apply `function` to the current value, store it and return it.

        If the call fails, a message is printed, the value is left
        unchanged and None is returned.
        """
        nonlocal x, count
        count += 1
        try:
            x = function(x)
            return x
        except TypeError as te:
            print(f"Type error: {te}")
        except OverflowError as oe:
            print(f"Overflow error: {oe}")
        except Exception as e:
            print(f"An error occurred: {e}")
    return inner
