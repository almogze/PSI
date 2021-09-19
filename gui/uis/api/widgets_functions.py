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
            ui_atom.load_pages.ImageView_Atom.setImage(loaded_image)


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
        ui_atom.load_pages.ImageView_Atom.setImage(loaded_image)
    else:
        print("ComboBox index is not Valid")


# ANALYSIS PAGE FUNCTIONALITY

def open_dialog_box_analysis(analysis: Analysis, switch: string) -> None:
    filename = QFileDialog.getOpenFileName()
    if switch == "excel_file":
        analysis.setExcelPath(filename[0])
        print(analysis.getExcelPath())


def load_excel_loc_to_lineEdit(analysis: Analysis, sheet_name: string, ui_analysis: UI_AnalysisWindow) -> None:
    print(sheet_name)
    analysis.sheet_name = sheet_name
    ui_analysis.load_pages.lineEdit_analysis_excel_name.setText(analysis.getExcelPath())
    ui_analysis.load_pages.lineEdit_analysis_sheet_name.setText(analysis.getSheetName())


def send_excel_parameters(analysis: Analysis, ui_analysis: UI_AnalysisWindow) -> None:
    error = QMessageBox()
    error.setWindowTitle("Error")
    error.setIcon(QMessageBox.Critical)

    x_name = ui_analysis.load_pages.lineEdit_analysis_x_column.text()
    dx_name = ui_analysis.load_pages.lineEdit_analysis_x_column_error.text()
    y_name = ui_analysis.load_pages.lineEdit_analysis_y_column.text()
    dy_name = ui_analysis.load_pages.lineEdit_analysis_y_column_error.text()

    # Collecting Excel's groupbox parameters into a boolean list
    # List represent the result of each method
    bool_list = [analysis.setSheetName(ui_analysis.load_pages.lineEdit_analysis_sheet_name.text()),
                 analysis.setColumnsNames(x_name, y_name, dx_name, dy_name),
                 analysis.setExcelPath(ui_analysis.load_pages.lineEdit_analysis_excel_name.text())]
    # All methods succeed
    if all(bool_list):
        print("All parameters sent")
        if not analysis.checkExcelFormat():
            print("file is not in excel format!")
            error.setText("File must be in xlsx format")
            error.exec()
    else:
        print("Missing excel parameters information!")
        error.setText("Missing data, please check that all parameters are loaded")
        error.exec()


def test_define():
    print("test!")
