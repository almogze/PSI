class Instances:
    _instance = None

    def __new__(cls, ui_analysis=None, ui_atom=None):
        if not Instances._instance:
            cls._instance = super(Instances, cls).__new__(cls)
            cls._instance.ui_analysis = ui_analysis
            cls._instance.ui_atom = ui_atom
        return Instances._instance

    def getAnalysis(self):
        return self._instance.ui_analysis

    def getAtom(self):
        return self._instance.ui_atom
