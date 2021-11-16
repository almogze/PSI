# importing the pyqtgraph.examples module
import pandas as pd
import plotly
import pyqtgraph.examples

# run this examples

# pyqtgraph.examples.run()

# import initExample ## Add path to library (just for examples; you do not need this)
from PIL import Image
from lmfit import Model

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication
from iminuit import Minuit
from iminuit.cost import LeastSquares
from iminuit.util import make_func_code, describe
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import numpy as np
from PyQt6 import *
import sys
from scipy.interpolate import griddata
from gui.uis.api.fitting import TwoD_Function_Fit

import lmfit
from lmfit.lineshapes import gaussian2d, lorentzian

# Interpret image data as row-major instead of col-major
# pg.setConfigOptions(imageAxisOrder='row-major')


if __name__ == '__main__':
    """""""""
    data = np.reshape(np.fromfile('D:\\University\\PSI\\Projects\\Measuring cloud density\\Program\\cloud data\\absorption136.bin', dtype='single')[1:], (2050, 2448))
    z = np.fromfile('D:\\University\\PSI\\Projects\\Measuring cloud density\\Program\\cloud data\\absorption136.bin', dtype='single')[1:]
    two_d = TwoD_Function_Fit()
    model = lmfit.models.Gaussian2dModel()

    x = np.linspace(0, 2049, 2050)
    y = np.linspace(0, 2447, 2448)
    X, Y = np.meshgrid(x,y)

    x1 = np.linspace(0, 9, 10).reshape(5,2)
    # y1 = np.linspace(0, 4, 5)
    # X1, Y1 = np.meshgrid(x1, y1)
    print(x1)
    print(x1[:, 0])

    z_2 = gaussian2d(x=X.ravel(), y=Y.ravel(), amplitude=30, centerx=1000, centery=1000, sigmax=200, sigmay=800)
    # z_2 += 2 * (np.random.rand(*z_2.shape) - .5)
    """""""""
    n = np.asarray(Image.open('D:\\6 slit inverse.jpg').convert('L'))
    print(n)

    """""""""
    # Narrow rectangular slit
    sinc_1 = lambda x, a, W, l, d: (a * W) * np.sinc((np.pi * W * x)/(l * d))
    sinc_2 = lambda x, a, W, l, d: ((a * W) ** 2) * np.sinc((np.pi * W * x)/(l * d)) ** 2

    model = Model(sinc_2)
    params = model.make_params(a=0.1, W=0.002, l=632 * 10 ** -9, d=1000)

    x = np.linspace(-3, 3, 5000)
    y_eval = model.eval(params, x=x)

    print(f'parameter names: {model.param_names}')
    print(f'independent variables: {model.independent_vars}')


    y_fit = sinc_2(x ,1,1,1,1)
    plt.plot(x, y_eval)
    plt.show()
    
    z_3 = two_d.twoD_Gaussian(x=X, y=Y,  amplitude=30, x0=1000, y0=1000, sigma_x=200, sigma_y=800, theta=0, offset=0)
    print(z_3)
    model.set_param_hint(name='amplitude', value=15, min=0,
                         max=50)
    model.set_param_hint(name='x0', value=500, min=0,
                         max=2049)
    model.set_param_hint(name='y0', value=500, min=0,
                         max=2447)
    model.set_param_hint(name='sigma_x', value=100, min=0,
                         max=2000)
    model.set_param_hint(name='sigma_y', value=300, min=0,
                         max=2000)
    model.set_param_hint(name='theta', value=0, min=0,
                         max=360)
    model.set_param_hint(name='offset', value=0, min=0,
                         max=1000)
    """""""""

    # params = model.guess(data.ravel(), x=X.ravel(), y=Y.ravel())
    # print(params)
    # res = model.fit(data.ravel(), x=X.ravel(), y=Y.ravel(), params=params)
    # print(res.fit_report())
