# IMPORT PACKAGES FOR ANALYSING
# ///////////////////////////////////////////////////////////////
import string

import lmfit.models
import pandas
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


def open_dialog_box_analysis(analysis: Analysis, switch: string, ui_analysis: UI_AnalysisWindow) -> None:
    filename = QFileDialog.getOpenFileName(caption="Open Data File", filter="All Files();;Excel Files (*.xlsx)")
    if switch == "excel_file":
        analysis.setExcelPath(filename[0])
        print(analysis.getExcelPath())
        if not analysis.checkExcelFormat():
            pop_error("file is not in excel format!", "File must be in xlsx format")
        else:
            ui_analysis.load_pages.lineEdit_analysis_excel_name.setText(analysis.getExcelPath())
            excel_file = pd.ExcelFile(analysis.getExcelPath())
            ui_analysis.load_pages.comboBox_analysis_excel_sheet_names.addItems(excel_file.sheet_names)
            print("Sheet names: ", excel_file.sheet_names)


def send_excel_parameters(analysis: Analysis, ui_analysis: UI_AnalysisWindow) -> None:
    # Collecting Excel's groupbox parameters into a boolean list
    # List represent the result of each method
    bool_list = [analysis.setSheetName(ui_analysis.load_pages.comboBox_analysis_excel_sheet_names.currentText()),
                 analysis.setExcelPath(ui_analysis.load_pages.lineEdit_analysis_excel_name.text())]
    # All methods succeed
    if all(bool_list):
        if not analysis.checkExcelFormat():
            pop_error("file is not in excel format!", "File must be in xlsx format")
        else:
            if analysis.readExcel():  # Create data frame related excel path
                print("Created Data Frame from excel path")
            if analysis.initializeAxis():
                initialize_excel_axis(ui_analysis.analysis.getExcelAxis(), ui_analysis)
                print("Axis initialization succeed")
    else:
        pop_error("Missing excel parameters information!", "Missing data, please check that all parameters are loaded")


def fun_fit_changed(analysis: Analysis, ui_analysis: UI_AnalysisWindow, ind: int):
    # Set the fit function label to match the new function that chosen
    ui_analysis.load_pages.label_analysis_fit_function.setText(analysis.fun_texts.fun_non_latex_texts_array[ind])
    # number of parameters of new fit function
    new_num_of_params = analysis.fun_fits.number_of_params[ind]
    # Check if the new fit function has the same amount of parameters
    if new_num_of_params == analysis.fit.get_func_par_num():
        return
    else:
        analysis.fit.set_func_par_num(new_num_of_params)
        refresh_params_data_enable(ui_analysis, new_num_of_params)


def initialize_excel_axis(axis: np.ndarray, ui_analysis: UI_AnalysisWindow) -> None:
    ui_analysis.load_pages.comboBox_analysis_x_axis.clear()
    ui_analysis.load_pages.comboBox_analysis_y_axis.clear()
    ui_analysis.load_pages.comboBox_analysis_x_error.clear()
    ui_analysis.load_pages.comboBox_analysis_y_error.clear()
    print("clean old axis")
    ui_analysis.load_pages.comboBox_analysis_x_axis.addItems(axis)
    ui_analysis.load_pages.comboBox_analysis_y_axis.addItems(axis)
    ui_analysis.load_pages.comboBox_analysis_x_error.addItems(np.append("None", axis))
    ui_analysis.load_pages.comboBox_analysis_y_error.addItems(np.append("None", axis))

    ui_analysis.load_pages.lineEdit_analysis_steps.setText("1")
    ui_analysis.load_pages.lineEdit_analysis_set_x_i.setText("0")
    ui_analysis.load_pages.lineEdit_analysis_set_x_f.setText("")


def plot_analysis_data(analysis: Analysis, ui_analysis: UI_AnalysisWindow) -> None:
    set_data(analysis, ui_analysis)
    # enabling the option to guess params
    ui_analysis.load_pages.pushButton_analyisis_guess_params.setEnabled(True)

    set_data_2_graph(analysis, ui_analysis)


