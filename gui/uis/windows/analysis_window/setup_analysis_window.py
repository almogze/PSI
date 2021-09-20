# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from PySide6 import QtGui, QtCore

from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
from pyqtgraph import PlotItem

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

# IMPORT PARAMETERS CLASS
# ///////////////////////////////////////////////////////////////
from gui.uis.api.fitting import Functions_Texts

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
        self.fun_text = Functions_Texts()
        self.graph: PlotItem = self.ui_analysis.graph
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
        (self.ui_analysis.analysis, "excel_file", self.ui_analysis))

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

        self.icon_button_send.clicked.connect(lambda: wf.load_excel_loc_to_lineEdit(self.ui_analysis.analysis,
                                                                                    self.ui_analysis.left_column.menus.lineEdit_sheet_name.text(),
                                                                                    self.ui_analysis))

        # ADD LAYOUT
        # self.ui_analysis.left_column.menus.load_btn_analysis_layout.addWidget(self.icon_button_send)

        # SEND EXCEL PARAMETERS BTN
        self.send_excel_parm_btn = PyPushButton(
            text="Send Excel Parameters",
            radius=18,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )

        self.send_excel_parm_btn.clicked.connect(lambda: wf.send_excel_parameters(self.ui_analysis.analysis,
                                                                                  self.ui_analysis))

        # ADD LAYOUT
        self.ui_analysis.load_pages.layout_send_excel_parameters.addWidget(self.send_excel_parm_btn)

        # COMBOBOX EDITING
        self.ui_analysis.load_pages.comboBox_analysis_box_location.addItems(["1", "2", "3", "4"])
        self.ui_analysis.load_pages.comboBox_analysis_fit_function.addItems(self.fun_text.fun_texts_array)
        self.ui_analysis.load_pages.comboBox_analysis_cost_function.addItems(["Chi2Regression", "EffVarChi2Reg",
                                                                              "Least of Squares"])

        # FIT, MATPLOTLIB AND CLEAN ALL BTNS
        self.ui_analysis.load_pages.fit_analysis_btn.clicked.connect(lambda: wf.fit_analysis_data(
            self.ui_analysis.analysis, self.ui_analysis))
        self.ui_analysis.load_pages.matplotlib_fit_analsis_btn.clicked. \
            connect(lambda: wf.matplotlib_fit_analysis_data(self.ui_analysis.analysis, self.ui_analysis))
        self.ui_analysis.load_pages.analysis_clean_all_btn.clicked. \
            connect(lambda: wf.clean_all_analysis_screen(self.ui_analysis.analysis, self.ui_analysis))

        # INITIALIZE VALUES
        self.ui_analysis.load_pages.lineEdit_analysis_initial_a.setText("0")
        self.ui_analysis.load_pages.lineEdit_analysis_initial_b.setText("0")
        self.ui_analysis.load_pages.lineEdit_analysis_s_limit_a.setText("-1000")
        self.ui_analysis.load_pages.lineEdit_analysis_s_limit_b.setText("-1000")
        self.ui_analysis.load_pages.lineEdit_analysis_f_limit_a.setText("1000")
        self.ui_analysis.load_pages.lineEdit_analysis_f_limit_b.setText("1000")

        # INITIALIZE GRAPH
        self.graph.showGrid(x=True, y=True)
        self.graph.addLegend()

        # ///////////////////////////////////////////////////////////////
        # END -  WIDGETS
        # ///////////////////////////////////////////////////////////////
