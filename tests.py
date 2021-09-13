# importing the pyqtgraph.examples module
import pyqtgraph.examples

# run this examples
# pyqtgraph.examples.run()


import initExample ## Add path to library (just for examples; you do not need this)


import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import numpy as np

# Interpret image data as row-major instead of col-major
# pg.setConfigOptions(imageAxisOrder='row-major')



if __name__ == '__main__':
    array_1d = np.fromfile("D:\\University\\PSI\\Projects\\Measuring cloud density\\Program\\cloud data\\absorption1.bin" , dtype=np.uint8)[4:]
    print(np.reshape(array_1d, (6273, 3200)))