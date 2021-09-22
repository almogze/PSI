# IMPORT PACKAGES FOR ANALYSING
# ///////////////////////////////////////////////////////////////
import string

import pandas as pd
from PIL import Image
import numpy as np
import os
from PySide6.QtWidgets import QFileDialog
from iminuit import Minuit

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


def fit_analysis_data(analysis: Analysis, ui_analysis: UI_AnalysisWindow) -> None:
    # Initialize axis and parameters with user's data
    set_parameters(analysis, ui_analysis)
    set_data(analysis, ui_analysis)
    # Plot data on a graph
    set_data_2_graph(analysis, ui_analysis)


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
    # Set fit function as user marked
    analysis.fit.set_function(
        analysis.fun_fits.fun_fit_array[ui_analysis.load_pages.comboBox_analysis_fit_function.currentIndex()])
    # Activate optimization with the current cost function
    if dx is None and dy is None:
        analysis.fit.opt_by_scipy()
        plot_opt_func(analysis, ui_analysis)
    else:
        opt: Minuit = analysis.fit.optimize()
        plot_opt_func_2(opt, analysis, ui_analysis)


def set_parameters(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    analysis.fit.set_a_initial(float(ui_analysis.load_pages.lineEdit_analysis_initial_a.text()))
    analysis.fit.set_b_initial(float(ui_analysis.load_pages.lineEdit_analysis_initial_b.text()))
    analysis.fit.set_a_limits(float(ui_analysis.load_pages.lineEdit_analysis_s_limit_a.text()),
                              float(ui_analysis.load_pages.lineEdit_analysis_f_limit_a.text()))
    analysis.fit.set_b_limits(float(ui_analysis.load_pages.lineEdit_analysis_s_limit_b.text()),
                              float(ui_analysis.load_pages.lineEdit_analysis_f_limit_b.text()))


# Return an array of two rgb colors, one for plot line and one for plot symbol
def get_graph_colors(ui_analysis: UI_AnalysisWindow) -> np.array:
    colors = [(55, 55, 55), "b", "g", "r", "c", "m", "y", "k", "w"]
    plot_line_color = colors[ui_analysis.load_pages.comboBox_analysis_plot_line_color.currentIndex()]
    plot_symbol_color = colors[ui_analysis.load_pages.comboBox_analysis_plot_symbol_color.currentIndex()]
    return [plot_line_color, plot_symbol_color]


def set_data_2_graph(analysis: Analysis, ui_analysis: UI_AnalysisWindow) -> None:
    colors = get_graph_colors(ui_analysis)
    ui_analysis.graph.plot(analysis.fit.get_x_array(), analysis.fit.get_y_array(),
                           symbol='o', pen=colors[0], symbolBrush=colors[1], symbolPen='w', symbolSize=4,
                           name=ui_analysis.load_pages.lineEdit_analysis_main_title.text())
    # Add titles and units
    ui_analysis.graph.setTitle(title=ui_analysis.load_pages.lineEdit_analysis_main_title.text())
    ui_analysis.graph.setLabel('left', ui_analysis.load_pages.lineEdit_analysis_x_title.text(),
                               units=ui_analysis.load_pages.lineEdit_analysis_x_units.text())
    ui_analysis.graph.setLabel('bottom', ui_analysis.load_pages.lineEdit_analysis_y_title.text(),
                               units=ui_analysis.load_pages.lineEdit_analysis_y_units.text())


def plot_opt_func(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    x = analysis.fit.get_x_array()
    function = analysis.fit.get_function()
    func_x = np.linspace(x[0], x[-1], 10000)
    params = analysis.fit.get_params_array()
    y_fit = function(func_x, *params)
    ui_analysis.graph.plot(func_x, y_fit)


def plot_opt_func_2(opt: Minuit, analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    par = opt.parameters
    fit_arg = opt.fitarg
    x = analysis.fit.get_x_array()
    function = analysis.fit.get_function()
    par_values = []
    for _ in (par):
        par_values.append(fit_arg[_])
    func_x = np.linspace(x[0], x[-1], 10000)  # 10000 linearly spaced numbers
    y_fit = function(func_x, *par_values)
    ui_analysis.graph.plot(func_x, y_fit)  # plot the function over 10k points covering the x axis


def matplotlib_fit_analysis_data(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    return None


def clean_all_analysis_screen(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    return None


def test_define():
    print("test!")
