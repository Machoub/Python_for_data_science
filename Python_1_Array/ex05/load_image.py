from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def ft_load(path: str) -> np.ndarray:
    try:
        assert isinstance(path, str) and len(path) > 0, "Path must be a non-empty string"
        img = Image.open(path)
        assert img is not None, "Image could not be loaded"
        assert img.format in ['JPEG', 'JPG'], "Image format must be JPEG or JPG"
        Image_array = np.array(img)
        print("The shape of image is:", Image_array.shape)
        print(Image_array)

        return Image_array
    except Exception as Error:
        print("An error occurred:", Error)
        return np.array([])