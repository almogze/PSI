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
from gui.uis.api.fitting import TwoD_Function_Fit

from gui.uis.api.analysis import Analysis
from gui.uis.windows.atom_window import UI_AtomWindow
from gui.uis.windows.analysis_window import UI_AnalysisWindow
from gui.uis.api.fitting import Fit
from gui.widgets import *
from qt_core import *


def pop_error(s1: string, s2: string):
    error = QMessageBox()
    error.setWindowTitle("Error")
    error.setIcon(QMessageBox.Critical)
    print(s1)
    error.setText(s2)
    error.exec()


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
        pop_error("Can not Calculate! Please load images first", "Please load images first")


def load_image(atom: Atom, ui_atom: UI_AtomWindow) -> None:
    if checkAndSet(atom):
        checkAndLoad(atom, ui_atom)


def checkAndSet(atom: Atom) -> bool:
    condition = bool(True)
    if not atom.clearToSet():
        pop_error("Can not set images! Please check images path", "Please check images path")
        condition = bool(False)
    elif atom.checkImageFormatJPG():
        atom.setImageJPG()
    elif atom.checkImageFormatBIN():
        atom.setImageBIN()
    else:
        pop_error("At least one of the images is not in jpg or bin format", "images are not in format")
        condition = bool(False)
    return condition


def checkAndLoad(atom: Atom, ui_atom: UI_AtomWindow) -> None:
    if not atom.clearToLoad():
        pop_error("Can not load images! Please check images numpy arrays", "Please check images numpy arrays")
    else:
        loaded_image = atom.loadImage(ui_atom.cloud_combo.currentIndex())
        if loaded_image is None:
            print("ComboBox index is not Valid")
        else:
            # clear old plots
            ui_atom.graph_top.clear()
            ui_atom.graph_right.clear()
            # load image
            ui_atom.image.setImage(image=loaded_image)
            # Set bounds for lines
            ui_atom.inf1.setBounds([0, len(loaded_image)])
            ui_atom.inf2.setBounds([0, len(loaded_image[0])])
            # plot top and right graphs
            pos_x = int(ui_atom.inf1.value())
            pos_y = int(ui_atom.inf2.value())
            ui_atom.graph_top.plot(np.arange(len(loaded_image)), loaded_image[:, pos_y])
            ui_atom.graph_right.plot(loaded_image[pos_x], np.arange(len(loaded_image[0])))
            # add lines positions
            ui_atom.image_view.setTitle(
                "pixel: (%d, %d), intensity: %0.2f" % (pos_x, pos_y, loaded_image[pos_x, pos_y]))


def clear_image(atom: Atom, ui_atom: UI_AtomWindow) -> None:
    atom.clearImage()
    ui_atom.load_pages.ImageView_Atom.clear()
    ui_atom.load_pages.label_atom_number.setText(str(0))
    ui_atom.load_pages.label_cloud_temperature.setText(str(0))
    ui_atom.load_pages.lineEdit_with_cloud_path.clear()
    ui_atom.load_pages.lineEdit_without_cloud_path.clear()


def combo_current_change(atom: Atom, ui_atom: UI_AtomWindow, ind: int) -> None:
    # clear old plots
    ui_atom.graph_top.clear()
    ui_atom.graph_right.clear()
    loaded_image = atom.loadImage(ind)
    if loaded_image is not None:
        ui_atom.image.setImage(image=loaded_image)
        pos_x = int(ui_atom.inf1.value())
        pos_y = int(ui_atom.inf2.value())
        ui_atom.graph_top.plot(np.arange(len(loaded_image)), loaded_image[:, pos_y])
        ui_atom.graph_right.plot(loaded_image[pos_x], np.arange(len(loaded_image[0])))
        ui_atom.image_view.setTitle(
            "pixel: (%d, %d), intensity: %0.2f" % (pos_x, pos_y, loaded_image[pos_x, pos_y]))
    else:
        print("ComboBox index is not Valid")


def update_top_graph(atom: Atom, ui_atom: UI_AtomWindow):
    if atom.clearToLoad():
        loaded_image = atom.loadImage(ui_atom.cloud_combo.currentIndex())
        pos_x = int(ui_atom.inf1.value())
        pos_y = int(ui_atom.inf2.value())
        ui_atom.graph_top.clear()
        ui_atom.graph_top.plot(np.arange(len(loaded_image)), loaded_image[:, pos_y])
        ui_atom.image_view.setTitle(
            "pixel: (%d, %d), intensity: %0.2f" % (pos_x, pos_y, loaded_image[pos_x, pos_y]))


