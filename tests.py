# importing the pyqtgraph.examples module

import pyqtgraph.examples

# run this examples

pyqtgraph.examples.run()


# import initExample ## Add path to library (just for examples; you do not need this)


import numpy as np
from PyQt6.QtWidgets import QApplication
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
    """""""""
    array_1d = file_no_cloud = open("D:\\University\\PSI\\Projects\\Measuring cloud density\\Program\\cloud data\\absorption1.bin", 'rb')
    array_2 = np.reshape(np.fromfile(array_1d, dtype='single')[1:], (2050, 2448))

    app = QApplication(sys.argv)
    window = pyqt.QtWidgets.QWidget()
    window.setWindowTitle('pythongraph crosshair example')
    layout = pyqt.QtWidgets.QVBoxLayout(window)
    label = pyqt.QtWidgets.QLabel()
    label.setText("Test!")
    layout.addWidget(label)


"
    window.show()
    sys.exit(app.exec())
    """""""""""

    from matplotlib.figure import Figure
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

    # Get window background color
    bg = palette().window().color()
    cl = (bg.redF(), bg.greenF(), bg.blueF())

    # Create figure, using window bg color
    self.fig = Figure(edgecolor=cl, facecolor=cl)

    # Add FigureCanvasQTAgg widget to form
    self.canvas = FigureCanvasQTAgg(self.fig)
    self.tex_label_placeholder.layout().addWidget(self.canvas)

    # Clear figure
    self.fig.clear()

    # Set figure title
    self.fig.suptitle('$TeX$',
                      x=0.0, y=0.5,
                      horizontalalignment='left',
                      verticalalignment='center')
    self.canvas.draw()


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