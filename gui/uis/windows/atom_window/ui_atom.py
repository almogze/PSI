# IMPORT PACKAGES FOR ANALYSING
# ///////////////////////////////////////////////////////////////
from PIL import Image
import numpy as np
import os

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.core.functions import Functions
from gui.uis.windows.main_window import UI_MainWindow

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# IMPORT ATOM CLASS
# ///////////////////////////////////////////////////////////////
from gui.uis.api.atom import Atom

# PY WINDOW
# ///////////////////////////////////////////////////////////////
class UI_AtomWindow(object):
    def setup_ui_atom(self, parent, ui: UI_MainWindow):
        if not parent.objectName():
            parent.setObjectName("AtomWindow")

        self.atom = Atom()
        self.load_pages = ui.load_pages
        self.left_column = ui.left_column
        self.cloud_combo: QComboBox = ui.load_pages.cloud_comboBox
        self.result_groupBox: QGroupBox = ui.load_pages.groupBox_Atom_results

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes: Themes = themes.items