def optimize_analysis_data(analysis: Analysis, ui_analysis: UI_AnalysisWindow) -> None:
    ui_analysis.analysis.fit = Fit()
    # Keep the number of parameters in the fit function
    fun_ind = ui_analysis.load_pages.comboBox_analysis_fit_function.currentIndex()
    analysis.fit.set_func_par_num(analysis.fun_fits.number_of_params[fun_ind])
    # initialize data
    set_data(analysis, ui_analysis)
    # Initialize parameters with user's data
    set_parameters(analysis, ui_analysis)
    # Activate optimization
    set_opt_and_plot(analysis, ui_analysis)
    # Update optimized parameters
    update_parameters(analysis, ui_analysis)


def get_axis_labels(ui_analysis: UI_AnalysisWindow) -> np.array:
    x_name = ui_analysis.load_pages.comboBox_analysis_x_axis.currentText()
    y_name = ui_analysis.load_pages.comboBox_analysis_y_axis.currentText()
    dx_name = ui_analysis.load_pages.comboBox_analysis_x_error.currentText()
    dy_name = ui_analysis.load_pages.comboBox_analysis_y_error.currentText()
    return [x_name, y_name, dx_name, dy_name]


def set_data(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    df: pd.DataFrame = analysis.getDataFrame()
    if not check_excel_columns(df):
        pop_error("excel columns are not int of float", "please check columns types")
    else:
        labels = get_axis_labels(ui_analysis)

        steps = int(ui_analysis.load_pages.lineEdit_analysis_steps.text())
        x_i = int(ui_analysis.load_pages.lineEdit_analysis_set_x_i.text())
        if ui_analysis.load_pages.lineEdit_analysis_set_x_f.text() == "":
            x_f = len(df[labels[0]].values)
        else:
            x_f = int(ui_analysis.load_pages.lineEdit_analysis_set_x_f.text())

        x = df[labels[0]].values[x_i:x_f]
        x = x[::steps]
        y = df[labels[1]].values[x_i:x_f]
        y = y[::steps]
        if labels[2] == "None":
            dx = None
        else:
            dx = df[labels[2]].values[x_i:x_f]
            dx = dx[::steps]
        if labels[3] == "None":
            dy = None
        else:
            dy = df[labels[3]].values[x_i:x_f]
            dy = dy[::steps]
        ui_analysis.analysis.setFitData(x, y, dx, dy)
        analysis.addPlot(x, y, ui_analysis.load_pages.lineEdit_analysis_curve_label.text(),
                         get_graph_colors(ui_analysis)[0])


def check_excel_columns(df: pandas.DataFrame) -> bool:
    if all(x == 'int64' or x == 'float64' for x in df.dtypes.values):
        return bool(True)
    else:
        return bool(False)


def pop_error(s1: string, s2: string):
    error = QMessageBox()
    error.setWindowTitle("Error")
    error.setIcon(QMessageBox.Critical)
    print(s1)
    error.setText(s2)
    error.exec()


def set_opt_and_plot(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    # Set fit function index as user marked
    fun_ind = ui_analysis.load_pages.comboBox_analysis_fit_function.currentIndex()
    fun_name = ui_analysis.load_pages.comboBox_analysis_fit_function.currentText()
    # Set the wanted fit function
    print(analysis.fun_texts.fun_texts_array[fun_ind])
    analysis.fit.set_function(analysis.fun_fits.fun_fit_array[fun_ind])
    # Keep the number of parameters in the fit function
    analysis.fit.set_func_par_num(analysis.fun_fits.number_of_params[fun_ind])
    # Activate optimization with the current cost function
    if analysis.fit.has_uncertainty():
        opt: Minuit = analysis.fit.optimize()
        ui_analysis.load_pages.lineEdit_analysis_chi2Ndof.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_chi2Ndof.setText(str(analysis.fit.get_chi_ndof()))
        ui_analysis.load_pages.lineEdit_analysis_chi2.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_chi2.setText(str(analysis.fit.get_chi2()))
    else:
        if generate_model_from_name(analysis, ui_analysis, fun_name) is not None:
            # fitting using the LMFIT library
            analysis.fit.opt_by_lmfit_generic(generate_model_from_name(analysis, ui_analysis, fun_name))

            ui_analysis.load_pages.lineEdit_analysis_chi2Ndof.setEnabled(False)
            ui_analysis.load_pages.lineEdit_analysis_chi2Ndof.setText("None")
            ui_analysis.load_pages.lineEdit_analysis_chi2.setEnabled(True)
            print(str(analysis.fit.get_chi_ndof()))
            ui_analysis.load_pages.lineEdit_analysis_chi2.setText(str(analysis.fit.get_chi_ndof()))
        else:
            analysis.fit.opt_by_scipy()
            ui_analysis.load_pages.lineEdit_analysis_chi2.setEnabled(False)
            ui_analysis.load_pages.lineEdit_analysis_chi2.setText("None")
            ui_analysis.load_pages.lineEdit_analysis_chi2Ndof.setEnabled(False)
            ui_analysis.load_pages.lineEdit_analysis_chi2Ndof.setText("None")
    # updating errors
    update_parameters_error(analysis, ui_analysis)
    # Plot data on a graph
    plot_opt_func(analysis, ui_analysis)


def generate_model_from_name(analysis: Analysis, ui_analysis: UI_AnalysisWindow, fun_name) -> lmfit.models:
    model = None
    # if fun_name == "Gaussian":
    #    model = lmfit.models.GaussianModel()
    #    analysis.fit.set_function(lmfit.lineshapes.gaussian)
    #    ui_analysis.load_pages.label_analysis_fit_function.setText(
    #        "f(x) = (a / (c * sqrt(2 * pi)) * e ^ ( -0.5 * ((x - b) ^ 2 / c ^ 2))")
    if fun_name == "Sine":
        model = lmfit.models.SineModel()
    elif fun_name == "Polynomial second degree":
        model = lmfit.models.QuadraticModel()
    elif fun_name == "Polynomial third degree":
        model = lmfit.models.PolynomialModel(degree=3)
    # elif fun_name == "Error Function" or fun_name == "Complementary Error Function":
    #    model = lmfit.models.StepModel(form='linear') + lmfit.models.ConstantModel()
    return model


def set_parameters(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    param_num = analysis.fit.get_func_par_num()
    analysis.fit.set_a_initial(float(ui_analysis.load_pages.lineEdit_analysis_initial_a.text()))
    analysis.fit.set_a_limits(float(ui_analysis.load_pages.lineEdit_analysis_s_limit_a.text()),
                              float(ui_analysis.load_pages.lineEdit_analysis_f_limit_a.text()))
    if param_num > 1:
        analysis.fit.set_b_initial(float(ui_analysis.load_pages.lineEdit_analysis_initial_b.text()))
        analysis.fit.set_b_limits(float(ui_analysis.load_pages.lineEdit_analysis_s_limit_b.text()),
                                  float(ui_analysis.load_pages.lineEdit_analysis_f_limit_b.text()))
        if param_num > 2:
            analysis.fit.set_c_initial(float(ui_analysis.load_pages.lineEdit_analysis_initial_c.text()))
            analysis.fit.set_c_limits(float(ui_analysis.load_pages.lineEdit_analysis_s_limit_c.text()),
                                      float(ui_analysis.load_pages.lineEdit_analysis_f_limit_c.text()))
            if param_num > 3:
                analysis.fit.set_d_initial(float(ui_analysis.load_pages.lineEdit_analysis_initial_d.text()))
                analysis.fit.set_d_limits(float(ui_analysis.load_pages.lineEdit_analysis_s_limit_d.text()),
                                          float(ui_analysis.load_pages.lineEdit_analysis_f_limit_d.text()))


def refresh_params_data_enable(ui_analysis: UI_AnalysisWindow, params_num: int):
    if params_num == 1:
        ui_analysis.load_pages.lineEdit_analysis_initial_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_param_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_err_a.setEnabled(True)

        ui_analysis.load_pages.lineEdit_analysis_initial_b.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_b.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_b.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_param_b.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_err_b.setEnabled(False)

        ui_analysis.load_pages.lineEdit_analysis_initial_c.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_c.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_c.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_param_c.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_err_c.setEnabled(False)

        ui_analysis.load_pages.lineEdit_analysis_initial_d.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_d.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_d.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_param_d.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_err_d.setEnabled(False)
        refresh_param_data_text(ui_analysis,
                                [["0", "-1000", "1000"], ["None", "None", "None"], ["None", "None", "None"],
                                 ["None", "None", "None"]])
    elif params_num == 2:
        ui_analysis.load_pages.lineEdit_analysis_initial_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_param_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_err_a.setEnabled(True)

        ui_analysis.load_pages.lineEdit_analysis_initial_b.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_b.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_b.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_param_b.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_err_b.setEnabled(True)

        ui_analysis.load_pages.lineEdit_analysis_initial_c.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_c.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_c.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_param_c.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_err_c.setEnabled(False)

        ui_analysis.load_pages.lineEdit_analysis_initial_d.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_d.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_d.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_param_d.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_err_d.setEnabled(False)
        # Check if the selected fit function is Normalized Gaussian
        if ui_analysis.load_pages.comboBox_analysis_fit_function.currentText() == "Normalized Gaussian":
            refresh_param_data_text(ui_analysis,
                                    [["1", "0.001", "1000"], ["1", "0.001", "1000"], ["None", "None", "None"],
                                     ["None", "None", "None"]])
        else:
            refresh_param_data_text(ui_analysis,
                                    [["0", "-1000", "1000"], ["0", "-1000", "1000"], ["None", "None", "None"],
                                     ["None", "None", "None"]])
    elif params_num == 3:
        ui_analysis.load_pages.lineEdit_analysis_initial_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_param_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_err_a.setEnabled(True)

        ui_analysis.load_pages.lineEdit_analysis_initial_b.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_b.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_b.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_param_b.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_err_b.setEnabled(True)

        ui_analysis.load_pages.lineEdit_analysis_initial_c.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_c.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_c.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_param_c.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_err_c.setEnabled(True)

        ui_analysis.load_pages.lineEdit_analysis_initial_d.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_d.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_d.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_param_d.setEnabled(False)
        ui_analysis.load_pages.lineEdit_analysis_err_d.setEnabled(False)
        # Check if the selected fit function is Gaussian
        if ui_analysis.load_pages.comboBox_analysis_fit_function.currentText() == "Gaussian":
            refresh_param_data_text(ui_analysis,
                                    [["1", "0.001", "1000"], ["1", "-1000", "1000"], ["1", "0.001", "1000"],
                                     ["None", "None", "None"]])
        else:
            refresh_param_data_text(ui_analysis,
                                    [["0", "-1000", "1000"], ["0", "-1000", "1000"], ["0", "-1000", "1000"],
                                     ["None", "None", "None"]])
    elif params_num == 4:
        ui_analysis.load_pages.lineEdit_analysis_initial_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_param_a.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_err_a.setEnabled(True)

        ui_analysis.load_pages.lineEdit_analysis_initial_b.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_b.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_b.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_param_b.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_err_b.setEnabled(True)

        ui_analysis.load_pages.lineEdit_analysis_initial_c.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_c.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_c.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_param_c.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_err_c.setEnabled(True)

        ui_analysis.load_pages.lineEdit_analysis_initial_d.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_s_limit_d.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_f_limit_d.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_param_d.setEnabled(True)
        ui_analysis.load_pages.lineEdit_analysis_err_d.setEnabled(True)
        # Check if the selected fit function is offset Gaussian
        if ui_analysis.load_pages.comboBox_analysis_fit_function.currentText() == "Offset Gaussian":
            refresh_param_data_text(ui_analysis,
                                    [["1", "0.001", "1000"], ["1", "-1000", "1000"], ["1", "0.001", "1000"],
                                     ["0", "-1000", "1000"]])
        else:
            refresh_param_data_text(ui_analysis,
                                    [["0", "-1000", "1000"], ["0", "-1000", "1000"], ["0", "-1000", "1000"],
                                     ["0", "-1000", "1000"]])


def refresh_param_data_text(ui_analysis: UI_AnalysisWindow, text_arr):
    ui_analysis.load_pages.lineEdit_analysis_initial_a.setText(text_arr[0][0])
    ui_analysis.load_pages.lineEdit_analysis_s_limit_a.setText(text_arr[0][1])
    ui_analysis.load_pages.lineEdit_analysis_f_limit_a.setText(text_arr[0][2])

    ui_analysis.load_pages.lineEdit_analysis_initial_b.setText(text_arr[1][0])
    ui_analysis.load_pages.lineEdit_analysis_s_limit_b.setText(text_arr[1][1])
    ui_analysis.load_pages.lineEdit_analysis_f_limit_b.setText(text_arr[1][2])

    ui_analysis.load_pages.lineEdit_analysis_initial_c.setText(text_arr[2][0])
    ui_analysis.load_pages.lineEdit_analysis_s_limit_c.setText(text_arr[2][1])
    ui_analysis.load_pages.lineEdit_analysis_f_limit_c.setText(text_arr[2][2])

    ui_analysis.load_pages.lineEdit_analysis_initial_d.setText(text_arr[3][0])
    ui_analysis.load_pages.lineEdit_analysis_s_limit_d.setText(text_arr[3][1])
    ui_analysis.load_pages.lineEdit_analysis_f_limit_d.setText(text_arr[3][2])


def update_parameters(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    num_of_params = analysis.fit.get_func_par_num()
    if num_of_params > 0:
        ui_analysis.load_pages.lineEdit_analysis_param_a.setText("%0.4f" % analysis.fit.get_a_parameter())
        if num_of_params > 1:
            ui_analysis.load_pages.lineEdit_analysis_param_b.setText("%0.4f" % analysis.fit.get_b_parameter())
            if num_of_params > 2:
                ui_analysis.load_pages.lineEdit_analysis_param_c.setText("%0.4f" % analysis.fit.get_c_parameter())
                if num_of_params > 3:
                    ui_analysis.load_pages.lineEdit_analysis_param_d.setText("%0.4f" % analysis.fit.get_d_parameter())


def update_parameters_error(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    num_of_params = analysis.fit.get_func_par_num()
    if num_of_params > 0 and analysis.fit.get_a_err_parameter() is not None:
        ui_analysis.load_pages.lineEdit_analysis_err_a.setText("%0.4f" % analysis.fit.get_a_err_parameter())
        if num_of_params > 1:
            ui_analysis.load_pages.lineEdit_analysis_err_b.setText("%0.4f" % analysis.fit.get_b_err_parameter())
            if num_of_params > 2:
                ui_analysis.load_pages.lineEdit_analysis_err_c.setText("%0.4f" % analysis.fit.get_c_err_parameter())
                if num_of_params > 3:
                    ui_analysis.load_pages.lineEdit_analysis_err_d.setText("%0.4f" % analysis.fit.get_d_err_parameter())


# Return an array of two rgb colors, one for plot line and one for plot symbol
def get_graph_colors(ui_analysis: UI_AnalysisWindow) -> np.array:
    colors = [(55, 55, 55), "b", "g", "r", "c", "m", "y", "k", "w"]
    plot_line_color = colors[ui_analysis.load_pages.comboBox_analysis_plot_line_color.currentIndex()]
    plot_symbol_color = colors[ui_analysis.load_pages.comboBox_analysis_plot_symbol_color.currentIndex()]
    return [plot_line_color, plot_symbol_color]


def set_data_2_graph(analysis: Analysis, ui_analysis: UI_AnalysisWindow) -> None:
    colors = get_graph_colors(ui_analysis)
    x = analysis.fit.get_x_array()
    y = analysis.fit.get_y_array()
    dx = analysis.fit.get_dx_array()
    dy = analysis.fit.get_dy_array()
    # Add error bar
    if dx is not None and dy is not None:
        ui_analysis.graph.addItem(
            pg.ErrorBarItem(x=x, y=y, top=dy / 2, bottom=dy / 2, left=dx / 2, right=dx / 2))
    elif dy is not None:
        ui_analysis.graph.addItem(pg.ErrorBarItem(x=x, y=y, top=dy / 2, bottom=dy / 2))
    ui_analysis.graph.plot(analysis.fit.get_x_array(), analysis.fit.get_y_array(),
                           symbol='o', pen=colors[0], symbolBrush=colors[1], symbolPen='w', symbolSize=8)
    # Add titles and units
    ui_analysis.graph.setTitle(title=ui_analysis.load_pages.lineEdit_analysis_main_title.text())
    ui_analysis.graph.setLabel('left', ui_analysis.load_pages.lineEdit_analysis_x_title.text(),
                               units=ui_analysis.load_pages.lineEdit_analysis_x_units.text())
    ui_analysis.graph.setLabel('bottom', ui_analysis.load_pages.lineEdit_analysis_y_title.text(),
                               units=ui_analysis.load_pages.lineEdit_analysis_y_units.text())


def plot_opt_func(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    colors = get_graph_colors(ui_analysis)
    x = analysis.fit.get_x_array()
    function = analysis.fit.get_function()
    func_x = np.linspace(x[0], x[-1], 10000)
    params = analysis.fit.get_params_array()
    y_fit = function(func_x, *params)
    ind = ui_analysis.load_pages.comboBox_analysis_fit_function.currentIndex()
    ui_analysis.graph.plot(func_x, y_fit, pen=colors[0], name=analysis.fun_texts.fun_non_latex_texts_array[ind])


def plot_opt_func_with_uncertainties(opt: Minuit, analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    colors = get_graph_colors(ui_analysis)
    x = analysis.fit.get_x_array()
    function = analysis.fit.get_function()
    par_values = analysis.fit.get_params_array()
    func_x = np.linspace(x[0], x[-1], 10000)  # 10000 linearly spaced numbers
    y_fit = function(func_x, *par_values)
    ui_analysis.graph.plot(func_x, y_fit, pen=colors[0])  # plot the function over 10k points covering the x axis


def matplotlib_fit_analysis_data(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    pages = ui_analysis.load_pages
    x = analysis.fit.get_x_array()
    y = analysis.fit.get_y_array()
    dx = analysis.fit.get_dx_array()
    dy = analysis.fit.get_dy_array()
    text = "$ Fitted \  to \ f(x) = {} $\n".format(analysis.fun_texts.fun_latex_texts_array[ui_analysis.load_pages.
                                                   comboBox_analysis_fit_function.currentIndex()])
    ascii_prm = 97
    for i in range(analysis.fit.get_func_par_num()):
        text += "$\ \ \ %s$ = %0.4f $\pm$ %0.4f \n" % (
            chr(ascii_prm + i), analysis.fit.get_params_array()[i], analysis.fit.get_err_array()[i])
    if analysis.fit.get_chi_ndof() is not None:
        text = text + "$\dfrac{{\chi}^2}{N_{dof}} = %0.4f(%0.4f/%d)$\n" % (
            analysis.fit.get_chi_ndof(), analysis.fit.get_chi_ndof() * len(x),
            len(x))
    func_x = np.linspace(x[0], x[-1], 10000)  # 10000 linearly spaced numbers
    function = analysis.fit.get_function()
    par_values = analysis.fit.get_params_array()
    y_fit = function(func_x, *par_values)
    x_title = "%s [%s]" % (pages.lineEdit_analysis_x_title.text(), pages.lineEdit_analysis_x_units.text())
    y_title = "%s [%s]" % (pages.lineEdit_analysis_y_title.text(), pages.lineEdit_analysis_y_units.text())
    main_title = "%s" % ui_analysis.load_pages.lineEdit_analysis_main_title.text()
    plt.rc("font", size=16, family="Times New Roman")
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.plot(func_x, y_fit)  # plot the function over 10k points covering the x axis
    ax.scatter(x, y, c="black")
    ax.errorbar(x, y, dy, dx, fmt='none', ecolor='red', capsize=3)
    ax.set_xlabel(x_title, fontdict={"size": 21})
    ax.set_ylabel(y_title, fontdict={"size": 21})
    anchored_text = AnchoredText(text, loc=ui_analysis.load_pages.comboBox_analysis_box_location.currentIndex())
    ax.add_artist(anchored_text)
    plt.grid(True)
    plt.title(main_title)
    plt.show()


def matplotlib_plot_analysis_data(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    pages = ui_analysis.load_pages
    main_title = "%s" % ui_analysis.load_pages.lineEdit_analysis_main_title.text()
    x_title = "%s [%s]" % (pages.lineEdit_analysis_x_title.text(), pages.lineEdit_analysis_x_units.text())
    y_title = "%s [%s]" % (pages.lineEdit_analysis_y_title.text(), pages.lineEdit_analysis_y_units.text())
    plt.rc("font", size=16, family="Times New Roman")
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    for i in range(len(analysis.get_plots())):
        x, y = analysis.get_plot(i)
        color = analysis.get_plot_color(i)
        label = analysis.get_plot_label(i)
        if len(color) > 1:
            ax.plot(x, y, label=label)
        else:
            ax.plot(x, y, color=color, label=label)
    ax.set_xlabel(x_title, fontdict={"size": 21})
    ax.set_ylabel(y_title, fontdict={"size": 21})
    plt.grid(True)
    plt.title(main_title)
    plt.legend()
    plt.show()


def clean_graph_analysis(ui_analysis: UI_AnalysisWindow):
    pages = ui_analysis.load_pages
    pages.lineEdit_analysis_main_title.clear()
    pages.lineEdit_analysis_x_title.clear()
    pages.lineEdit_analysis_x_units.clear()
    pages.lineEdit_analysis_y_title.clear()
    pages.lineEdit_analysis_y_units.clear()
    pages.lineEdit_analysis_curve_label.clear()
    pages.comboBox_analysis_box_location.setCurrentIndex(0)
    pages.comboBox_analysis_plot_line_color.setCurrentIndex(0)
    pages.comboBox_analysis_plot_symbol_color.setCurrentIndex(0)
    ui_analysis.graph.clear()
    ui_analysis.graph.setTitle(title="")
    ui_analysis.graph.setLabel('left', "")
    ui_analysis.graph.setLabel('bottom', "")
    ui_analysis.analysis.clear_plots()
    print("Graph Clean Done")


def clean_opt_analysis(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    pages = ui_analysis.load_pages
    pages.comboBox_analysis_fit_function.setCurrentIndex(0)
    refresh_params_data_enable(ui_analysis, 2)
    pages.lineEdit_analysis_param_a.setText("None")
    pages.lineEdit_analysis_err_a.setText("None")
    pages.lineEdit_analysis_param_b.setText("None")
    pages.lineEdit_analysis_err_b.setText("None")
    pages.lineEdit_analysis_param_c.setText("None")
    pages.lineEdit_analysis_err_c.setText("None")
    pages.lineEdit_analysis_param_d.setText("None")
    pages.lineEdit_analysis_err_d.setText("None")
    pages.lineEdit_analysis_steps.setText("")
    pages.lineEdit_analysis_set_x_i.setText("")
    pages.lineEdit_analysis_set_x_f.setText("")
    ui_analysis.load_pages.lineEdit_analysis_chi2Ndof.setEnabled(False)
    ui_analysis.load_pages.lineEdit_analysis_chi2.setEnabled(False)
    ui_analysis.load_pages.pushButton_analyisis_guess_params.setEnabled(False)
    ui_analysis.load_pages.lineEdit_analysis_chi2Ndof.setText("None")
    ui_analysis.load_pages.lineEdit_analysis_chi2.setText("None")
    pages.comboBox_analysis_x_axis.setCurrentIndex(0)
    pages.comboBox_analysis_y_axis.setCurrentIndex(0)
    pages.comboBox_analysis_x_error.setCurrentIndex(0)
    pages.comboBox_analysis_y_error.setCurrentIndex(0)
    analysis.fit = Fit()
    print("Optimization Clean Done")


def clean_all_analysis_screen(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    # Clean Graph
    clean_graph_analysis(ui_analysis)
    # Clean Optimization
    clean_opt_analysis(analysis, ui_analysis)
    # Clear Excel Path
    ui_analysis.load_pages.lineEdit_analysis_excel_name.clear()
    # Clear Excel Sheet Names
    ui_analysis.load_pages.comboBox_analysis_excel_sheet_names.clear()
    # Clear Axis Combos
    ui_analysis.load_pages.comboBox_analysis_x_axis.clear()
    ui_analysis.load_pages.comboBox_analysis_y_axis.clear()
    ui_analysis.load_pages.comboBox_analysis_x_error.clear()
    ui_analysis.load_pages.comboBox_analysis_y_error.clear()
    # Creating new analysis
    ui_analysis.analysis = Analysis()
    print("Clean All Done")


def guess_params(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    fun_name = ui_analysis.load_pages.comboBox_analysis_fit_function.currentText()
    analysis.fit.guess_params(fun_name)
    update_initial_parameters(analysis, ui_analysis)


def update_initial_parameters(analysis: Analysis, ui_analysis: UI_AnalysisWindow):
    num_of_params = analysis.fit.get_func_par_num()
    if num_of_params > 0:
        ui_analysis.load_pages.lineEdit_analysis_initial_a.setText(str(analysis.fit.get_a_initial()))
        ui_analysis.load_pages.lineEdit_analysis_s_limit_a.setText(str(analysis.fit.get_a_limit_i()))
        ui_analysis.load_pages.lineEdit_analysis_f_limit_a.setText(str(analysis.fit.get_a_limit_f()))
        if num_of_params > 1:
            ui_analysis.load_pages.lineEdit_analysis_initial_b.setText(str(analysis.fit.get_b_initial()))
            ui_analysis.load_pages.lineEdit_analysis_s_limit_b.setText(str(analysis.fit.get_b_limit_i()))
            ui_analysis.load_pages.lineEdit_analysis_f_limit_b.setText(str(analysis.fit.get_b_limit_f()))
            if num_of_params > 2:
                ui_analysis.load_pages.lineEdit_analysis_initial_c.setText(str(analysis.fit.get_c_initial()))
                ui_analysis.load_pages.lineEdit_analysis_s_limit_c.setText(str(analysis.fit.get_c_limit_i()))
                ui_analysis.load_pages.lineEdit_analysis_f_limit_c.setText(str(analysis.fit.get_c_limit_f()))
                if num_of_params > 3:
                    ui_analysis.load_pages.lineEdit_analysis_initial_d.setText(str(analysis.fit.get_d_initial()))
                    ui_analysis.load_pages.lineEdit_analysis_s_limit_d.setText(str(analysis.fit.get_d_limit_i()))
                    ui_analysis.load_pages.lineEdit_analysis_f_limit_d.setText(str(analysis.fit.get_d_limit_f()))
