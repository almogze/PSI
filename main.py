# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.uis.api.instances import Instances
from gui.uis.windows.atom_window import UI_AtomWindow, SetupAtomWindow
from gui.uis.windows.analysis_window import *
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP WINDOWS
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        self.ui_analysis = UI_AnalysisWindow()
        self.ui_analysis.setup_ui_analysis(self, self.ui)

        self.ui_atom = UI_AtomWindow()
        self.ui_atom.setup_ui_atom(self, self.ui)

        # needed in order to link ui_atom and ui_analysis together
        self.instances = Instances(ui_analysis=self.ui_analysis, ui_atom=self.ui_atom)
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP WINDOWS
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)
        SetupAtomWindow.setup_gui_atom(self)
        SetupAnalysisWindow.setup_gui_analysis(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////

        # OPEN MAIN PAGE
        if btn.objectName() == "btn_home":
            #Select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            #Load page
            MainFunctions.set_page(self, self.ui.load_pages.page_main)
            MainFunctions.set_left_column_menu(
                self,
                menu=self.ui.left_column.menus.menu_empty,
                title="General Settings",
                icon_path=Functions.set_svg_icon("icon_settings.svg")
            )

        # OPEN ATOM PAGE
        if btn.objectName() == "btn_atom":
            #Select file
            self.ui.left_menu.select_only_one(btn.objectName())

            #Load page
            MainFunctions.set_page(self, self.ui.load_pages.page_atom)
            MainFunctions.set_left_column_menu(
                self,
                menu=self.ui.left_column.menus.menu_atom,
                title="Atom Settings",
                icon_path=Functions.set_svg_icon("icon_settings.svg")
            )

        # OPEN FRINGES PAGE
        if btn.objectName() == "btn_fringes":
            #Select file
            self.ui.left_menu.select_only_one(btn.objectName())

            #Load page
            MainFunctions.set_page(self, self.ui.load_pages.page_fringes)
            MainFunctions.set_left_column_menu(
                self,
                menu=self.ui.left_column.menus.menu_fringes,
                title="Fringes Settings",
                icon_path=Functions.set_svg_icon("icon_settings.svg")
            )

        # OPEN ANALYSIS PAGE
        if btn.objectName() == "btn_analysis":
            #Select file
            self.ui.left_menu.select_only_one(btn.objectName())

            #Load page
            MainFunctions.set_page(self, self.ui.load_pages.page_analysis)
            MainFunctions.set_left_column_menu(
                self,
                menu=self.ui.left_column.menus.menu_analysis,
                title="Analysis Settings",
                icon_path=Functions.set_svg_icon("icon_settings.svg")
            )

        # OPEN SETTINGS
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                #if btn.objectName() == "btn_close_left_column":
                self.ui.left_menu.deselect_all_tab()

                    # Show / Hide
                MainFunctions.toggle_left_column(self)

                # Select tab
                self.ui.left_menu.select_only_one_tab(btn.objectName())


        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn            
            top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            top_settings.set_active_tab(False)            

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())