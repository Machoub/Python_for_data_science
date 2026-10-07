from typing import Any


def callLimit(limit: int):
    """Decorator factory: allow the decorated function `limit` calls only.

    Args:
        limit: the maximum number of calls allowed.

    Returns:
        A decorator that prints an error once the limit is exceeded.
    """
    count = 0

    def callLimiter(function):
        """Wrap `function` so that it can only be called `limit` times."""
        def limit_function(*args: Any, **kwds: Any):
            """Call `function` if the limit is not reached, else report it."""
            try:
                nonlocal count
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as e:
                print(f"Error: {e}")
        return limit_function
    return callLimiter


def main():
    """Call two limited functions several times to show the limit."""
    @callLimit(3)
    def f():
        """Print f()."""
        print("f()")

    @callLimit(1)
    def g():
        """Print g()."""
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
