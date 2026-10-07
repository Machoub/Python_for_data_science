def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Compute the BMI of each person from two lists.

    BMI = weight / height ** 2, with height in meters and weight in kg.

    Args:
        height: heights in meters (ints or floats, strictly positive).
        weight: weights in kg (ints or floats, strictly positive).

    Returns:
        The list of BMI values, in the same order as the inputs.
        An empty list if the lists differ in size, contain a value that
        is not an int or a float, or contain a value <= 0. An error
        message is printed in that case.
    """
    try:
        if len(height) != len(weight):
            raise ValueError(
                "Lists of height and weight must have the same length.")
        for h, w in zip(height, weight):
            if (not isinstance(h, (int, float))
                    or not isinstance(w, (int, float))):
                raise TypeError("Lists have the bad args [int, float]")
            if h <= 0 or w <= 0:
                raise ValueError(
                    "Height and weight values must be positive.")
        return [w / (h ** 2) for h, w in zip(height, weight)]
    except Exception as msg:
        print("An error occurred:", msg)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Tell, for each BMI value, whether it is above a given limit.

    Args:
        bmi: BMI values (ints or floats).
        limit: the threshold to compare each BMI value with.

    Returns:
        A list of booleans, True where the BMI is strictly above the
        limit. An empty list if the limit or a BMI value is not an int
        or a float. An error message is printed in that case.
    """
    try:
        if not isinstance(limit, int) and not isinstance(limit, float):
            raise TypeError("BMI or Limits bad args")
        ret = []
        for value in bmi:
            if not isinstance(value, (int, float)):
                raise TypeError("BMI values must be integers or floats.")
            ret.append(value > limit)
        return ret
    except Exception as msg:
        print("An error occurred:", msg)
        return []
