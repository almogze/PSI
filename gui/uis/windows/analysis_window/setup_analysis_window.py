# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from PySide6 import QtGui

from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from gui.uis.windows.main_window.functions_main_window import *
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

# IMPORT WIDGETS FUNCTIONS
# ///////////////////////////////////////////////////////////////
import gui.uis.api.widgets_functions as wf

# LOAD UI ATOM
# ///////////////////////////////////////////////////////////////
from .ui_analysis import *

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
            text=" Import excel file",
            radius=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_folder = QIcon(Functions.set_svg_icon("icon_folder_open_2.svg"))
        self.excel_location_btn.setIcon(self.icon_folder)
        self.excel_location_btn.setMaximumHeight(40)

        self.excel_location_btn.clicked.connect(lambda: wf.open_dialog_box_analysis
        (self.ui_analysis.analysis, "excel_file"))

        # ADD LAYOUT
        self.ui_analysis.left_column.menus.excel_file_path_btn_layout.addWidget(self.excel_location_btn)

        # BUTTON SEND
        self.icon_button_send = PyPushButton(
            text="  Send excel file path",
            radius=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_send = QIcon(Functions.set_svg_icon("icon_send.svg"))
        self.icon_button_send.setIcon(self.icon_send)
        self.icon_button_send.setMaximumHeight(40)

        self.icon_button_send.clicked.connect(lambda: wf.send_excel_parameters(self.ui_analysis.analysis,
                                                                               self.ui_analysis.left_column.menus.lineEdit_sheet_name.text(),
                                                                               self.ui_analysis))

        # ADD LAYOUT
        self.ui_analysis.left_column.menus.load_btn_analysis_layout.addWidget(self.icon_button_send)

        # ///////////////////////////////////////////////////////////////
        # END -  WIDGETS
        # ///////////////////////////////////////////////////////////////
