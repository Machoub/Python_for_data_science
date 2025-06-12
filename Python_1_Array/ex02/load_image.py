from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def ft_load(path: str) -> list:
    try:
        #shape not 3
        if path[-5:] != ".jpeg" and path[-4:] != ".jpg":
            raise FileNotFoundError("bad format .jpeg or .jpg")
        img = np.asanyarray(Image.open(path))
        print("The shape of image is: ", img.shape)
        return img
    except Exception as Error:
        print("An error occurred:", Error)
        return []

print(ft_load("landscape.jpg"))