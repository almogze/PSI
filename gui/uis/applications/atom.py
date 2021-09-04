
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
