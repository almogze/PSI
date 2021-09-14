# Data taken from Steck - Rubidium 87 D Line Data
import numpy as np

class Parameters:
    def __init__(self):
        self.wave_length_rb87 = 780.241209686 * (10 ** -9) * 100            # [ cm ]
        self.sigma_0 = (3 * self.wave_length_rb87 ** 2) / (2 * np.pi)       # [ cm ^ 2 ]
        self.ccd_pixel_size = 3.45 * 3.45 * ((10 ** -4) ** 2)                   # [ cm ^ 2 ]
