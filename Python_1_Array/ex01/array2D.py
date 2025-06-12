import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    try:
        if not isinstance(family, list) or type(start) is not int or type(end) is not int:
            raise TypeError("Error type")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("Input list with different sizes.")
        print ("My shape is : ", np.array(family).shape)
        ret = family[start:end]
        print ("My new shape is : ", np.array(ret).shape)
        return ret
    except Exception as Error:
        print("An error occurred:", Error)
        return []