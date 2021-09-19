from PIL import Image
import numpy as np
import os
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
        self._instance.no_cloud_image_array = np.array(Image.open(self.no_cloud_path))
        self._instance.cloud_image_array = np.array(Image.open(self.with_cloud_path))

    def setImageBIN(self):
        # Camera: Prosilica GC 2450
        # Pixel size: 3.45 X 3.45 [micro meter]
        # Resolution: 2050 X 2448

        # Bin file format:
        # pixel represented as a floating point of 4 byte
        # first byte is a parameter byte and therefore removed from the array
        file_no_cloud = open(self.no_cloud_path, 'rb')
        file_with_cloud = open(self.with_cloud_path, 'rb')
        self._instance.no_cloud_image_array = np.reshape(np.fromfile(file_no_cloud, dtype='single')[1:], (2050, 2448))
        self._instance.cloud_image_array = np.reshape(np.fromfile(file_with_cloud, dtype='single')[1:], (2050, 2448))
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
        if iend1 != '.jpg' or iend2 != '.jpg':
            return bool(False)
        return bool(True)

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
        rel_I = np.divide(self.cloud_image_array, self.no_cloud_image_array,
                          out=np.zeros_like(self.no_cloud_image_array), where=self.no_cloud_image_array != 0)
        sum_of_rel = np.log(rel_I, out=np.zeros_like(rel_I), where=(rel_I > 0))
        number_of_atoms = - np.divide(np.sum(sum_of_rel) * self.prm.ccd_pixel_size , self.prm.sigma_0)
        return number_of_atoms

    def normSignal(self) -> np.array:
        sub = self.no_cloud_image_array - self.cloud_image_array
        return np.divide(sub, self.no_cloud_image_array, out=np.zeros_like(sub), where=self.no_cloud_image_array != 0)

