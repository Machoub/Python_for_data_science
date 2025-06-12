
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        if len(height) != len(weight):
            raise ValueError("Lists of height and weight must have the same length.")
        bmi_value = []
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float) or not isinstance(w, (int, float))):
                raise TypeError("Lists have the bad args [int, float]")
            if h <= 0 or w <= 0:
                raise ValueError("Height and weight values must be positive.")
            bmi = (w / pow(h, 2))
            bmi_value.append(bmi)
        return bmi_value
    except Exception as msg:
        print("An error occurred:", msg)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
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