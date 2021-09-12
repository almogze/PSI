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
    if atom.clearToSet():
        if not atom.checkImageFormat():
            error.setText("image is not in format jpg")
            error.exec()
            print("At least one of the cloud images is not in jpg format")
        else:
            atom.setImage()
            if atom.clearToLoad():
                loaded_iamge = atom.loadImage(ui_atom.cloud_combo.currentIndex())
                if loaded_iamge is not None:
                    ui_atom.load_pages.ImageView_Atom.setImage(loaded_iamge)
                else:
                    print("ComboBox index is not Valid")
            else:
                print("Can not load images! Please check images numpy arrays")
                error.setText("Please check images numpy arrays")
                error.exec()
    else:
        print("Can not set images! Please check images path")
        error.setText("Please check images path")
        error.exec()


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