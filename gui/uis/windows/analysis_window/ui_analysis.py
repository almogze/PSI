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

# IMPORT SETUP MAIN WINDOW
# ///////////////////////////////////////////////////////////////
# from .setup_analysis_window import *

# IMPORT MAIN WINDOW PAGES / AND SIDE BOXES FOR APP
# ///////////////////////////////////////////////////////////////
from gui.uis.pages.ui_main_pages import Ui_MainPages

# RIGHT COLUMN
# ///////////////////////////////////////////////////////////////
from gui.uis.columns.ui_right_column import Ui_RightColumn

# CREDITS
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_credits_bar.py_credits import PyCredits

# IMPORT ANALYSIS CLASS
# ///////////////////////////////////////////////////////////////
from gui.uis.api.analysis import Analysis


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class UI_AnalysisWindow(object):
    def setup_ui_analysis(self, parent, ui: UI_MainWindow):
        if not parent.objectName():
            parent.setObjectName("AnalysisWindow")

        self.analysis = Analysis()
        self.load_pages = ui.load_pages
        self.left_column = ui.left_column

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

