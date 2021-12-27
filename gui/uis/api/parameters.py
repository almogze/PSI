# Data taken from Steck - Rubidium 87 D Line Data
import numpy as np


class Parameters:
    def __init__(self):
        self.wave_length_rb87 = 780.241209686 * (10 ** -9) * 100  # [ cm ]
        self.sigma_0 = (3 * self.wave_length_rb87 ** 2) / (2 * np.pi)  # [ cm ^ 2 ]
        self.ccd_pixel_size = 3.45 * 3.45 * ((10 ** -4) ** 2)  # [ cm ^ 2 ]

        # Cloud Parameters
        self.detuning = 0
        self.lens_1 = 0
        self.lens_2 = 0
        self.ccd_pixel_length = 3.45 * (10 ** -4)  # [ cm ^ 2 ]

    def set_cloud_parameters(self, detuning, sigma_0, f1, f2, pixel_length):
        self.detuning = detuning
        self.sigma_0 = sigma_0
        self.lens_1 = f1
        self.lens_2 = f2
        self.ccd_pixel_length = pixel_length

