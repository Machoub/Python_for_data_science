
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
        if not isinstance(bmi, (int, float)) or not isinstance(limit, int):
            raise TypeError("BMI or Limits bad args")
        for first, seconde in zip(bmi):
            if first > limit or seconde > limit:
                return False
            elif first <= limit or seconde <= limit:
                return True
    except Exception as msg:
        print("An error occurred:", msg)
        return []
    

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))