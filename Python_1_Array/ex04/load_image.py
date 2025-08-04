from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified path and return it as a numpy array."""
    try:
        #shape not 3
        if path[-5:] != ".jpeg" and path[-4:] != ".jpg":
            raise FileNotFoundError("bad format .jpeg or .jpg")
        img = np.asanyarray(Image.open(path))
        if img.ndim != 3:
            raise ValueError("Image must have 3 dimensions (height, width, channels)")
        print("The shape of image is: ", img.shape)
        return img
    except Exception as Error:
        print("An error occurred:", Error)
        return []