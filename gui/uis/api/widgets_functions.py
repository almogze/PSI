# IMPORT PACKAGES FOR ANALYSING
# ///////////////////////////////////////////////////////////////
import string

from PIL import Image
import numpy as np
import os
from PySide6.QtWidgets import QFileDialog

from gui.uis.api.atom import Atom
from gui.uis.api.analysis import Analysis
from gui.uis.windows.atom_window import UI_AtomWindow
from gui.uis.windows.analysis_window import UI_AnalysisWindow
from gui.widgets import *
from qt_core import *


# ATOM PAGE FUNCTIONALITY

def open_dialog_box_atom(atom: Atom, switch: string) -> None:
    filename = QFileDialog.getOpenFileName()
    if switch == "no_cloud":
        atom.setNoCloudPath(filename[0])
        print(atom.getNoCloudPath())
    elif switch == "with_cloud":
        atom.setCloudPath(filename[0])
        print(atom.getCloudPath())


# ANALYSIS PAGE FUNCTIONALITY

def open_dialog_box_analysis(analysis: Analysis, switch: string) -> None:
    filename = QFileDialog.getOpenFileName()
    if switch == "excel_file":
        analysis.setExcelPath(filename[0])
        print(analysis.getExcelPath())


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
            ui_atom.load_pages.ImageView_Atom.setImage(loaded_image)


def clear_image(atom: Atom, ui_atom: UI_AtomWindow) -> None:
    # atom.clearImage()
    ui_atom.load_pages.ImageView_Atom.clear()


def combo_current_change(atom: Atom, ui_atom: UI_AtomWindow, ind: int) -> None:
    loaded_iamge = atom.loadImage(ind)
    if loaded_iamge is not None:
        ui_atom.load_pages.ImageView_Atom.setImage(loaded_iamge)
    else:
        print("ComboBox index is not Valid")


def send_excel_parameters(analysis: Analysis, sheet_name: string, ui_analysis: UI_AnalysisWindow) -> None:
    print(sheet_name)
    analysis.sheet_name = sheet_name
    ui_analysis.load_pages.lineEdit_analysis_excel_name.setText(analysis.getExcelPath())
    ui_analysis.load_pages.lineEdit_analysis_sheet_name.setText(analysis.getSheetName())


def test_define():
    print("test!")