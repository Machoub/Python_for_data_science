from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def rotate_image(img):
    """Transpose an image by hand, keeping only its first channel.

    Pixel (row, column) of the result is pixel (column, row) of the input,
    i.e. the image is flipped along its main diagonal. The transposition is
    done with loops, as the subject forbids any library for it.

    Args:
        img: numpy array of shape (height, width, channels).

    Returns:
        A 2D numpy array of shape (width, height).

    Raises:
        ValueError: if img does not have 3 dimensions.
    """
    if img.ndim != 3:
        raise ValueError(
            "Image must have 3 dimensions (height, width, channels)")
    rotate_img = []
    for x in range(img.shape[1]):
        row = []
        for y in range(img.shape[0]):
            row.append(img[y, x, 0])
        rotate_img.append(row)
    return np.array(rotate_img)


def main():
    """Load animal.jpeg, crop a square, transpose it and display the result."""
    try:
        img_array = ft_load("animal.jpeg")
        if len(img_array) == 0:
            return
        gray = np.array(Image.fromarray(img_array).convert("L"))
        y_start, y_end = 100, 500
        x_start, x_end = 450, 850
        zoomed_img = gray[y_start:y_end, x_start:x_end, np.newaxis]
        print("The shape of image is:", zoomed_img.shape, "or",
              zoomed_img.shape[:2])
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
