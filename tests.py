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

# Interpret image data as row-major instead of col-major
# pg.setConfigOptions(imageAxisOrder='row-major')


if __name__ == '__main__':
    x = np.linspace(0, 9, 10)
    y = np.linspace(0, 4, 5)
    x1, y1 = np.meshgrid(x, y)
    print(x1)
    print(y1)