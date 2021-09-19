import string

from PIL import Image
import numpy as np
import os
from gui.uis.api.parameters import Functions_Fit, Functions_Texts


class Analysis(object):
    _instance = None

    def __new__(self):
        if not Analysis._instance:
            self._instance = super(Analysis, self).__new__(self)
            # EXCEL SETTINGS FIELDS
            self.excel_file_path = None
            self.sheet_name = None

            self.x_column_name = None
            self.y_column_name = None
            self.dx_column_name = None
            self.dy_column_name = None

            # GRAPH SETTINGS FIELDS
            self.main_title = None
            self.x_label_title = None
            self.y_label_title = None
            self.box_location = 1
            self.fun_texts = Functions_Texts()

            # FIT SETTINGS FIELDS
            self.fun_fits = Functions_Fit()

        return Analysis._instance

    def setExcelPath(self, path) -> bool:
        if path == "":
            return bool(False)
        self._instance.excel_file_path = path
        return bool(True)

    def setSheetName(self, sheet_name) -> bool:
        if sheet_name == "":
            return bool(False)
        self._instance.sheet_name = sheet_name
        return bool(True)

    def setColumnsNames(self, x_name: string, y_name: string, dx_name: string, dy_name: string) -> bool:
        if x_name == "" or y_name == "" or dx_name == "" or dy_name == "":
            return bool(False)
        self._instance.x_column_name = x_name
        self._instance.y_column_name = y_name
        self._instance.dx_column_name = dx_name
        self._instance.dy_column_name = dy_name
        return bool(True)

    def getExcelPath(self):
        return self._instance.excel_file_path

    def getSheetName(self):
        return self._instance.sheet_name

    def checkExcelFormat(self) -> bool:
        ename, eend = os.path.splitext(self._instance.excel_file_path)
        if eend != '.xlsx':
            return bool(False)
        return bool(True)
