# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from PySide6 import QtGui

from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
import sys
import os

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

# LOAD UI ANALYSIS
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.analysis_window.ui_analysis import *

# MAIN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *


class SetupAnalysisWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui_analysis = UI_AnalysisWindow()

        # SETUP APPLICATIONS
        # Notice that they comes in singleton mode
        # ///////////////////////////////////////////////////////////////

    # SETUP ATOM WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui_analysis(self):
        self.themes = self.ui_analysis.themes

        # /////////////////////////////////////////////////////////
        # ANALYSIS WIDGETS
        # /////////////////////////////////////////////////////////

        # GRAPH LOAD / CLEAR BUTTONS

        # self.atom_graph_generate_btn = QPushButton("Generate")
        self.excel_location_btn = PyPushButton(
            text=" Load excel file",
            radius=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_folder = QIcon(Functions.set_svg_icon("icon_folder_open_2.svg"))
        self.excel_location_btn.setIcon(self.icon_folder)
        self.excel_location_btn.setMaximumHeight(40)

        # ADD LAYOUT
        self.ui_analysis.left_column.menus.excel_file_path_btn_layout.addWidget(self.excel_location_btn)

        # ///////////////////////////////////////////////////////////////
        # END -  WIDGETS
        # ///////////////////////////////////////////////////////////////
