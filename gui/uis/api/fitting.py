import numpy as np
import matplotlib.pyplot as plt
import warnings
from iminuit import Minuit, describe, cost
from iminuit.util import make_func_code
from scipy.optimize import curve_fit
from matplotlib.offsetbox import AnchoredText

# IMPORT COST FUNCTIONS
from iminuit.cost import LeastSquares



class Functions_Texts:
    def __init__(self):
        self.latex_text_lin_fun = "a\cdot x +b"
        self.latex_text_exp_fun = "a \cdot e^{b\cdot x}"
        self.latex_text_cos_fun = "a\cdot \cos(b\cdot x)"
        self.latex_text_cos2_fun = "a\cdot \cos(b\cdot x)^2"
        self.latex_text_poly2_fun = "a\cdot x^2 + b\cdot x + c"
        self.latex_text_poly3_fun = "a\cdot x^3 + b\cdot x^2 + c\cdot x +d"
        self.latex_text_normalised_gauss_fun = "\dfrac{1}{\sigma\sqrt{2\pi}} e^{-\dfrac{(x-\mu)^2}{2\sigma^2}}"
        self.latex_text_gauss_fun = "c\cdot e^{-\dfrac{(x-\mu)^2}{2\sigma^2}}"
        self.latex_text_normalised_poisson_fun = "\dfrac{\lambda^x \cdot e^{-\lambda}}{x!}"
        self.latex_text_poisson_fun = "c\cdot \dfrac{\lambda^x \cdot e^{-\lambda}}{x!}"

        self.text_lin_fun = "Linear"
        self.text_exp_fun = "Exponential"
        self.text_cos_fun = "Cosine"
        self.text_cos2_fun = "Cosine square"
        self.text_poly2_fun = "Polynomial second degree"
        self.text_poly3_fun = "Polynomial third degree"
        self.text_normalised_gauss_fun = "Normalized Gaussian"
        self.text_gauss_fun = "Gaussian"
        self.text_normalised_poisson_fun = "Normalized Poisson"
        self.text_poisson_fun = "Poisson"

        self.fun_latex_texts_array = [self.latex_text_lin_fun, self.latex_text_exp_fun, self.latex_text_cos_fun,
                                      self.latex_text_cos2_fun, self.latex_text_poly2_fun, self.latex_text_poly3_fun,
                                      self.latex_text_normalised_gauss_fun, self.latex_text_gauss_fun,
                                      self.latex_text_normalised_poisson_fun, self.latex_text_poisson_fun]

        self.fun_texts_array = [self.text_lin_fun, self.text_exp_fun, self.text_cos_fun, self.text_cos2_fun,
                                self.text_poly2_fun, self.text_poly3_fun, self.text_normalised_gauss_fun,
                                self.text_gauss_fun, self.text_normalised_poisson_fun, self.text_poisson_fun]


class Functions_Fit:
    def __init__(self):
        self.fit_lin_fun = lambda x, a, b: b + (x * a)
        self.fit_exp_fun = lambda x, a, b: a * (np.exp(b * x))
        self.fit_cos_fun = lambda x, a, b: a * (np.cos(b * x))
        self.fit_cos2_fun = lambda x, a, b: a * (np.cos(b * x)) ** 2
        self.fit_poly2_fun = lambda x, a, b, c: a * (x ** 2) + b * x + c
        self.fit_poly3_fun = lambda x, a, b, c, d: a * (x ** 3) + b * (x ** 2) + c * x + d
        self.fit_normalised_gauss_fun = lambda x, a, b: 1 / a * (np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - b) / a) ** 2)
        self.fit_gauss_fun = lambda x, sigma, mu, a: a * np.exp(-0.5 * ((x - mu) ** 2 / sigma ** 2))
        self.fit_normalised_poisson_fun = lambda x, lam: ((lam ** x) * np.exp((-1) * lam)) / (np.math.factorial(x))
        self.fit_poisson_fun = lambda x, lam, a: a * ((lam ** x) * np.exp((-1) * lam)) / (np.math.factorial(x))

        self.fun_fit_array = [self.fit_lin_fun, self.fit_exp_fun, self.fit_cos_fun, self.fit_cos2_fun,
                              self.fit_poly2_fun, self.fit_poly3_fun, self.fit_normalised_gauss_fun,
                              self.fit_gauss_fun, self.fit_normalised_poisson_fun, self.fit_poisson_fun]


class EffVarChi2Reg:  # This class is like Chi2Regression but takes into account dx
    # This part defines the variables the class will use
    def __init__(self, x, y, dx, dy, model):
        self.model = model  # model predicts y value for given x value
        self.x = x  # the x values
        self.y = y  # the y values
        self.dx = dx  # the x-axis uncertainties
        self.dy = dy  # the y-axis uncertainties
        self.func_code = make_func_code(describe(self.model)[1:])
        self.h = (x[-1] - x[
            0]) / 10000000000000000000  # this is the step size for the numerical calculation of the df/dx = last value in x (x[-1]) - first value in x (x[0])/10000

    # This part defines the calculations when the function is called
    def __call__(self, *par):  # par are a variable number of model parameters
        self.ym = self.model(self.x, *par)
        df = (self.model(self.x + self.h,
                         *par) - self.ym) / self.h  # the derivative df/dx at point x is taken as [f(x+h)-f(x)]/h
        chi2 = sum(((self.y - self.ym) ** 2) / (self.dy ** 2 + (
                df * self.dx) ** 2))  # chi2 is now Sum of: f(x)-y)^2/(uncert_y^2+(df/dx*uncert_x)^2)
        return chi2


