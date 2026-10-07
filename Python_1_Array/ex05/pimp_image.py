import numpy as np
import matplotlib.pyplot as plt


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Extract the red channel from a 3D numpy array representing an image.
    """
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError(
            "Input must be a 3D numpy array with 3 channels (RGB).")
    red_filter = np.array(array)
    red_filter[:, :, 1] = red_filter[:, :, 1] * 0  # Set green channel to 0
    red_filter[:, :, 2] = red_filter[:, :, 2] * 0  # Set blue channel to 0
    plt.imshow(red_filter)  # Display the red channel image
    plt.show()
    return red_filter


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Extract the green channel from a 3D numpy array representing an image.
    """
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError(
            "Input must be a 3D numpy array with 3 channels (RGB).")
    green_filter = np.array(array)
    green_filter[:, :, 0] = 0  # Set red channel to 0
    green_filter[:, :, 2] = green_filter[:, :, 2] - green_filter[:, :, 2]
    plt.imshow(green_filter)  # Display the green channel image
    plt.show()
    return green_filter


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Extract the blue channel from a 3D numpy array representing an image.
    """
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError(
            "Input must be a 3D numpy array with 3 channels (RGB).")
    blue_filter = np.array(array)
    blue_filter[:, :, 0] = 0  # Set red channel to 0
    blue_filter[:, :, 1] = 0  # Set green channel to 0
    plt.imshow(blue_filter)  # Display the blue channel image
    plt.show()
    return blue_filter


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Invert the colors of a 3D numpy array representing an image.
    """
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError(
            "Input must be a 3D numpy array with 3 channels (RGB).")
    invert = np.array(array)
    invert = 255 - invert  # Invert the colors
    plt.imshow(invert)  # Display the inverted image
    plt.show()
    return invert


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Convert a 3D numpy array representing an image to grayscale.
    """
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError(
            "Input must be a 3D numpy array with 3 channels (RGB).")
    grey = np.sum(array / 3, axis=2)
    grey_image = np.zeros_like(array)
    grey_image[:, :, 0] = grey
    grey_image[:, :, 1] = grey
    grey_image[:, :, 2] = grey
    plt.imshow(grey_image)  # Display the grayscale image
    plt.show()
    return grey_image
