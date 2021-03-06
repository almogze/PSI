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
from gui.uis.api.atom_api_functions import *

# LOAD UI ATOM
# ///////////////////////////////////////////////////////////////
from .ui_atom import *

# MAIN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *


class SetupAtomWindow:
    def __init__(self):
        super().__init__()
        # SETUP ATOM WINDOW
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui_atom = UI_AtomWindow()

        # SETUP APPLICATIONS
        # Notice that they comes in singleton mode
        # ///////////////////////////////////////////////////////////////

    # SETUP ATOM WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui_atom(self):
        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        self.themes = self.ui_atom.themes
        self.graph: PlotItem = self.ui_atom.graph
        self.spots = self.ui_atom.spots

        # /////////////////////////////////////////////////////////
        # ATOM WIDGETS
        # /////////////////////////////////////////////////////////

        # GRAPHIC VIEW
        # ///////////////////////////////////////////////////////////////
        self.ui_atom.image_view.getAxis('left').setLabel('y axis pixels')
        self.ui_atom.image_view.getAxis('bottom').setLabel('x axis pixels')
        self.ui_atom.image_view.setTitle(
            "pixel: (%0.0f, %0.0f), intensity: None" % (self.ui_atom.inf1.value(), self.ui_atom.inf2.value()))

        self.ui_atom.graph_top.getAxis('bottom').setStyle(showValues=False)
        self.ui_atom.graph_top.showAxis('top')
        self.ui_atom.graph_top.getAxis('top').setLabel('x axis pixels')
        self.ui_atom.graph_top.getAxis('left').setLabel('pixels intensity')

        self.ui_atom.graph_right.getAxis('left').setStyle(showValues=False)
        self.ui_atom.graph_right.getAxis('bottom').setLabel('pixels intensity')
        self.ui_atom.graph_right.showAxis('right')
        self.ui_atom.graph_right.getAxis('right').setLabel('y axis pixels')

        self.ui_atom.image_view.addItem(self.ui_atom.image)
        self.ui_atom.bar.setImageItem(self.ui_atom.image, insert_in=self.ui_atom.image_view)

        self.ui_atom.image_view.addItem(self.ui_atom.inf1)
        self.ui_atom.image_view.addItem(self.ui_atom.inf2)

        # signals dealing: lines motion and scaling
        self.ui_atom.inf1.sigPositionChanged.connect(lambda: update_right_graph(self.ui_atom.atom, self.ui_atom))
        self.ui_atom.inf2.sigPositionChanged.connect(lambda: update_top_graph(self.ui_atom.atom, self.ui_atom))

        self.ui_atom.inf1.sigPositionChangeFinished.connect(lambda: fit_gaussian_y(self.ui_atom.atom, self.ui_atom))
        self.ui_atom.inf2.sigPositionChangeFinished.connect(lambda: fit_gaussian_x(self.ui_atom.atom, self.ui_atom))

        self.ui_atom.image_view.sigRangeChanged.connect(
            lambda window, viewRange: update_region_image_view(viewRange, self.ui_atom))
        self.ui_atom.graph_top.sigRangeChanged.connect(
            lambda window, viewRange: update_region_top(viewRange, self.ui_atom))
        self.ui_atom.graph_right.sigRangeChanged.connect(
            lambda window, viewRange: update_region_right(viewRange, self.ui_atom))


        # GRAPH LOAD / CLEAR BUTTONS

        # self.atom_graph_generate_btn = QPushButton("Generate")
        self.atom_graph_load_btn = PyPushButton(
            text="Load",
            radius=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.atom_graph_load_btn.clicked.connect(lambda: load_image(self.ui_atom.atom, self.ui_atom))

        self.atom_graph_clear_btn = PyPushButton(
            text="Clear",
            radius=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.atom_graph_clear_btn.clicked.connect(lambda: clear_image(self.ui_atom.atom, self.ui_atom))

        self.ui_atom.load_pages.btn_atom_graph_load_layout.addWidget(self.atom_graph_load_btn)
        self.ui_atom.load_pages.btn_atom_clear_layout.addWidget(self.atom_graph_clear_btn)

        # BTN OPEN IMAGE 1
        self.no_cloud_btn = PyPushButton(
            text=" Open image",
            radius=3,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_folder = QIcon(Functions.set_svg_icon("icon_folder_open_2.svg"))
        self.no_cloud_btn.setIcon(self.icon_folder)
        self.no_cloud_btn.setMaximumHeight(40)

        self.no_cloud_btn.clicked.connect(lambda: open_dialog_box_atom( self.ui_atom.atom, self.ui_atom,  "Without Cloud"))
        # ADD LAYOUT
        self.ui_atom.left_column.menus.no_cloud_layout.addWidget(self.no_cloud_btn)

        # BTN OPEN IMAGE 2
        self.with_cloud_btn = PyPushButton(
            text=" Open image",
            radius=3,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"]
        )
        self.with_cloud_btn.setMaximumHeight(40)
        self.with_cloud_btn.setIcon(self.icon_folder)

        self.with_cloud_btn.clicked.connect(lambda: open_dialog_box_atom(self.ui_atom.atom, self.ui_atom,  "With Cloud"))
        # ADD LAYOUT
        self.ui_atom.left_column.menus.with_cloud_layout.addWidget(self.with_cloud_btn)

        self.ui_atom.load_pages.btn_atom_clear_graph.clicked.connect(
            lambda: clear_automatic_graph(self.ui_atom.atom, self.ui_atom))

        # BTN OPEN IMAGE AUTOMATIC
        self.automatic_pull_btn = PyPushButton(
            text=" Pull Images",
            radius=3,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_two"],
            bg_color_pressed=self.themes["app_color"]["dark_three"]
        )
        self.automatic_pull_btn.setMaximumHeight(40)
        self.automatic_pull_btn.setIcon(self.icon_folder)

        self.automatic_pull_btn.clicked.connect(
            lambda: open_dialog_box_atom(self.ui_atom.atom, self.ui_atom, "Automatic Pull"))
        # ADD LAYOUT
        self.ui_atom.left_column.menus.aoutomatic_pull_atom_layout.addWidget(self.automatic_pull_btn)

        # COMBOBOX WIDGETS
        self.ui_atom.cloud_combo.addItems(["subtraction", "without cloud", "with cloud", "normalized signal"])
        self.ui_atom.cloud_combo.currentIndexChanged.connect(
            lambda: combo_current_change(self.ui_atom.atom, self.ui_atom, self.ui_atom.cloud_combo.currentIndex()))

        # BTN CALCULATE ABSORPTION
        self.calc_by_abs_imaging = PyPushButton(
            text="Calculate single absorption",
            radius=3,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )

        self.calc_by_abs_imaging.clicked.connect(
            lambda: calculate_atom_number(self.ui_atom.atom, self.ui_atom, self.ui_atom.atom.getCloudArray(),
                                          self.ui_atom.atom.getNonCloudArray()))
        # ADD LAYOUT
        self.ui_atom.load_pages.absorption_single_imaging_layout.addWidget(self.calc_by_abs_imaging)

        # CLOUD PARAMETER BTNS
        self.ui_atom.load_pages.btn_atom_add_cloud_parameters.clicked.connect(
            lambda: add_cloud_parameters(self.ui_atom.atom, self.ui_atom))

        self.ui_atom.load_pages.btn_atom_clear_cloud_parameters.clicked.connect(
            lambda: clear_cloud_parameters(self.ui_atom.atom, self.ui_atom))


        # FIT 2D GAUSSIAN
        self.ui_atom.load_pages.btn_atom_fit_2d_gaussian.clicked.connect(
            lambda: fit_gaussian_shape(self.ui_atom.atom, self.ui_atom))

        self.ui_atom.load_pages.btn_atom_clear_fit.clicked.connect(lambda: clear_fit(self.ui_atom.atom, self.ui_atom))

        self.ui_atom.load_pages.btn_atom_guess_fit.clicked.connect(
            lambda: guess_params(self.ui_atom.atom, self.ui_atom))

        # AUTOMATIC PLOT SETUP
        self.atom_graph_send_to_analysis = PyPushButton(
            text="to Analysis",
            radius=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        # self.atom_graph_send_to_analysis.clicked.connect()

        self.atom_graph_send_to_excel = PyPushButton(
            text="to Excel",
            radius=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.atom_graph_send_to_excel.clicked.connect(
            lambda: export_to_excel(self.ui_atom.atom, self.ui_atom, self.ui_atom.graph_cloud_combo.currentIndex()))
        self.atom_graph_send_to_analysis.clicked.connect(
            lambda: export_to_analysis(self.ui_atom.atom, self.ui_atom, self.ui_atom.graph_cloud_combo.currentIndex()))

        self.ui_atom.load_pages.btn_atom_send_to_analysis_layout.addWidget(self.atom_graph_send_to_analysis)
        self.ui_atom.load_pages.btn_atom_send_to_excel_layout.addWidget(self.atom_graph_send_to_excel)

        # AUTOMATIC CLOUD - COMBOBOX
        self.ui_atom.graph_cloud_combo.addItems(["Number of Atoms", "Sigma x", "Sigma y", "Parameter"])
        self.ui_atom.graph_cloud_combo.currentIndexChanged.connect(
            lambda: graph_combo_current_change(self.ui_atom.atom, self.ui_atom,
                                               self.ui_atom.graph_cloud_combo.currentIndex()))


        # BTN CALCULATE SEQUENCE
        self.calc_automatic = PyPushButton(
            text="Calculate Sequence",
            radius=3,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )

        self.calc_automatic.clicked.connect(lambda: calculate_automatic_sequence(self.ui_atom.atom, self.ui_atom,
                                                                                 self.ui_atom.graph_cloud_combo.currentIndex()))
        # ADD LAYOUT
        self.ui_atom.load_pages.sequence_imaging_layout.addWidget(self.calc_automatic)

        # INITIALIZE CLOUD GRAPH
        self.graph.addItem(self.spots)
        self.graph.showGrid(x=True, y=True)
        self.graph.addLegend()

        self.spots.sigClicked.connect(lambda plot, points: clickedPoint(plot, points, self.ui_atom.atom, self.ui_atom))

        # ///////////////////////////////////////////////////////////////
        # END -  WIDGETS
        # ///////////////////////////////////////////////////////////////
