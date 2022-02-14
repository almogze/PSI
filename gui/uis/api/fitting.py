import lmfit
import numpy as np

from iminuit import Minuit, describe, cost
from iminuit.util import make_func_code
from scipy.optimize import curve_fit

# IMPORT FUNCTIONS
from scipy.special import erf, erfc

# IMPORT COST FUNCTIONS
from iminuit.cost import LeastSquares
# IMPORT MODELS FOR FITTING
from lmfit.models import GaussianModel, Model


class Functions_Texts:
    def __init__(self):
        self.non_latex_text_lin_fun = "f(x) = a * x + b"
        self.non_latex_text_exp_fun = "f(x) = a * e ^ (b * x)"
        self.non_latex_text_sin_fun = "f(x) = a * sin(b * x + c)"
        self.non_latex_text_cos_fun = "f(x) = a * cos(b * x)"
        self.non_latex_text_cos2_fun = "f(x) = a * (cos(b * x)) ^ 2"
        self.non_latex_text_poly2_fun = "f(x) = a * x ^ 2 + b * x + c"
        self.non_latex_text_poly2_fun_2 = "f(x) = a * x ^ 2 + b"
        self.non_latex_text_poly3_fun = "f(x) = a * x ^ 3 + b * x ^ 2 + c * x + d"
        self.non_latex_text_normalised_gauss_fun = "f(x) = 1 / a * (sqrt(2 * pi)) * e ^ (-0.5 * ((x - b) / a) ^ 2)"
        self.non_latex_text_gauss_fun = "f(x) = a * e ^ ( -0.5 * ((x - b) ^ 2 / c ^ 2))"
        self.non_latex_text_off_gauss_fun = "f(x) = a * e ^ ( -0.5 * ((x - b) ^ 2 / c ^ 2)) + d"
        self.non_latex_text_normalised_poisson_fun = "f(x) = ((a ** x) * e ^ - a / x!"
        self.non_latex_text_poisson_fun = "a * ((b ** x) * e ^ ((-1) * b)) / x!"
        self.non_latex_text_error_fun = "a * erf((x - b) / (sqrt(2) * c)) + d"
        self.non_latex_text_error_c_fun = "a * erfc((x - b) / (sqrt(2) * c)) + d"
        self.non_text_1_slits_fraun_fun = " a * sinc ^ 2 ( (pi b (x - c)))"
        self.non_text_2_slits_fraun_fun = " c * cos ^ 2 ( (pi b (x - d))) * sinc ^ 2 ( (pi a (x - d)))"
        self.non_text_4_slits_fraun_fun = " c * sinc ^ 2 ( (pi a (x - d))) * (sin ^ 2 ( (4 pi b (x - d)))) / (sin ^ 2 ( (pi b (x - d))))"
        self.non_text_6_slits_fraun_fun = " c * sinc ^ 2 ( (pi a (x - d))) * (sin ^ 2 ( (6 pi b (x - d)))) / (sin ^ 2 ( (pi b (x - d))))"

        self.latex_text_lin_fun = "a\cdot x +b"
        self.latex_text_exp_fun = "a \cdot e^{b\cdot x}"
        self.latex_text_sin_fun = "a \cdot \sin(b\cdot x + c)"
        self.latex_text_cos_fun = "a\cdot \cos(b\cdot x)"
        self.latex_text_cos2_fun = "a\cdot \cos(b\cdot x)^2"
        self.latex_text_poly2_fun = "a\cdot x^2 + b\cdot x + c"
        self.latex_text_poly2_fun_2 = "a\cdot x^2  + b"
        self.latex_text_poly3_fun = "a\cdot x^3 + b\cdot x^2 + c\cdot x +d"
        self.latex_text_normalised_gauss_fun = "\dfrac{1}{\sigma\sqrt{2\pi}} e^{-\dfrac{(x-b)^2}{2a^2}}"
        self.latex_text_gauss_fun = "a\cdot e^{-\dfrac{(x-b)^2}{c^2}}"
        self.latex_text_off_gauss_fun = "a\cdot e^{-\dfrac{(x-b)^2}{c^2}}+d"
        self.latex_text_normalised_poisson_fun = "\dfrac{\lambda^x \cdot e^{-\lambda}}{x!}"
        self.latex_text_poisson_fun = "c\cdot \dfrac{\lambda^x \cdot e^{-\lambda}}{x!}"
        self.latex_text_error_fun = "a\cdot erf(\dfrac{(x-b)}{\sqrt{2}\cdot c})+d"
        self.latex_text_error_c_fun = "a\cdot erfc(\dfrac{(x-b)}{\sqrt{2}\cdot c})+d"
        self.latex_text_1_slits_fraun_fun = "a\cdot sinc^2(\pi b (x - c))"
        self.latex_text_2_slits_fraun_fun = "c\cdot cos^2(\pi b (x - d))\cdot sinc^2(\pi a (x - d))"
        self.latex_text_4_slits_fraun_fun = "c\cdot sinc^2(\pi a (x - d))\cdot \dfrac{sin^2(4 \pi b (x - d))}{sin^2(\pi b (x - d))}"
        self.latex_text_6_slits_fraun_fun = "c\cdot sinc^2(\pi a (x - d))\cdot \dfrac{sin^2(6 \pi b (x - d))}{sin^2(\pi b (x - d))}"

        self.text_lin_fun = "Linear"
        self.text_exp_fun = "Exponential"
        self.text_sin_fun = "Sine"
        self.text_cos_fun = "Cosine"
        self.text_cos2_fun = "Cosine square"
        self.text_poly2_fun = "Polynomial second degree"
        self.text_poly2_fun_2 = "Polynomial second degree - 2"
        self.text_poly3_fun = "Polynomial third degree"
        self.text_normalised_gauss_fun = "Normalized Gaussian"
        self.text_gauss_fun = "Gaussian"
        self.text_off_gauss_fun = "Offset Gaussian"
        self.text_normalised_poisson_fun = "Normalized Poisson"
        self.text_poisson_fun = "Poisson"
        self.text_error_fun = "Error Function"
        self.text_error_c_fun = "Complementary Error Function"
        self.text_1_slits_fraun_fun = "1 Slit Fraunhofer"
        self.text_2_slits_fraun_fun = "2 Slits Fraunhofer"
        self.text_4_slits_fraun_fun = "4 Slits Fraunhofer"
        self.text_6_slits_fraun_fun = "6 Slits Fraunhofer"

        self.fun_non_latex_texts_array = [self.non_latex_text_lin_fun, self.non_latex_text_exp_fun,
                                          self.non_latex_text_sin_fun,
                                          self.non_latex_text_cos_fun, self.non_latex_text_cos2_fun,
                                          self.non_latex_text_poly2_fun, self.non_latex_text_poly2_fun_2,
                                          self.non_latex_text_poly3_fun,
                                          self.non_latex_text_normalised_gauss_fun, self.non_latex_text_gauss_fun,
                                          self.non_latex_text_off_gauss_fun,
                                          self.non_latex_text_normalised_poisson_fun, self.non_latex_text_poisson_fun,
                                          self.non_latex_text_error_fun, self.non_latex_text_error_c_fun,
                                          self.non_text_1_slits_fraun_fun, self.non_text_2_slits_fraun_fun,
                                          self.non_text_4_slits_fraun_fun, self.non_text_6_slits_fraun_fun]

        self.fun_latex_texts_array = [self.latex_text_lin_fun, self.latex_text_exp_fun, self.latex_text_sin_fun,
                                      self.latex_text_cos_fun,
                                      self.latex_text_cos2_fun, self.latex_text_poly2_fun, self.latex_text_poly2_fun_2,
                                      self.latex_text_poly3_fun,
                                      self.latex_text_normalised_gauss_fun, self.latex_text_gauss_fun,
                                      self.latex_text_off_gauss_fun,
                                      self.latex_text_normalised_poisson_fun, self.latex_text_poisson_fun,
                                      self.latex_text_error_fun, self.latex_text_error_c_fun,
                                      self.latex_text_1_slits_fraun_fun, self.latex_text_2_slits_fraun_fun,
                                      self.latex_text_4_slits_fraun_fun, self.latex_text_6_slits_fraun_fun]

        self.fun_texts_array = [self.text_lin_fun, self.text_exp_fun, self.text_sin_fun, self.text_cos_fun,
                                self.text_cos2_fun,
                                self.text_poly2_fun, self.text_poly2_fun_2, self.text_poly3_fun,
                                self.text_normalised_gauss_fun,
                                self.text_gauss_fun, self.text_off_gauss_fun,
                                self.text_normalised_poisson_fun, self.text_poisson_fun,
                                self.text_error_fun, self.text_error_c_fun, self.text_1_slits_fraun_fun,
                                self.text_2_slits_fraun_fun, self.text_4_slits_fraun_fun, self.text_6_slits_fraun_fun]


