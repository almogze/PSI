import string

from PIL import Image
import numpy as np
import pandas as pd
import os
from gui.uis.api.fitting import Functions_Fit, Functions_Texts, Fit


class Analysis(object):
    _instance = None

    def __new__(self):
        if not Analysis._instance:
            self._instance = super(Analysis, self).__new__(self)
            # EXCEL SETTINGS FIELDS
            self.excel_file_path = None
            self.sheet_name = None

            self.axis: np.ndarray = None

            # GRAPH SETTINGS FIELDS
            self.main_title = None
            self.x_label_title = None
            self.y_label_title = None
            self.box_location = 1
            self.fun_texts = Functions_Texts()

            # FIT SETTINGS FIELDS
            self.data_frame: pd.DataFrame = None
            self.fit = Fit()
            self.fun_fits = Functions_Fit()

        return Analysis._instance

    def setExcelPath(self, path) -> bool:
        if path == "":
            return bool(False)
        self._instance.excel_file_path = path
        return bool(True)

    def setExcelSheetName(self, sheet_name):
        self._instance.sheet_name = sheet_name

    def getSheetName(self):
        return self._instance.sheet_name

    def setSheetName(self, sheet_name) -> bool:
        if sheet_name == "":
            return bool(False)
        self._instance.sheet_name = sheet_name
        return bool(True)

    def getExcelPath(self):
        return self._instance.excel_file_path

    def getExcelAxis(self):
        return self._instance.axis

    def getDataFrame(self):
        return self._instance.data_frame

    def checkExcelFormat(self) -> bool:
        ename, eend = os.path.splitext(self._instance.excel_file_path)
        if eend != '.xlsx':
            return bool(False)
        return bool(True)

    def readExcel(self) -> bool:
        if (self.excel_file_path is not None) and (self.sheet_name is not None):
            self._instance.data_frame = pd.read_excel(self.excel_file_path, sheet_name=self.sheet_name)
            return bool(True)
        return bool(False)

    def initializeAxis(self) -> bool:
        if self.data_frame is None:
            return bool(False)
        elif len(self.data_frame.axes.pop(1).values) < 2:
            return bool(False)
        else:
            # extract the axis names from excel file
            self._instance.axis = self.data_frame.axes.pop(1).values
            return bool(True)

    def setFitData(self, x, y, dx, dy):
        self._instance.fit.set_arrays(x, y, dx, dy)


