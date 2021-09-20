# IMPORT PACKAGES FOR ANALYSING
# ///////////////////////////////////////////////////////////////
import string

import pandas as pd
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

def open_dialog_box_analysis(analysis: Analysis, switch: string, ui_analysis: UI_AnalysisWindow) -> None:
    error = QMessageBox()
    error.setWindowTitle("Error")
    error.setIcon(QMessageBox.Critical)

    filename = QFileDialog.getOpenFileName()
    if switch == "excel_file":
        analysis.setExcelPath(filename[0])
        print(analysis.getExcelPath())
        if not analysis.checkExcelFormat():
            print("file is not in excel format!")
            error.setText("File must be in xlsx format")
            error.exec()
        else:
            ui_analysis.load_pages.lineEdit_analysis_excel_name.setText(analysis.getExcelPath())
            excel_file = pd.ExcelFile(analysis.getExcelPath())
            ui_analysis.load_pages.comboBox_analysis_excel_sheet_names.addItems(excel_file.sheet_names)
            print("Sheet names: ", excel_file.sheet_names)


def send_excel_parameters(analysis: Analysis, ui_analysis: UI_AnalysisWindow) -> None:
    error = QMessageBox()
    error.setWindowTitle("Error")
    error.setIcon(QMessageBox.Critical)

    # Collecting Excel's groupbox parameters into a boolean list
    # List represent the result of each method
    bool_list = [analysis.setSheetName(ui_analysis.load_pages.comboBox_analysis_excel_sheet_names.currentText()),
                 analysis.setExcelPath(ui_analysis.load_pages.lineEdit_analysis_excel_name.text())]
    # All methods succeed
    if all(bool_list):
        if not analysis.checkExcelFormat():
            print("file is not in excel format!")
            error.setText("File must be in xlsx format")
            error.exec()
        else:
            if analysis.readExcel():  # Create data frame related excel path
                print("Created Data Frame from excel path")
            if analysis.initializeAxis():
                initialize_excel_axis(ui_analysis.analysis.getExcelAxis(), ui_analysis)
                print("Axis initialization succeed")
    else:
        print("Missing excel parameters information!")
        error.setText("Missing data, please check that all parameters are loaded")
        error.exec()


def initialize_excel_axis(axis: np.ndarray, ui_analysis: UI_AnalysisWindow) -> None:
    ui_analysis.load_pages.comboBox_analysis_x_axis.addItems(axis)
    ui_analysis.load_pages.comboBox_analysis_y_axis.addItems(axis)
    ui_analysis.load_pages.comboBox_analysis_x_error.addItems(np.append(axis, "None"))
    ui_analysis.load_pages.comboBox_analysis_y_error.addItems(np.append(axis, "None"))


def fit_analysis_data(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    set_data(analysis, ui_analysis)
    set_data_2_graph(analysis, ui_analysis)
    ui_analysis.graph.setTitle(title=ui_analysis.load_pages.lineEdit_analysis_main_title.text())
    ui_analysis.graph.setLabel('left', ui_analysis.load_pages.lineEdit_analysis_x_title.text(), units='X')
    ui_analysis.graph.setLabel('bottom', ui_analysis.load_pages.lineEdit_analysis_y_title.text(), units='Y')


def get_axis_labels(ui_analysis: UI_AnalysisWindow) -> np.array:
    x_name = ui_analysis.load_pages.comboBox_analysis_x_axis.currentText()
    y_name = ui_analysis.load_pages.comboBox_analysis_y_axis.currentText()
    dx_name = ui_analysis.load_pages.comboBox_analysis_x_error.currentText()
    dy_name = ui_analysis.load_pages.comboBox_analysis_y_error.currentText()
    return [x_name, y_name, dx_name, dy_name]


def set_data(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    df: pd.DataFrame = analysis.getDataFrame()
    labels = get_axis_labels(ui_analysis)
    x = df[labels[0]].values
    y = df[labels[1]].values
    if labels[2] == "None":
        dx = None
    else:
        dx = df[labels[2]].values
    if labels[3] == "None":
        dy = None
    else:
        dy = df[labels[3]].values
    ui_analysis.analysis.setFitData(x, y, dx, dy)


def set_parameters(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    analysis.fit.set_a_initial(ui_analysis.load_pages.lineEdit_analysis_initial_a.text())
    analysis.fit.set_b_initial(ui_analysis.load_pages.lineEdit_analysis_initial_b.text())
    analysis.fit.set_a_limits(ui_analysis.load_pages.lineEdit_analysis_s_limit_a, ui_analysis.load_pages.
                              lineEdit_analysis_f_limit_a)
    analysis.fit.set_b_limits(ui_analysis.load_pages.lineEdit_analysis_s_limit_b, ui_analysis.load_pages.
                              lineEdit_analysis_f_limit_b)


# Return an array of two rgb colors, one for plot line and one for plot symbol
def get_graph_rgb_colors(ui_analysis: UI_AnalysisWindow) -> np.array:
    plot_line_r = ui_analysis.load_pages.lineEdit_analysis_plot_line_color_r.text()
    plot_line_g = ui_analysis.load_pages.lineEdit_analysis_plot_line_color_g.text()
    plot_line_b = ui_analysis.load_pages.lineEdit_analysis_plot_line_color_b.text()
    plot_r = ui_analysis.load_pages.lineEdit_analysis_plot_color_r.text()
    plot_g = ui_analysis.load_pages.lineEdit_analysis_plot_color_g.text()
    plot_b = ui_analysis.load_pages.lineEdit_analysis_plot_color_b.text()
    return [plot_line_r, plot_line_g, plot_line_b, plot_r, plot_g, plot_b]


def set_data_2_graph(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    rgbs = get_graph_rgb_colors(ui_analysis)
    print(rgbs)
    if all(map(lambda s: s != "" and 0 <= int(s) < 256, rgbs)):
        print("1")
        ui_analysis.graph.plot(analysis.fit.get_x_array(), analysis.fit.get_y_array(), symbol='o', pen=(rgbs[0], rgbs[1]
                                                                                                        , rgbs[2]),
                               symbolBrush=(rgbs[3], rgbs[4], rgbs[5]),
                               name=ui_analysis.load_pages.lineEdit_analysis_main_title.text())
    elif all(map(lambda s: s != "" and 0 <= int(s) < 256, rgbs[:3])):
        print("2")
        ui_analysis.graph.plot(analysis.fit.get_x_array(), analysis.fit.get_y_array(),
                               symbolBrush=(rgbs[3], rgbs[4], rgbs[5]),
                               name=ui_analysis.load_pages.lineEdit_analysis_main_title.text())
    elif all(map(lambda s: s != "" and 0 <= int(s) < 256, rgbs[3:])):
        print("3")
        ui_analysis.graph.plot(analysis.fit.get_x_array(), analysis.fit.get_y_array(), symbol='o',
                               pen=(rgbs[0], rgbs[1], rgbs[2]),
                               name=ui_analysis.load_pages.lineEdit_analysis_main_title.text())
    else:
        print("4")
        ui_analysis.graph.plot(analysis.fit.get_x_array(), analysis.fit.get_y_array(), symbol='o',
                               name=ui_analysis.load_pages.lineEdit_analysis_main_title.text())


def matplotlib_fit_analysis_data(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    return None


def clean_all_analysis_screen(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    return None


def test_define():
    print("test!")