class Functions_Fit:
    def __init__(self):
        self.fit_lin_fun = lambda x, a, b: b + (x * a)
        self.fit_exp_fun = lambda x, a, b: a * (np.exp(b * x))
        self.fit_sin_fun = lambda x, a, b, c: a * np.sin(b * x + c)
        self.fit_cos_fun = lambda x, a, b: a * (np.cos(b * x))
        self.fit_cos2_fun = lambda x, a, b: a * (np.cos(b * x)) ** 2
        self.fit_poly2_fun = lambda x, a, b, c: a * (x ** 2) + b * x + c
        self.fit_poly2_fun_2 = lambda x, a, b: a * (x ** 2) + b
        self.fit_poly3_fun = lambda x, a, b, c, d: a * (x ** 3) + b * (x ** 2) + c * x + d
        self.fit_normalised_gauss_fun = lambda x, a, b: 1 / a * (np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - b) / a) ** 2)
        self.fit_gauss_fun = lambda x, a, b, c: a * np.exp(-0.5 * ((x - b) ** 2 / c ** 2))
        self.fit_off_gauss_fun = lambda x, a, b, c, d: a * np.exp(-0.5 * ((x - b) ** 2 / c ** 2)) + d
        self.fit_normalised_poisson_fun = lambda x, a: ((a ** x) * np.exp((-1) * a)) / (np.math.factorial(x))
        self.fit_poisson_fun = lambda x, a, b: a * ((b ** x) * np.exp((-1) * b)) / (np.math.factorial(x))
        self.fit_error_fun = lambda x, a, b, c, d: a * erf((x - b) / (np.sqrt(2) * c)) + d
        self.fit_error_c_fun = lambda x, a, b, c, d: a * erfc((x - b) / (np.sqrt(2) * c)) + d
        self.fit_1_slit_fraun_fun = lambda x, a, b, c: a * (np.sinc((np.pi * b * (x - c)))) ** 2
        self.fit_2_slits_fraun_fun = lambda x, a, b, c, d: c * (np.cos((np.pi * b * (x - d))) ** 2) * np.sinc(
            (np.pi * a * (x - d))) ** 2
        self.fit_4_slits_fraun_fun = lambda x, a, b, c, d: c * (np.sinc(np.pi * a * (x - d)) ** 2) * (
                    (np.sin(np.pi * 4 * b * (x - d))) / (np.sin(np.pi * b * (x - d)))) ** 2
        self.fit_6_slits_fraun_fun = lambda x, a, b, c, d: c * (np.sinc(np.pi * a * (x - d)) ** 2) * (
                    (np.sin(np.pi * 6 * b * (x - d))) / (np.sin(np.pi * b * (x - d)))) ** 2

        self.fun_fit_array = [self.fit_lin_fun, self.fit_exp_fun, self.fit_sin_fun, self.fit_cos_fun, self.fit_cos2_fun,
                              self.fit_poly2_fun, self.fit_poly2_fun_2, self.fit_poly3_fun,
                              self.fit_normalised_gauss_fun,
                              self.fit_gauss_fun, self.fit_off_gauss_fun,
                              self.fit_normalised_poisson_fun, self.fit_poisson_fun, self.fit_error_fun,
                              self.fit_error_c_fun, self.fit_1_slit_fraun_fun, self.fit_2_slits_fraun_fun,
                              self.fit_4_slits_fraun_fun, self.fit_6_slits_fraun_fun]

        self.number_of_params = [2, 2, 3, 2, 2, 3, 2, 4, 2, 3, 4, 1, 2, 4, 4, 3, 4, 4, 4]


