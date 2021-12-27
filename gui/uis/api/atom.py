from PIL import Image
import numpy as np
import os
from os import walk
from gui.uis.api.parameters import Parameters


class Atom(object):
    _instance = None

    def __new__(self):
        if not Atom._instance:
            self._instance = super(Atom, self).__new__(self)
            self.prm = Parameters()
            self.no_cloud_path = None
            self.with_cloud_path = None
            self.no_cloud_image_array: np.array = None
            self.cloud_image_array: np.array = None
            # Automatic Series
            self.directory_path = None
            self.automatic_with_cloud = []
            self.automatic_without_cloud = []
            # Initial Parameters
            self.x_0 = 0
            self.y_0 = 0
            self.sigma_x = 0
            self.sigma_y = 0
        return Atom._instance

    def setNoCloudPath(self, path):
        self._instance.no_cloud_path = path

    def getNoCloudPath(self):
        return self._instance.no_cloud_path

    def setCloudPath(self, path):
        self._instance.with_cloud_path = path

    def getCloudPath(self):
        return self._instance.with_cloud_path

    def setImageJPG(self):
        self._instance.no_cloud_image_array = np.asarray(Image.open(self.no_cloud_path).convert('L'))
        self._instance.cloud_image_array = np.asarray(Image.open(self.with_cloud_path).convert('L'))

    def addCloudFile(self, file):
        self.automatic_with_cloud.append(file)

    def addNoCloudFile(self, file):
        self.automatic_without_cloud.append(file)

    def setDirectoryPath(self, path):
        self.directory_path = path

    def getDirectoryPath(self):
        return self.directory_path

    def addAndSortAutomaticData(self) -> bool:
        if self.getDirectoryPath() is None:
            return bool(False)
        else:
            for (dirpath, dirnames, filenames) in walk(self.getDirectoryPath()):
                for file in filenames:
                    name, end = os.path.splitext(file)
                    if 'Without' in name and end == '.bin':
                        self.addNoCloudFile(file)
                    elif 'With' in name and end == '.bin':
                        self.addCloudFile(file)
            self.automatic_with_cloud.sort(key=lambda file_1: int(file_1[4:len(file_1) - 4]))
            self.automatic_without_cloud.sort(key=lambda file_1: int(file_1[7:len(file_1) - 4]))
            print(self.automatic_with_cloud)
            print(self.automatic_without_cloud)
            return bool(True)

    def setImageBIN(self):
        # Camera: Prosilica GC 2450
        # Pixel size: 3.45 X 3.45 [micro meter]
        # Resolution: 2050 X 2448

        # Bin file format:
        # pixel represented as a floating point of 4 byte
        # first byte is a parameter byte and therefore removed from the array
        file_no_cloud = open(self.no_cloud_path, 'rb')
        file_with_cloud = open(self.with_cloud_path, 'rb')
        self._instance.no_cloud_image_array = np.reshape(np.fromfile(file_no_cloud, dtype='int16')[2:], (2050, 2448))
        self._instance.cloud_image_array = np.reshape(np.fromfile(file_with_cloud, dtype='int16')[2:], (2050, 2448))
        file_no_cloud.close()
        file_with_cloud.close()

    def loadImage(self, ind: int) -> np.array:
        if ind == 0:
            return self.cloud_image_array
        elif ind == 1:
            return self.no_cloud_image_array
        elif ind == 2:
            return self.no_cloud_image_array - self.cloud_image_array
        elif ind == 3:
            return self.normSignal()
        else:
            return None

    def clearToLoad(self) -> bool:
        if self.cloud_image_array is None or self.no_cloud_image_array is None:
            return bool(False)
        return bool(True)

    def clearToSet(self) -> bool:
        if self.with_cloud_path is None or self.no_cloud_path is None:
            return bool(False)
        return bool(True)

    def checkImageFormatJPG(self) -> bool:
        iname1, iend1 = os.path.splitext(self.no_cloud_path)
        iname2, iend2 = os.path.splitext(self.with_cloud_path)
        if (iend1 == '.jpg' and iend2 == '.jpg') or (iend1 == '.jpeg' and iend2 == '.jpeg'):
            return bool(True)
        return bool(False)

    def checkImageFormatBIN(self) -> bool:
        iname1, iend1 = os.path.splitext(self.no_cloud_path)
        iname2, iend2 = os.path.splitext(self.with_cloud_path)
        if iend1 != '.bin' or iend2 != '.bin':
            return bool(False)
        return bool(True)

    def clearImage(self):
        self._instance.no_cloud_path = None
        self._instance.with_cloud_path = None
        self._instance.no_cloud_image_array = None
        self._instance.cloud_image_array = None

    def calculateAtomNumber(self):
        rel_I = np.divide(self.cloud_image_array.astype(float), self.no_cloud_image_array.astype(float),
                          out=np.zeros_like(self.no_cloud_image_array.astype(float)),
                          where=self.no_cloud_image_array.astype(float) != 0)
        sum_of_rel = np.log(rel_I, out=np.zeros_like(rel_I), where=(rel_I > 0))
        number_of_atoms = - np.divide(np.sum(sum_of_rel) * self.prm.ccd_pixel_size, self.prm.sigma_0)
        return number_of_atoms

    def normSignal(self) -> np.array:
        sub = self.no_cloud_image_array - self.cloud_image_array
        return np.divide(sub.astype(float), self.no_cloud_image_array.astype(float),
                         out=np.zeros_like(sub.astype(float)), where=self.no_cloud_image_array.astype(float) != 0)

    def setX_0(self, x_0: int):
        self.x_0 = x_0

    def setY_0(self, y_0: int):
        self.y_0 = y_0

    def getX_0(self):
        return self.x_0

    def getY_0(self):
        return self.y_0

    def set_sigma_X(self, sigma_x: float):
        self.sigma_x = sigma_x

    def set_sigma_Y(self, sigma_y: float):
        self.sigma_y = sigma_y

    def get_sigma_X(self):
        return self.sigma_x

    def get_sigma_Y(self):
        return self.sigma_y

    def CheckCloudParams(self) -> bool:
        if self.getX_0() is not None and self.getX_0() is not None and self.getX_0() is not None and self.getX_0() is not None:
            return bool(True)
        return bool(False)