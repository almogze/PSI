from PIL import Image
import numpy as np
import os

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

            # FIT SETTINGS FIELDS

        return Analysis._instance

    def setExcelPath(self, path):
        self._instance.excel_file_path = path

    def setSheetName(self, sheet_name):
        self._instance.sheet_name = sheet_name

    def setColumnsNames(self, x_name, y_name, dx_name, dy_name):
        self._instance.x_column_name = x_name
        self._instance.y_column_name = y_name
        self._instance.dx_column_name = dx_name
        self._instance.dy_column_name = dy_name

    def getExcelPath(self):
        return self._instance.excel_file_path

    def checkExcelFormat(self) -> bool:
        ename, eend = os.path.splitext(self._instance.excel_file_path)
        if eend != '.xlsx':
            return bool(False)
        return bool(True)
