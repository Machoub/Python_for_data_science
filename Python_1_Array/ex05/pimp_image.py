import numpy as np

def ft_red(array: np.ndarray) -> np.ndarray:
	"""
	Extract the red channel from a 3D numpy array representing an image.
	"""
	if array.ndim != 3 or array.shape[2] != 3:
		raise ValueError("Input must be a 3D numpy array with 3 channels (RGB).")
	red_filter = np.array(array)
	red_filter[:, :, 1] = red_filter[:, :, 1] * 0  # Set green channel to 0
	red_filter[:, :, 2] = red_filter[:, :, 2] * 0  # Set blue channel to 0

	return red_filter

def ft_green(array: np.ndarray) -> np.ndarray:
	"""
	Extract the green channel from a 3D numpy array representing an image.
	"""
	if array.ndim != 3 or array.shape[2] != 3:
		raise ValueError("Input must be a 3D numpy array with 3 channels (RGB).")
	green_filter = np.array(array)
	green_filter[:, :, 0] = 0  # Set red channel to 0
	green_filter[:, :, 2] -= green_filter[:, :, 2]

	return green_filter

def ft_blue(array: np.ndarray) -> np.ndarray:
	"""
	Extract the blue channel from a 3D numpy array representing an image.
	"""
	if array.ndim != 3 or array.shape[2] != 3:
		raise ValueError("Input must be a 3D numpy array with 3 channels (RGB).")
	blue_filter = np.array(array)
	blue_filter[:, :, 0] = 0  # Set red channel to 0
	blue_filter[:, :, 1] = 0  # Set green channel to 0

	return blue_filter

def ft_invert(array: np.ndarray) -> np.ndarray:
	"""
	Invert the colors of a 3D numpy array representing an image.
	"""
	if array.ndim != 3 or array.shape[2] != 3:
		raise ValueError("Input must be a 3D numpy array with 3 channels (RGB).")
	invert = np.array(array)
	invert = 255 - invert  # Invert the colors

	return invert

def ft_grey(array: np.ndarray) -> np.ndarray:
	"""
	Convert a 3D numpy array representing an image to grayscale.
	"""
	if array.ndim != 3 or array.shape[2] != 3:
		raise ValueError("Input must be a 3D numpy array with 3 channels (RGB).")
	grey = (array[:, :, 0].astype(np.float32) +
			array[:, :, 1].astype(np.float32) +
			array[:, :, 2].astype(np.float32)) / 3
	grey_image = np.zeros_like(array)
	grey_image[:, :, 0] = grey
	grey_image[:, :, 1] = grey
	grey_image[:, :, 2] = grey

	return grey_image