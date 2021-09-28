# importing the pyqtgraph.examples module
import pandas as pd
import pyqtgraph.examples

# run this examples

pyqtgraph.examples.run()

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

# Interpret image data as row-major instead of col-major
# pg.setConfigOptions(imageAxisOrder='row-major')


if __name__ == '__main__':
    p1 = pg
    """""""""
    popt = curve_fit(f, x, y, p0=(0, 0),
                     bounds=((-1000, -1000), (1000, 1000)))

    arr = np.array([11, 12, 13, 14, 15, 16, 17, 15, 11, 12, 14, None, None, None])
    result = next(x for x in arr if x is None)
    print(result)

    """""""""


"""""""""""""""

 linear_cost = LeastSquares(x, y, dy, f)
    opt = Minuit(linear_cost, 1, 1)
    opt.migrad()
    print(opt.errors)
    print(describe(f))
    f.func_code = make_func_code(["alpha", "beta", "gamma"])
    print(describe(f))
    print(f.func_code)

"""""""""""""""
