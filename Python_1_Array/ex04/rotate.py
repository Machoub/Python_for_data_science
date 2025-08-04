from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load

def rotate_image(img):
    if img.ndim != 3:
        raise ValueError("Image must have 3 dimensions (height, width, channels)")
    rotate_img = []
    for x in range(img.shape[0]):
        row = []
        for y in range(img.shape[1]):
            row.append(img[y, x, 0])
        rotate_img.append(row)
    return np.array(rotate_img)

def main():
    try:
    
        image = Image.open("animal.jpeg")
        img_array = np.array(image)
        x_start, x_end = 100, 500
        y_start, y_end = 450, 850
        #check if the image is loaded correctly
        zoomed_img = img_array[x_start:x_end, y_start:y_end, 0:1]
        print("The shape of image is", zoomed_img.shape, "or", zoomed_img.shape[:2])
        print(zoomed_img)
        rotate_img = rotate_image(zoomed_img)
        print("New shape after Transpose:", rotate_img.shape[:2])
        print(rotate_img)
        plt.imshow(rotate_img, cmap="gray")
        plt.show()
    except AssertionError as e:
        print("Assertion Error:", e)
    except KeyboardInterrupt:
        print("Process interrupted by user.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()