class Fit(object):
    def __init__(self):
        self.a = None  # Final optimized parameter
        self.b = None  # Final optimized parameter
        self.c = None  # Final optimized parameter
        self.d = None  # Final optimized parameter

        self.a_0 = 0
        self.a_err = 0
        self.b_0 = 0
        self.b_err = 0
        self.c_0 = 0
        self.c_err = 0
        self.d_0 = 0
        self.d_err = 0

        self.a_limit_i = -1000
        self.a_limit_f = 1000
        self.b_limit_i = -1000
        self.b_limit_f = 1000
        self.c_limit_i = -1000
        self.c_limit_f = 1000
        self.d_limit_i = -1000
        self.d_limit_f = 1000

        self.params_array = []

        self.function = None
        self.x: np.array = None  # the x values
        self.y: np.array = None  # the y values
        self.dx: np.array = None  # the x-axis uncertainties
        self.dy: np.array = None  # the y-axis uncertainties

    def set_a_parameter(self, a):
        self.a = a

    def set_b_parameter(self, b):
        self.b = b

    def set_c_parameter(self, c):
        self.c = c

    def set_d_parameter(self, d):
        self.d = d

    def get_a_parameter(self):
        return self.a

    def get_b_parameter(self):
        return self.b

    def set_a_err_parameter(self, a_err):
        self.a_err = a_err

    def set_b_err_parameter(self, b_err):
        self.b_err = b_err

    def set_c_err_parameter(self, c_err):
        self.c_err = c_err

    def set_d_err_parameter(self, d_err):
        self.d_err = d_err

    def get_a_err_parameter(self):
        return self.a_err

    def get_b_err_parameter(self):
        return self.b_err

    def set_a_initial(self, a_0):
        self.a_0 = a_0

    def set_b_initial(self, b_0):
        self.b_0 = b_0

    def set_a_limits(self, a_i, a_f):
        self.a_limit_i = a_i
        self.a_limit_f = a_f

    def set_b_limits(self, b_i, b_f):
        self.b_limit_i = b_i
        self.b_limit_f = b_f

    def get_a_limit_i(self):
        return self.a_limit_i

    def get_a_limit_f(self):
        return self.a_limit_f

    def get_b_limit_i(self):
        return self.b_limit_i

    def get_b_limit_f(self):
        return self.b_limit_f

    def set_function(self, function):
        self.function = function

    def get_function(self):
        return self.function

    def set_arrays(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def get_x_array(self):
        return self.x

    def get_y_array(self):
        return self.y

    def get_dx_array(self):
        return self.dx

    def get_dy_array(self):
        return self.dy

    def get_params_array(self):
        return self.params_array

    def optimize(self) -> Minuit:
        cost_function = self.build_cost_function()
        opt = Minuit(cost_function, a=self.a_0, b=self.b_0)
        opt.limits = [(self.a_limit_i, self.a_limit_f), (self.b_limit_i, self.b_limit_f)]
        opt.migrad()
        self.set_params(opt.values)
        self.set_errors(opt.errors)
        return opt

    # set fit function's parameters with optimal values so that the sum of the squared residuals of
    # f(xdata, *parameters_optimal) - ydata is minimized.
    def opt_by_scipy(self) -> np.array:
        popt = curve_fit(self.function, self.x, self.y, p0=(self.a_0, self.b_0),
                         bounds=((self.a_limit_i, self.b_limit_i), (self.a_limit_f, self.b_limit_f)))[0]
        self.set_params(popt)

    # Cost Functions Builders:
    def build_cost_function(self) -> LeastSquares or EffVarChi2Reg:
        if self.dx is not None and self.dy is not None:
            return EffVarChi2Reg(self.x, self.y, self.dx, self.dy, self.function)
        else:
            return LeastSquares(self.x, self.y, self.dy, self.function)

    def set_params(self, params: np.array):
        size = len(params)
        if size > 0:
            self.set_a_parameter(params[0])
            if size > 1:
                self.set_b_parameter(params[1])
                if size > 2:
                    self.set_c_parameter(params[2])
                    if size > 3:
                        self.set_d_parameter(params[3])
        self.update_array()

    def set_errors(self, errors: np.array):
        size = len(errors)
        if size > 0:
            self.set_a_err_parameter(errors[0])
            if size > 1:
                self.set_b_err_parameter(errors[1])
                if size > 2:
                    self.set_c_err_parameter(errors[2])
                    if size > 3:
                        self.set_d_err_parameter(errors[3])

    def update_array(self):
        if self.a is not None:
            self.params_array.append(self.a)
            if self.b is not None:
                self.params_array.append(self.b)
                if self.c is not None:
                    self.params_array.append(self.c)
                    if self.d is not None:
                        self.params_array.append(self.d)

