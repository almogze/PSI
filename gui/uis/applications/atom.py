from PIL import Image
import os

class Atom(object):
    _instance = None
    def __new__(self):
        if not Atom._instance:
            self._instance = super(Atom, self).__new__(self)
            self.no_cloud_path = None
            self.with_cloud_path = None
        return Atom._instance

    def setNoCloudPath(self, path):
        self._instance.no_cloud_path = path

    def getNoCloudPath(self):
        return self._instance.no_cloud_path

    def setCloudPath(self, path):
        self._instance.with_cloud_path = path

    def getCloudPath(self):
        return self._instance.with_cloud_path

    def setImage(self, error):
        if (self.with_cloud_path is None) or (self.no_cloud_path is None):
            print("Data is None!")
            error.setText("Need to insert image")
            error.exec()
        else:
            iname1, iend1 = os.path.splitext(self.no_cloud_path)
            iname2, iend2 = os.path.splitext(self.no_cloud_path)
            if iend1 != '.jpg' or iend2 != '.jpg':
                error.setText("image is not in format jpg")
                error.exec()
                print("image names: %s, %s", iname1, iname2)
            else:
                return Image.open(self.with_cloud_path)