def update_right_graph(atom: Atom, ui_atom: UI_AtomWindow):
    if atom.clearToLoad():
        loaded_image = atom.loadImage(ui_atom.cloud_combo.currentIndex())
        pos_x = int(ui_atom.inf1.value())
        pos_y = int(ui_atom.inf2.value())
        ui_atom.graph_right.clear()
        ui_atom.graph_right.plot(loaded_image[pos_x], np.arange(len(loaded_image[0])))
        ui_atom.image_view.setTitle(
            "pixel: (%d, %d), intensity: %0.2f" % (pos_x, pos_y, loaded_image[pos_x, pos_y]))


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


def fit_gaussian_shape(atom: Atom, ui_atom: UI_AtomWindow) -> None:
    if atom.clearToLoad():
        print("1")
        two_d = TwoD_Function_Fit()
        print("2")
        data = (atom.loadImage(ui_atom.cloud_combo.currentIndex())).ravel()
        print("3")
        initial_params = tuple(get_init_parameters(ui_atom))
        print("4")
        popt, pcov = two_d.fit_2D_function(two_d.gaussian, data, initial_params)
        print("5")
        insert_values(ui_atom, popt)
        insert_errors(ui_atom, pcov)

        x = np.linspace(0, 2049, 2050)
        y = np.linspace(0, 2447, 2448)
        X, Y = np.meshgrid(x, y)

        fit = two_d.twoD_Gaussian(X, Y, *popt)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.imshow(fit, origin='bottom', cmap='plasma')
        ax.contour(X, Y, fit, colors='w')
        plt.show()


    else:
        pop_error("images are not loaded", "please load images first")


def get_init_parameters(ui_atom: UI_AtomWindow) -> np.array:
    x_0 = float(ui_atom.load_pages.lineEdit_atom_initial_x_0.text())
    y_0 = float(ui_atom.load_pages.lineEdit_atom_initial_y_0.text())
    sigma_x = float(ui_atom.load_pages.lineEdit_atom_initial_sigma_x.text())
    sigma_y = float(ui_atom.load_pages.lineEdit_atom_initial_sigma_y.text())
    amplitude = float(ui_atom.load_pages.lineEdit_atom_initial_amplitude.text())
    theta = float(ui_atom.load_pages.lineEdit_atom_initial_theta.text())
    offset = float(ui_atom.load_pages.lineEdit_atom_initial_offset.text())
    return [amplitude, x_0, y_0, sigma_x, sigma_y, theta, offset]


def insert_values(ui_atom: UI_AtomWindow, popt: np.array) -> None:
    ui_atom.load_pages.lineEdit_atom_result_amplitude.setText(str(popt[0]))
    ui_atom.load_pages.lineEdit_atom_result_x_0.setText(str(popt[1]))
    ui_atom.load_pages.lineEdit_atom_result_y_0.setText(str(popt[2]))
    ui_atom.load_pages.lineEdit_atom_result_sigma_x.setText(str(popt[3]))
    ui_atom.load_pages.lineEdit_atom_result_sigma_y.setText(str(popt[4]))
    ui_atom.load_pages.lineEdit_atom_result_theta.setText(str(popt[5]))
    ui_atom.load_pages.lineEdit_atom_result_offset.setText(str(popt[6]))


def insert_errors(ui_atom: UI_AtomWindow, pcov: np.array) -> None:
    ui_atom.load_pages.lineEdit_atom_error_amplitude.setText(str(pcov[0][0]))
    ui_atom.load_pages.lineEdit_atom_error_x_0.setText(str(pcov[1][1]))
    ui_atom.load_pages.lineEdit_atom_error_y_0.setText(str(pcov[2][2]))
    ui_atom.load_pages.lineEdit_atom_error_sigma_x.setText(str(pcov[3][3]))
    ui_atom.load_pages.lineEdit_atom_error_sigma_y.setText(str(pcov[4][4]))
    ui_atom.load_pages.lineEdit_atom_error_theta.setText(str(pcov[5][5]))
    ui_atom.load_pages.lineEdit_atom_error_offset.setText(str(pcov[6][6]))


def clear_fit(atom: Atom, ui_atom: UI_AtomWindow) -> None:
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


"""""""""""
def matplotlib_fit_analysis_data(atom: Atom, ui_atom: UI_AtomWindow) -> None:
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
"""""""""""