class TwoD_Function_Fit:
    def twoD_Gaussian(self, x, y, amplitude, x0, y0, sigma_x, sigma_y, theta, offset):
        x0 = float(x0)
        y0 = float(y0)
        a = (np.cos(theta) ** 2) / (2 * sigma_x ** 2) + (np.sin(theta) ** 2) / (2 * sigma_y ** 2)
        b = -(np.sin(2 * theta)) / (4 * sigma_x ** 2) + (np.sin(2 * theta)) / (4 * sigma_y ** 2)
        c = (np.sin(theta) ** 2) / (2 * sigma_x ** 2) + (np.cos(theta) ** 2) / (2 * sigma_y ** 2)
        g = offset + amplitude * np.exp(- (
                a * ((x - x0) ** 2) + 2 * b * (x - x0) * (y - y0) + c * ((y - y0) ** 2)))
        return g

    # This is the callable that is passed to curve_fit. M is a (2,N) array
    # where N is the total number of data points in Z, which will be ravelled
    # to one dimension.
    def gaussian(self, M, *args):
        x, y = M
        return self.twoD_Gaussian(x, y, *args)

    # set fit function's parameters with optimal values so that the sum of the squared residuals of
    # f(xdata, *parameters_optimal) - ydata is minimized.
    def fit_2D_function(self, two_d_function, data, p0) -> np.array:
        print(data)
        # Creating axis same scale as image
        x = np.linspace(0, 2049, 2050)
        y = np.linspace(0, 2447, 2448)
        X, Y = np.meshgrid(x, y)
        # We need to ravel the meshgrids of X, Y points to a pair of 1-D arrays.
        print()
        print(X)
        print(Y)
        xdata = np.vstack((X.ravel(), Y.ravel()))
        if two_d_function == self.gaussian:
            return curve_fit(two_d_function, xdata, data.ravel(), p0=p0, bounds=(
                tuple([0.1, -np.inf, -np.inf, 0.001, 0.001, 0, -np.inf]),
                tuple([np.inf, np.inf, np.inf, np.inf, np.inf, 360, np.inf])))
        return curve_fit(two_d_function, xdata, data.ravel(), p0=p0)

    def guess_params(self, data):
        print("Guessing Parameters for 2D gaussian:")
        model = lmfit.models.Gaussian2dModel()
        x = np.linspace(0, 2049, 2050)
        y = np.linspace(0, 2447, 2448)
        parms = model.guess(data, x=x, y=y)


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
        self.p_array = [self.a, self.b, self.c, self.d]

        self.a_0 = 0
        self.b_0 = 0
        self.c_0 = 0
        self.d_0 = 0
        self.p_0_array = [self.a_0, self.b_0, self.c_0, self.d_0]

        self.a_err = None
        self.b_err = None
        self.c_err = None
        self.d_err = None
        self.p_err_array = [self.a_err, self.b_err, self.c_err, self.d_err]

        self.a_limit_i = -1000
        self.b_limit_i = -1000
        self.c_limit_i = -1000
        self.d_limit_i = -1000
        self.limits_i_array = [self.a_limit_i, self.b_limit_i, self.c_limit_i, self.d_limit_i]

        self.a_limit_f = 1000
        self.b_limit_f = 1000
        self.c_limit_f = 1000
        self.d_limit_f = 1000
        self.limits_f_array = [self.a_limit_f, self.b_limit_f, self.c_limit_f, self.d_limit_f]

        self.params_array = []

        self.function = None
        self.func_par_num = 2

        self.x: np.array = None  # the x values
        self.y: np.array = None  # the y values
        self.dx: np.array = None  # the x-axis uncertainties
        self.dy: np.array = None  # the y-axis uncertainties

        self.chi_ndof = None
        self.chi2 = None

    def set_a_parameter(self, a):
        self.a = a
        self.p_array[0] = a

    def set_b_parameter(self, b):
        self.b = b
        self.p_array[1] = b

    def set_c_parameter(self, c):
        self.c = c
        self.p_array[2] = c

    def set_d_parameter(self, d):
        self.d = d
        self.p_array[3] = d

    def get_a_parameter(self):
        return self.a

    def get_b_parameter(self):
        return self.b

    def get_c_parameter(self):
        return self.c

    def get_d_parameter(self):
        return self.d

    def set_a_err_parameter(self, a_err):
        self.a_err = a_err
        self.p_err_array[0] = a_err

    def set_b_err_parameter(self, b_err):
        self.b_err = b_err
        self.p_err_array[1] = b_err

    def set_c_err_parameter(self, c_err):
        self.c_err = c_err
        self.p_err_array[2] = c_err

    def set_d_err_parameter(self, d_err):
        self.d_err = d_err
        self.p_err_array[3] = d_err

    def get_a_err_parameter(self):
        return self.a_err

    def get_b_err_parameter(self):
        return self.b_err

    def get_c_err_parameter(self):
        return self.c_err

    def get_d_err_parameter(self):
        return self.d_err

    def set_a_initial(self, a_0):
        self.a_0 = a_0
        self.p_0_array[0] = a_0

    def set_b_initial(self, b_0):
        self.b_0 = b_0
        self.p_0_array[1] = b_0

    def set_c_initial(self, c_0):
        self.c_0 = c_0
        self.p_0_array[2] = c_0

    def set_d_initial(self, d_0):
        self.d_0 = d_0
        self.p_0_array[3] = d_0

    def get_a_initial(self):
        return self.a_0

    def get_b_initial(self):
        return self.b_0

    def get_c_initial(self):
        return self.c_0

    def get_d_initial(self):
        return self.d_0

    def set_a_limits(self, a_i, a_f):
        self.a_limit_i = a_i
        self.a_limit_f = a_f
        self.limits_i_array[0] = a_i
        self.limits_f_array[0] = a_f

    def set_b_limits(self, b_i, b_f):
        self.b_limit_i = b_i
        self.b_limit_f = b_f
        self.limits_i_array[1] = b_i
        self.limits_f_array[1] = b_f

    def set_c_limits(self, c_i, c_f):
        self.c_limit_i = c_i
        self.c_limit_f = c_f
        self.limits_i_array[2] = c_i
        self.limits_f_array[2] = c_f

    def set_d_limits(self, d_i, d_f):
        self.d_limit_i = d_i
        self.d_limit_f = d_f
        self.limits_i_array[3] = d_i
        self.limits_f_array[3] = d_f

    def get_a_limit_i(self):
        return self.a_limit_i

    def get_a_limit_f(self):
        return self.a_limit_f

    def get_b_limit_i(self):
        return self.b_limit_i

    def get_b_limit_f(self):
        return self.b_limit_f

    def get_c_limit_i(self):
        return self.c_limit_i

    def get_c_limit_f(self):
        return self.c_limit_f

    def get_d_limit_i(self):
        return self.d_limit_i

    def get_d_limit_f(self):
        return self.d_limit_f

    def set_function(self, function):
        self.function = function

    def get_function(self):
        return self.function

    def set_arrays(self, x, y, dx=None, dy=None):
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

    def get_err_array(self):
        return self.p_err_array

    def set_func_par_num(self, par_num):
        self.func_par_num = par_num

    def get_func_par_num(self):
        return self.func_par_num

    def set_chi_ndof(self, chi_ndof):
        self.chi_ndof = chi_ndof

    def get_chi_ndof(self):
        return self.chi_ndof

    def set_chi2(self, chi2):
        self.chi2 = chi2

    def get_chi2(self):
        return self.chi2

    def optimize(self) -> Minuit:
        cost_function = self.build_cost_function()
        print("initial parameters are: ", tuple(self.p_0_array[:self.func_par_num]))
        # Set Optimization with initial parameters
        if self.get_func_par_num() == 1:
            opt = Minuit(cost_function, self.a_0)
        elif self.get_func_par_num() == 2:
            opt = Minuit(cost_function, self.a_0, self.b_0)
        elif self.get_func_par_num() == 3:
            opt = Minuit(cost_function, self.a_0, self.b_0, self.c_0)
        else:
            opt = Minuit(cost_function, self.a_0, self.b_0, self.c_0, self.d_0)
        # Set Optimization's parameters limits
        limits = []
        for i in range(self.func_par_num):
            limits.append((self.limits_i_array[i], self.limits_f_array[i]))
        opt.limits = limits
        # Activate optimization
        opt.migrad()
        # updates parameters values
        self.set_params(opt.values)
        self.set_errors(opt.errors)
        # calculate chi squares / number of degree of freedom
        chi2 = opt.fval
        ndof = len(self.get_x_array()) - len(self.get_params_array())
        self.set_chi_ndof(chi2 / ndof)
        self.set_chi2(chi2)
        return opt

    # set fit function's parameters with optimal values so that the sum of the squared residuals of
    # f(xdata, *parameters_optimal) - ydata is minimized.
    def opt_by_scipy(self):
        popt, pcov = curve_fit(self.function, self.x, self.y, p0=tuple(self.p_0_array[:self.func_par_num]), bounds=(
            tuple(self.limits_i_array[:self.func_par_num]), tuple(self.limits_f_array[:self.func_par_num])))
        print("optimized parameters are: ", popt)
        self.set_params(popt)
        stderr = []
        for i in range(self.func_par_num):
            stderr.append(pcov[i][i])
        self.set_errors(stderr)

    # this method use lmfit library in oreder to fit functions
    # more details about this library can be found at https://lmfit.github.io/lmfit-py
    def opt_by_lmfit_generic(self, model: lmfit.models):
        # extract fit function's parameters names
        pars_names = model.param_names
        print(pars_names)
        # print(pars_names)
        # set each parameters with it's initial values
        for i in range(self.func_par_num):
            model.set_param_hint(name=pars_names[i], value=self.p_0_array[i], min=self.limits_i_array[i],
                                 max=self.limits_f_array[i])
        # fit the model
        result = model.fit(self.y, x=self.x)
        # print(result)
        # print(result.fit_report(min_correl=0.25))
        # extracting parameters values and standard errors
        values, stderr = [], []
        for i in range(self.func_par_num):
            # values
            values.append(result.values[pars_names[i]])
        # sometimes (usually when there is lack in data) cov matrix will be none
        if result.covar is not None:
            for i in range(self.func_par_num):
                # standard error (equal to sqrt(cov))
                stderr.append(np.sqrt(result.covar[i][i]))
        self.set_params(values)
        self.set_errors(stderr)
        self.set_chi2(result.chisqr)

    # Cost Functions Builders:
    def build_cost_function(self) -> LeastSquares or EffVarChi2Reg:
        if self.dx is None:
            return LeastSquares(self.x, self.y, self.dy, self.function)
        else:
            return EffVarChi2Reg(self.x, self.y, self.dx, self.dy, self.function)

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
        self.update_params_array()

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

    def update_params_array(self):
        if self.a is not None:
            self.params_array.append(self.a)
            if self.b is not None:
                self.params_array.append(self.b)
                if self.c is not None:
                    self.params_array.append(self.c)
                    if self.d is not None:
                        self.params_array.append(self.d)

    def has_uncertainty(self) -> bool:
        if self.dx is None and self.dy is None:
            return bool(False)
        return bool(True)

    def guess_params(self, fun_name):
        # print("Guessing Parameters:")
        if fun_name == "Gaussian" or fun_name == "Offset Gaussian":
            mod = lmfit.models.GaussianModel()
            p_0 = mod.guess(self.y, x=self.x)
            # print(p_0)
            self.set_a_initial(p_0['amplitude'].value / (p_0['sigma'].value * np.sqrt(2 * np.pi)))
            self.set_a_limits(p_0['amplitude'].min,
                              p_0['amplitude'].max)
            self.set_b_initial(p_0['center'].value)
            self.set_b_limits(np.min(self.x), np.max(self.x))
            self.set_c_initial(p_0['sigma'].value)
            self.set_c_limits(p_0['sigma'].min, p_0['sigma'].max)
        elif fun_name == "Sine":
            mod = lmfit.models.SineModel()
            p_0 = mod.guess(self.y, x=self.x)
            # print(p_0)
            self.set_a_initial(p_0['amplitude'].value)
            self.set_a_limits(p_0['amplitude'].min, p_0['amplitude'].max)
            self.set_b_initial(p_0['frequency'].value)
            self.set_b_limits(p_0['frequency'].min, p_0['frequency'].max)
            self.set_c_initial(p_0['shift'].value)
            self.set_c_limits(p_0['shift'].min, p_0['shift'].max)
        elif fun_name == "Lorentzian":
            mod = lmfit.models.LorentzianModel()
            p_0 = mod.guess(self.y, x=self.x)
            # print(p_0)
            self.set_a_initial(p_0['amplitude'].value)
            self.set_a_limits(p_0['amplitude'].min, p_0['amplitude'].max)
            self.set_b_initial(p_0['center'].value)
            self.set_b_limits(np.min(self.x), np.max(self.x))
            self.set_c_initial(p_0['sigma'].value)
            self.set_c_limits(p_0['sigma'].min, p_0['sigma'].max)
        elif fun_name == "Linear":
            mod = lmfit.models.LinearModel()
            p_0 = mod.guess(self.y, x=self.x)
            # print(p_0)
            self.set_a_initial(p_0['slope'].value)
            self.set_a_limits(p_0['slope'].min, p_0['slope'].max)
            self.set_b_initial(p_0['intercept'].value)
            self.set_b_limits(p_0['intercept'].min, p_0['intercept'].max)
        elif fun_name == "Polynomial second degree":
            mod = lmfit.models.QuadraticModel()
            p_0 = mod.guess(self.y, x=self.x)
            # print(p_0)
            self.set_a_initial(p_0['a'].value)
            self.set_a_limits(p_0['a'].min, p_0['a'].max)
            self.set_b_initial(p_0['b'].value)
            self.set_b_limits(p_0['b'].min, p_0['b'].max)
            self.set_c_initial(p_0['c'].value)
            self.set_c_limits(p_0['c'].min, p_0['c'].max)
        elif fun_name == "Polynomial third degree":
            mod = lmfit.models.PolynomialModel(degree=3)
            p_0 = mod.guess(self.y, x=self.x)
            # print(p_0)
            self.set_a_initial(p_0['c3'].value)
            self.set_a_limits(p_0['c3'].min, p_0['c3'].max)
            self.set_b_initial(p_0['c2'].value)
            self.set_b_limits(p_0['c2'].min, p_0['c2'].max)
            self.set_c_initial(p_0['c1'].value)
            self.set_c_limits(p_0['c1'].min, p_0['c1'].max)
            self.set_d_initial(p_0['c0'].value)
            self.set_d_limits(p_0['c0'].min, p_0['c0'].max)
        elif fun_name == "Polynomial third degree":
            mod = lmfit.models.PolynomialModel(degree=3)
            p_0 = mod.guess(self.y, x=self.x)
            # print(p_0)
            self.set_a_initial(p_0['c3'].value)
            self.set_a_limits(p_0['c3'].min, p_0['c3'].max)
            self.set_b_initial(p_0['c2'].value)
            self.set_b_limits(p_0['c2'].min, p_0['c2'].max)
            self.set_c_initial(p_0['c1'].value)
            self.set_c_limits(p_0['c1'].min, p_0['c1'].max)
            self.set_d_initial(p_0['c0'].value)
            self.set_d_limits(p_0['c0'].min, p_0['c0'].max)
        elif fun_name == "Exponential":
            mod = lmfit.models.ExponentialModel()
            p_0 = mod.guess(self.y, x=self.x)
            # print(p_0)
            self.set_a_initial(p_0['amplitude'].value)
            self.set_a_limits(p_0['amplitude'].min, p_0['amplitude'].max)
            self.set_b_initial(-1 / p_0['decay'].value)
            self.set_b_limits(-1 / p_0['decay'].max, -1 / p_0['decay'].min)
        elif fun_name == "Error Function" or fun_name == "Complementary Error Function":
            mod = lmfit.models.StepModel(form='linear')
            p_0 = mod.guess(self.y, x=self.x)
            # print(p_0)
            self.set_a_initial(p_0['amplitude'].value)
            self.set_a_limits(p_0['amplitude'].min, p_0['amplitude'].max)
            self.set_b_initial(p_0['center'].value)
            self.set_b_limits(np.min(self.x), np.max(self.x))
            self.set_c_initial(p_0['sigma'].value)
            self.set_c_limits(p_0['sigma'].min, p_0['sigma'].max)
