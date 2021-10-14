# importing the pyqtgraph.examples module
import pandas as pd
import pyqtgraph.examples

# run this examples

# pyqtgraph.examples.run()

# import initExample ## Add path to library (just for examples; you do not need this)

from scipy.optimize import curve_fit

import numpy as np
from PyQt6.QtWidgets import QApplication
from iminuit import Minuit
from iminuit.cost import LeastSquares
from iminuit.util import make_func_code, describe
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import numpy as np
import matplotlib.pyplot as plt
import PyQt6 as pyqt
from PyQt6 import *
import sys
from scipy.interpolate import griddata

import lmfit
from lmfit.lineshapes import gaussian2d, lorentzian

# Interpret image data as row-major instead of col-major
# pg.setConfigOptions(imageAxisOrder='row-major')


if __name__ == '__main__':
    x = np.linspace(0, 9, 1000)
    y = lmfit.lineshapes.linear(x, 5, 2)
    y += np.random.normal(0, 0.2, x.size)
    mod = lmfit.models.LinearModel()
    # p_0 = mod.guess(y, x)
    # print(p_0)
    # print(p_0['amplitude'].max)
    res = mod.fit(y, x=x)

    par = res.params
    p_names = mod.param_names
    slope = par.values()

    print(np.sqrt(res.covar[0][0]))
    print(p_names)
    # print(slope)
    print(res.fit_report())
