# IMPORT PACKAGES FOR ANALYSING
# ///////////////////////////////////////////////////////////////
import string

import pandas as pd
from PIL import Image
import numpy as np
import os
from PySide6.QtWidgets import QFileDialog
from iminuit import Minuit
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText

from gui.uis.api.atom import Atom
from gui.uis.api.analysis import Analysis
from gui.uis.windows.atom_window import UI_AtomWindow
from gui.uis.windows.analysis_window import UI_AnalysisWindow
from gui.uis.api.fitting import Fit
from gui.widgets import *
from qt_core import *


def open_dialog_box_atom(atom: Atom, ui_atom: UI_AtomWindow, switch: string) -> None:
    filename = QFileDialog.getOpenFileName()
    if switch == "no_cloud":
        atom.setNoCloudPath(filename[0])
        ui_atom.load_pages.lineEdit_without_cloud_path.setText(filename[0])
        print(atom.getNoCloudPath())
    elif switch == "with_cloud":
        atom.setCloudPath(filename[0])
        ui_atom.load_pages.lineEdit_with_cloud_path.setText(filename[0])
        print(atom.getCloudPath())


def calculate_atom_number(atom: Atom, ui_atom: UI_AtomWindow) -> None:
    if atom.clearToLoad():
        atom_number = atom.calculateAtomNumber()
        print(atom_number)
        ui_atom.load_pages.label_atom_number.setText(str(atom_number))
    else:
        error = QMessageBox()
        error.setWindowTitle("Error")
        print("Can not Calculate! Please load images first")
        error.setText("Please load images first")
        error.exec()


def load_image(atom: Atom, ui_atom: UI_AtomWindow) -> None:
    error = QMessageBox()
    error.setWindowTitle("Error")
    error.setIcon(QMessageBox.Critical)
    if checkAndSet(atom, error):
        checkAndLoad(atom, error, ui_atom)


def checkAndSet(atom: Atom, error: QMessageBox) -> bool:
    condition = bool(True)
    if not atom.clearToSet():
        print("Can not set images! Please check images path")
        error.setText("Please check images path")
        error.exec()
        condition = bool(False)
    elif atom.checkImageFormatJPG():
        atom.setImageJPG()
    elif atom.checkImageFormatBIN():
        atom.setImageBIN()
    else:
        error.setText("images are not in format")
        error.exec()
        print("At least one of the images is not in jpg or bin format")
        condition = bool(False)
    return condition


def checkAndLoad(atom: Atom, error: QMessageBox, ui_atom: UI_AtomWindow) -> None:
    if not atom.clearToLoad():
        print("Can not load images! Please check images numpy arrays")
        error.setText("Please check images numpy arrays")
        error.exec()
    else:
        loaded_image = atom.loadImage(ui_atom.cloud_combo.currentIndex())
        if loaded_image is None:
            print("ComboBox index is not Valid")
        else:
            # ui_atom.load_pages.ImageView_Atom.setImage(loaded_image)
            ui_atom.image.setImage(image=loaded_image)
            ui_atom.inf1.setBounds([0, len(loaded_image)])
            ui_atom.inf2.setBounds([0, len(loaded_image[0])])

            ui_atom.graph_top.plot(np.arange(len(loaded_image)), loaded_image[:, int(ui_atom.inf2.value())])
            ui_atom.graph_right.plot(loaded_image[int(ui_atom.inf1.value())], np.arange(len(loaded_image[0])))


def clear_image(atom: Atom, ui_atom: UI_AtomWindow) -> None:
    atom.clearImage()
    ui_atom.load_pages.ImageView_Atom.clear()
    ui_atom.load_pages.label_atom_number.setText(str(0))
    ui_atom.load_pages.label_cloud_temperature.setText(str(0))
    ui_atom.load_pages.lineEdit_with_cloud_path.clear()
    ui_atom.load_pages.lineEdit_without_cloud_path.clear()


def combo_current_change(atom: Atom, ui_atom: UI_AtomWindow, ind: int) -> None:
    loaded_image = atom.loadImage(ind)
    if loaded_image is not None:
        ui_atom.image.setImage(image=loaded_image)
        ui_atom.graph_top.plot(np.arange(len(loaded_image)), loaded_image[:, int(ui_atom.inf2.value())])
        ui_atom.graph_right.plot(loaded_image[ui_atom.inf1.value()], np.arange(len(loaded_image[0])))
    else:
        print("ComboBox index is not Valid")


def update_top_graph(atom: Atom, ui_atom: UI_AtomWindow):
    if atom.clearToLoad():
        loaded_image = atom.loadImage(ui_atom.cloud_combo.currentIndex())
        ui_atom.graph_top.clear()
        ui_atom.graph_top.plot(np.arange(len(loaded_image)), loaded_image[:, int(ui_atom.inf2.value())])


def update_right_graph(atom: Atom, ui_atom: UI_AtomWindow):
    if atom.clearToLoad():
        loaded_image = atom.loadImage(ui_atom.cloud_combo.currentIndex())
        ui_atom.graph_right.clear()
        ui_atom.graph_right.plot(loaded_image[int(ui_atom.inf1.value())], np.arange(len(loaded_image[0])))


def update_region_image_view(viewRange, ui_atom: UI_AtomWindow):
    # preventing infinite loop by disabling other signals
    ui_atom.graph_top.sigRangeChanged.disconnect()
    ui_atom.graph_right.sigRangeChanged.disconnect()

    rgn_x = viewRange[0]
    rgn_y = viewRange[1]
    ui_atom.graph_top.setXRange(rgn_x[0], rgn_x[1])
    ui_atom.graph_right.setYRange(rgn_y[0], rgn_y[1])
    # activating again other signals
    ui_atom.graph_top.sigRangeChanged.connect(lambda window, rgn: update_region_top(rgn, ui_atom))
    ui_atom.graph_right.sigRangeChanged.connect(lambda window, rgn: update_region_right(rgn, ui_atom))


def update_region_top(viewRange, ui_atom: UI_AtomWindow):
    # preventing infinite loop by disabling other signals
    ui_atom.image_view.sigRangeChanged.disconnect()

    rgn_x = viewRange[0]
    ui_atom.image_view.setXRange(rgn_x[0], rgn_x[1])
    # activating again other signals
    ui_atom.image_view.sigRangeChanged.connect(lambda window, rgn: update_region_image_view(rgn, ui_atom))


def update_region_right(viewRange, ui_atom: UI_AtomWindow):
    # preventing infinite loop by disabling other signals
    ui_atom.image_view.sigRangeChanged.disconnect()

    rgn_y = viewRange[1]
    ui_atom.image_view.setYRange(rgn_y[0], rgn_y[1])
    # activating again other signals
    ui_atom.image_view.sigRangeChanged.connect(lambda window, rgn: update_region_image_view(rgn, ui_atom))
