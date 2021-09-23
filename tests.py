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
    excel = pd.ExcelFile('D:\\University\\pycharmLab\\excelCharts\\Lazer\\AlmogRaz\\4.63\\4.63.xlsx')
    # print(excel.sheet_names[:3])
    data_frame: pd.DataFrame = pd.read_excel(
        "D:\\University\\pycharmLab\\excelCharts\\Lazer\\AlmogRaz\\4.63\\4.63.xlsx", sheet_name="lens")
    x = [1, 2, 3, 4, 5]
    y = [5, 7, 9, 11, 13]
    dy = np.ones_like(y)
    f = lambda x, a, b: a * x + b
    """""""""
    popt = curve_fit(f, x, y, p0=(0, 0),
                     bounds=((-1000, -1000), (1000, 1000)))

    arr = np.array([11, 12, 13, 14, 15, 16, 17, 15, 11, 12, 14, None, None, None])
    result = next(x for x in arr if x is None)
    print(result)

    """""""""
    linear_cost = LeastSquares(x, y, dy, f)
    opt = Minuit(linear_cost, 1, 1)
    opt.migrad()

    print(describe(f))
    f.func_code = make_func_code(["alpha", "beta", "gamma"])
    print(describe(f))
    print(f.func_code)

"""""""""""""""

import initExample ## Add path to library (just for examples; you do not need this)
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph.Point import Point

#generate layout
app = pg.mkQApp("Crosshair Example")
win = pg.GraphicsLayoutWidget(show=True)
win.setWindowTitle('pyqtgraph example: crosshair')
label = pg.LabelItem(justify='right')
win.addItem(label)
p1 = win.addPlot(row=1, col=0)
p2 = win.addPlot(row=2, col=0)
p3 = win.addPlot(row=2, col=1)

region = pg.LinearRegionItem()
region.setZValue(10)
# Add the LinearRegionItem to the ViewBox, but tell the ViewBox to exclude this 
# item when doing auto-range calculations.
p2.addItem(region, ignoreBounds=True)

#pg.dbg()
# p1.setAutoVisible(y=True)


#create numpy arrays
#make the numbers large to show that the xrange shows data from 10000 to all the way 0
data1 = 10000 + 15000 * pg.gaussianFilter(np.random.random(size=10000), 10) + 3000 * np.random.random(size=10000)
data2 = 15000 + 15000 * pg.gaussianFilter(np.random.random(size=10000), 10) + 3000 * np.random.random(size=10000)
data3 = 20000 + 15000 * pg.gaussianFilter(np.random.random(size=10000), 10) + 3000 * np.random.random(size=10000)

p1.plot(data1, pen="r")
p1.plot(data2, pen="g")

p2.plot(data1, pen="w")
p3.plot(data3, pen="b")
def update():
    region.setZValue(10)
    minX, maxX = region.getRegion()
    p1.setXRange(minX, maxX, padding=0)
    p3.setXRange(minX, maxX, padding=0)      

region.sigRegionChanged.connect(update)

def updateRegion(window, viewRange):
    rgn = viewRange[0]
    region.setRegion(rgn)

p1.sigRangeChanged.connect(updateRegion)
p3.sigRangeChanged.connect(updateRegion)

region.setRegion([1000, 2000])

#cross hair
vLine = pg.InfiniteLine(angle=90, movable=False)
hLine = pg.InfiniteLine(angle=0, movable=False)
p1.addItem(vLine, ignoreBounds=True)
p1.addItem(hLine, ignoreBounds=True)


vb = p1.vb

def mouseMoved(evt):
    pos = evt[0]  ## using signal proxy turns original arguments into a tuple
    if p1.sceneBoundingRect().contains(pos):
        mousePoint = vb.mapSceneToView(pos)
        index = int(mousePoint.x())
        if index > 0 and index < len(data1):
            label.setText("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>" % (mousePoint.x(), data1[index], data2[index]))
        vLine.setPos(mousePoint.x())
        hLine.setPos(mousePoint.y())



proxy = pg.SignalProxy(p1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)
#p1.scene().sigMouseMoved.connect(mouseMoved)


if __name__ == '__main__':
    pg.exec()



"""""""""""""""
