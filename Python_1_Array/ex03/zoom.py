import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from load_image import ft_load


def main():
    """Load an image, print its pixels, then display a zoomed crop."""
    try:
        img_array = ft_load("animal.jpeg")
        if len(img_array) == 0:
            return
        print(img_array)
        gray = np.array(Image.fromarray(img_array).convert("L"))
        y_start, y_end = 100, 500
        x_start, x_end = 450, 850
        zoomed_img = gray[y_start:y_end, x_start:x_end, np.newaxis]
        print("New shape after slicing:", zoomed_img.shape, "or",
              zoomed_img.shape[:2])
        print(zoomed_img)
        plt.imshow(zoomed_img, cmap="gray")
        plt.show()
    except AssertionError as e:
        print("Assertion Error:", e)
    except KeyboardInterrupt:
        print("Process interrupted by user.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
