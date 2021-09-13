from PIL import Image
import numpy as np
import os


class Atom(object):
    _instance = None

    def __new__(self):
        if not Atom._instance:
            self._instance = super(Atom, self).__new__(self)
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
        self._instance.no_cloud_image_array = np.reshape(np.fromfile(self.no_cloud_path, dtype=np.uint8)[4:], (2788, 7200))
        self._instance.cloud_image_array = np.reshape(np.fromfile(self.with_cloud_path, dtype=np.uint8)[4:], (2788 , 7200))

    def loadImage(self, ind: int) -> np.array:
        if ind == 0:
            return self.cloud_image_array
        elif ind == 1:
            return self.no_cloud_image_array
        elif ind == 2:
            return self.no_cloud_image_array - self.cloud_image_array
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
        self.no_cloud_path = None
        self.with_cloud_path = None
        self.no_cloud_image_array = None
        self.cloud_image_array = None

    def calculateAtomNumber(self):
        return
