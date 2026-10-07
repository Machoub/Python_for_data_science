from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Print the statistics requested through the keyword arguments.

    Args:
        *args: the numbers (int or float) to compute the statistics on.
        **kwargs: each value is the name of a statistic to print, among
            "mean", "median", "quartile", "var" and "std".
            The keys are ignored and an unknown statistic prints nothing.

    Prints "ERROR" for each requested statistic if no number is given, if
    one of the arguments is not a number, if the value is not a string,
    or if the calculation fails. The other statistics are still printed.
    """
    valid = len(args) > 0 and all(isinstance(n, (int, float)) for n in args)
    for value in kwargs.values():
        if not valid or not isinstance(value, str):
            print("ERROR")
            continue
        try:
            if value == "mean":
                print(f"{value} : {sum(args) / len(args)}")
            elif value == "median":
                sorted_args = sorted(args)
                mid = len(sorted_args) // 2
                if len(sorted_args) % 2 == 1:
                    median = sorted_args[mid]
                else:
                    median = (sorted_args[mid - 1] + sorted_args[mid]) / 2
                print(f"{value} : {median}")
            elif value == "quartile":
                sorted_args = sorted(args)
                q1 = float(sorted_args[len(sorted_args) // 4])
                q3 = float(sorted_args[3 * len(sorted_args) // 4])
                print(f"{value} : [{q1}, {q3}]")
            elif value == "var":
                mean = sum(args) / len(args)
                var = sum((xi - mean) ** 2 for xi in args) / len(args)
                print(f"{value} : {var}")
            elif value == "std":
                mean = sum(args) / len(args)
                var = sum((xi - mean) ** 2 for xi in args) / len(args)
                print(f"{value} : {var ** 0.5}")
        except ArithmeticError:
            print("ERROR")
