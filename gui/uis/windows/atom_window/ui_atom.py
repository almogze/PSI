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
from pyqtgraph import PlotItem, ImageItem

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

        # GRAPHIC SETTINGS
        # ///////////////////////////////////////////////////////////////
        self.image_view: PlotItem = self.load_pages.ImageView_Atom.addPlot()
        self.image_view.getAxis('left').setLabel('y axis pixels')
        self.image_view.getAxis('bottom').setLabel('x axis pixels')

        cmap = pg.colormap.get('CET-L8')
        self.bar = pg.ColorBarItem(
            interactive=True, values=(-5, 5), cmap=cmap,
            label='pixel intensity color'
        )

        self.image: ImageItem = ImageItem()

        self.graph_top: PlotItem = self.load_pages.ImageView_Atom_top.addPlot()
        self.graph_top.getAxis('bottom').setStyle(showValues=False)
        self.graph_top.showAxis('top')
        self.graph_top.getAxis('top').setLabel('x axis pixels')
        self.graph_top.getAxis('left').setLabel('pixels intensity')

        self.graph_right: PlotItem = self.load_pages.ImageView_Atom_right.addPlot()
        self.graph_right.getAxis('left').setStyle(showValues=False)
        self.graph_right.getAxis('bottom').setLabel('pixels intensity')
        self.graph_right.showAxis('right')
        self.graph_right.getAxis('right').setLabel('y axis pixels')

        self.image_view.addItem(self.image)
        self.bar.setImageItem(self.image, insert_in=self.image_view)

        # Add lines to image
        self.inf1 = pg.InfiniteLine(movable=True, angle=90, label='x pixel={value:0.0f}',
                               labelOpts={'color': (200, 200, 100), 'fill': (200, 200, 200, 50),
                                          'movable': True})
        self.inf2 = pg.InfiniteLine(movable=True, angle=0,
                               label='y pixel={value:0.0f}',
                               labelOpts={'color': (200, 200, 100), 'movable': True, 'fill': (200, 200, 200, 50)})

        self.image_view.addItem(self.inf1)
        self.image_view.addItem(self.inf2)

        self.inf1.sigPositionChanged.connect()
        self.inf2.sigPositionChanged.connect()

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes: Themes = themes.items
