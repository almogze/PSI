# Data taken from Steck - Rubidium 87 D Line Data
import numpy as np


class Parameters:
    def __init__(self):
        self.wave_length_rb87 = 780.241209686 * (10 ** -9) * 100  # [ cm ]
        self.sigma_0 = (3 * self.wave_length_rb87 ** 2) / (2 * np.pi)  # [ cm ^ 2 ]
        self.ccd_pixel_size = 3.45 * 3.45 * ((10 ** -4) ** 2)  # [ cm ^ 2 ]


class Functions_Texts:
    def __init__(self):
        text_lin_fun = "a\cdot x +b"
        text_exp_fun = "a \cdot e^{b\cdot x}"
        text_cos_fun = "a\cdot \cos(b\cdot x)"
        text_cos2_fun = "a\cdot \cos(b\cdot x)^2"
        text_poly2_fun = "a\cdot x^2 + b\cdot x + c"
        text_poly3_fun = "a\cdot x^3 + b\cdot x^2 + c\cdot x +d"
        text_normalised_gauss_fun = "\dfrac{1}{\sigma\sqrt{2\pi}} e^{-\dfrac{(x-\mu)^2}{2\sigma^2}}"
        text_gauss_fun = "c\cdot e^{-\dfrac{(x-\mu)^2}{2\sigma^2}}"
        text_normalised_poisson_fun = "\dfrac{\lambda^x \cdot e^{-\lambda}}{x!}"
        text_poisson_fun = "c\cdot \dfrac{\lambda^x \cdot e^{-\lambda}}{x!}"


class Functions_Fit:
    def __init__(self):
        fit_lin_fun = lambda x, a, b: b + (x * a)
        fit_exp_fun = lambda x, a, b: a * (np.exp(b * x))
        fit_cos_fun = lambda x, a, b: a * (np.cos(b * x))
        fit_cos2_fun = lambda x, a, b: a * (np.cos(b * x)) ** 2
        fit_poly2_fun = lambda x, a, b, c: a * (x ** 2) + b * x + c
        fit_poly3_fun = lambda x, a, b, c, d: a * (x ** 3) + b * (x ** 2) + c * x + d
        fit_normalised_gauss_fun = lambda x, a, b: 1 / a * (np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - b) / a) ** 2)
        fit_gauss_fun = lambda x, sigma, mu, a: a * np.exp(-0.5 * ((x - mu) ** 2 / sigma ** 2))
        fit_normalised_poisson_fun = lambda x, lam: ((lam ** x) * np.exp((-1) * lam)) / (np.math.factorial(x))
        fit_poisson_fun = lambda x, lam, a: a * ((lam ** x) * np.exp((-1) * lam)) / (np.math.factorial(x))
