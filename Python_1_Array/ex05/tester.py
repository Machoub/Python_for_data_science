from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
from pimp_image import ft_red, ft_green, ft_blue, ft_invert, ft_grey



array = ft_load("landscape.jpg")


red = ft_red(array)
green = ft_green(array)
blue = ft_blue(array)
invert = ft_invert(array)
grey = ft_grey(array)
print(ft_invert.__doc__)
plt.imshow(grey)
plt.savefig("landscape_grey.jpg")

