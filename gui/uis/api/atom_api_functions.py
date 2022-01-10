# IMPORT PACKAGES FOR ANALYSING
# ///////////////////////////////////////////////////////////////
import string

import lmfit
import pandas
import pandas as pd
from PIL import Image
import numpy as np
import os
from os import walk
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
    if switch == "Without Cloud":
        filename = QFileDialog.getOpenFileName(caption=switch,
                                               filter="All Files();;Image Files (*.png *.jpg *.bmp);;Bin Files (*.bin)")
        atom.setNoCloudPath(filename[0])
        ui_atom.load_pages.lineEdit_without_cloud_path.setText(filename[0])
        print(atom.getNoCloudPath())
    elif switch == "With Cloud":
        filename = QFileDialog.getOpenFileName(caption=switch,
                                               filter="All Files();;Image Files (*.png *.jpg *.bmp);;Bin Files (*.bin)")
        atom.setCloudPath(filename[0])
        ui_atom.load_pages.lineEdit_with_cloud_path.setText(filename[0])
        print(atom.getCloudPath())
    elif switch == "Automatic Pull":
        print("Notice you can only pull files with name starting with: With, Without")
        filename = QFileDialog.getOpenFileName(caption=switch, filter="Bin Files (With*.bin Without*.bin)")
        filepath = os.path.dirname(os.path.abspath(filename[0]))
        atom.setDirectoryPath(filepath)
        ui_atom.load_pages.lineEdit_atom_exported_file_path.setText(filepath)
        print(atom.getDirectoryPath())
        if not atom.CheckCloudParams():
            pop_error("Please analyze cloud parameters first", "Please Load single cloud data first")
        elif not atom.addAndSortAutomaticData():
            pop_error("Can not load Files", "Please check path of files")


def export_to_excel(atom: Atom, ui_atom: UI_AtomWindow):
    x, y = atom.getLastPlot()
    if x is None or y is None:
        pop_error("There is no data to export", "There is no data to export")
    else:
        name = ui_atom.load_pages.lineEdit_atom_exported_file_name.text()
        path = ui_atom.load_pages.lineEdit_atom_exported_file_path.text()
        if name == "" or path == "" :
            pop_error("File name or path is wrong", "File name or path is wrong")
        else:
            data = {'X': x, 'Y': y}
            df = pd.DataFrame(data)
            df.to_excel(excel_writer=path + '\\' + name + '.xlsx')
            print("DataFrame is written to Excel File successfully.")


def calculate_atom_number(atom: Atom, ui_atom: UI_AtomWindow, withCloud, withoutCloud) -> None:
    if atom.clearToLoad():
        if atom.CheckCloudParams():
            if not atom.getParametersCondition():
                add_cloud_parameters(atom, ui_atom)
            atom_number = atom.calculateAtomNumber(withCloud, withoutCloud)
            ui_atom.load_pages.lineEdit_atom_number.setText("%0.0f" % atom_number)
            return atom_number
        else:
            pop_error("Please Calculate parameters first!", "Please calculate cloud parameter first")
    else:
        pop_error("Can not Calculate! Please load images first", "Please load images first")


def calculate_automatic_sequence(atom: Atom, ui_atom: UI_AtomWindow, switch: int) -> None:
    if switch == 0:
        # Calculating atoms number
        print("Calculate Atom Number - Sequence")
        calculate_atom_number_sequence(atom, ui_atom)
    return


def calculate_atom_number_sequence(atom: Atom, ui_atom: UI_AtomWindow):
    x = []
    y = []
    seq_cloud = atom.getAutomaticCloudArray()
    print(seq_cloud)
    seq_non_cloud = atom.getAutomaticNonCloudArray()
    print(seq_non_cloud)
    print("Number of files: " + str(len(seq_cloud)))
    for i in range(len(seq_cloud)):
        x.append(i)
        atom_number = calculate_atom_number(atom, ui_atom, atom.path_to_array(seq_cloud[i]),
                                            atom.path_to_array(seq_non_cloud[i]))
        print("Number of calculated atoms: " + str(atom_number))
        y.append(atom_number)
    atom.setLastPlot(x, y)
    ui_atom.graph.plot(x, y, symbol='o', symbolPen='w', symbolSize=8)


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


def graph_combo_current_change(atom: Atom, ui_atom: UI_AtomWindow, ind: int) -> None:
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


def fit_gaussian_y(atom: Atom, ui_atom: UI_AtomWindow):
    if atom.clearToLoad():
        loaded_image = atom.loadImage(ui_atom.cloud_combo.currentIndex())
        pos_x = int(ui_atom.inf1.value())
        ui_atom.graph_right.clear()
        ui_atom.graph_right.plot(loaded_image[pos_x], np.arange(len(loaded_image[0])))

        model = lmfit.models.GaussianModel()
        fit = Fit()
        fit.set_func_par_num(3)
        fit.set_arrays(np.arange(len(loaded_image[0])), loaded_image[pos_x], None, None)
        fit.guess_params("Gaussian")
        fit.opt_by_lmfit_generic(model)

        x = fit.get_x_array()
        func_x = np.linspace(x[0], x[-1], len(loaded_image[0]))
        params = fit.get_params_array()
        y_fit = lmfit.lineshapes.gaussian(func_x, *params)
        ui_atom.graph_right.plot(x=y_fit, y=func_x, pen='r')
        # Insert Parameters into slots
        # Insert Values
        ui_atom.load_pages.lineEdit_atom_result_amplitude.setText(
            "%0.4f" % (params[0] / (params[2] * np.sqrt(2 * np.pi))))  # lmfit defines gaussian different
        ui_atom.load_pages.lineEdit_atom_result_y_0.setText("%0.4f" % params[1])
        atom.setY_0(int(params[1]))
        ui_atom.load_pages.lineEdit_atom_result_sigma_y.setText("%0.4f" % params[2])
        atom.set_sigma_Y(int(params[2]))
        # Insert Errors
        errors = fit.get_err_array()
        ui_atom.load_pages.lineEdit_atom_error_amplitude.setText(
            "%0.4f" % (errors[0] / (errors[2] * np.sqrt(2 * np.pi))))
        ui_atom.load_pages.lineEdit_atom_error_y_0.setText("%0.4f" % errors[1])
        ui_atom.load_pages.lineEdit_atom_error_sigma_y.setText("%0.4f" % errors[2])


def fit_gaussian_x(atom: Atom, ui_atom: UI_AtomWindow):
    if atom.clearToLoad():
        loaded_image = atom.loadImage(ui_atom.cloud_combo.currentIndex())
        pos_y = int(ui_atom.inf2.value())
        ui_atom.graph_top.clear()
        ui_atom.graph_top.plot(np.arange(len(loaded_image)), loaded_image[:, pos_y])

        model = lmfit.models.GaussianModel()
        fit = Fit()
        fit.set_func_par_num(3)
        fit.set_arrays(np.arange(len(loaded_image)), loaded_image[:, pos_y], None, None)
        fit.guess_params("Gaussian")
        fit.opt_by_lmfit_generic(model)

        x = fit.get_x_array()
        func_x = np.linspace(x[0], x[-1], len(loaded_image))
        params = fit.get_params_array()
        y_fit = lmfit.lineshapes.gaussian(func_x, *params)
        ui_atom.graph_top.plot(y=y_fit, x=func_x, pen='r')
        # Insert Parameters into slots
        # Insert Values
        ui_atom.load_pages.lineEdit_atom_result_amplitude.setText(
            "%0.4f" % (params[0] / (params[2] * np.sqrt(2 * np.pi))))  # lmfit defines gaussian different
        ui_atom.load_pages.lineEdit_atom_result_x_0.setText("%0.4f" % params[1])
        atom.setX_0(int(params[1]))
        ui_atom.load_pages.lineEdit_atom_result_sigma_x.setText("%0.4f" % params[2])
        atom.set_sigma_X(int(params[2]))
        # Insert Errors
        errors = fit.get_err_array()
        ui_atom.load_pages.lineEdit_atom_error_amplitude.setText(
            "%0.4f" % (errors[0] / (errors[2] * np.sqrt(2 * np.pi))))
        ui_atom.load_pages.lineEdit_atom_error_x_0.setText("%0.4f" % errors[1])
        ui_atom.load_pages.lineEdit_atom_error_sigma_x.setText("%0.4f" % errors[2])


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
    # clear initial values
    ui_atom.load_pages.lineEdit_atom_initial_amplitude.clear()
    ui_atom.load_pages.lineEdit_atom_initial_x_0.clear()
    ui_atom.load_pages.lineEdit_atom_initial_y_0.clear()
    ui_atom.load_pages.lineEdit_atom_initial_sigma_x.clear()
    ui_atom.load_pages.lineEdit_atom_initial_sigma_y.clear()
    ui_atom.load_pages.lineEdit_atom_initial_theta.clear()
    ui_atom.load_pages.lineEdit_atom_initial_offset.clear()
    # clear limits
    # min
    ui_atom.load_pages.lineEdit_atom_min_amplitude.clear()
    ui_atom.load_pages.lineEdit_atom_min_x_0.clear()
    ui_atom.load_pages.lineEdit_atom_min_y_0.clear()
    ui_atom.load_pages.lineEdit_atom_min_sigma_x.clear()
    ui_atom.load_pages.lineEdit_atom_min_sigma_y.clear()
    ui_atom.load_pages.lineEdit_atom_min_theta.clear()
    ui_atom.load_pages.lineEdit_atom_min_offset.clear()
    # max
    ui_atom.load_pages.lineEdit_atom_max_amplitude.clear()
    ui_atom.load_pages.lineEdit_atom_max_x_0.clear()
    ui_atom.load_pages.lineEdit_atom_max_y_0.clear()
    ui_atom.load_pages.lineEdit_atom_max_sigma_x.clear()
    ui_atom.load_pages.lineEdit_atom_max_sigma_y.clear()
    ui_atom.load_pages.lineEdit_atom_max_theta.clear()
    ui_atom.load_pages.lineEdit_atom_max_offset.clear()
    # clear results
    ui_atom.load_pages.lineEdit_atom_result_amplitude.clear()
    ui_atom.load_pages.lineEdit_atom_result_x_0.clear()
    ui_atom.load_pages.lineEdit_atom_result_y_0.clear()
    ui_atom.load_pages.lineEdit_atom_result_sigma_x.clear()
    ui_atom.load_pages.lineEdit_atom_result_sigma_y.clear()
    ui_atom.load_pages.lineEdit_atom_result_theta.clear()
    ui_atom.load_pages.lineEdit_atom_result_offset.clear()
    # clear standard errors
    ui_atom.load_pages.lineEdit_atom_error_amplitude.clear()
    ui_atom.load_pages.lineEdit_atom_error_x_0.clear()
    ui_atom.load_pages.lineEdit_atom_error_y_0.clear()
    ui_atom.load_pages.lineEdit_atom_error_sigma_x.clear()
    ui_atom.load_pages.lineEdit_atom_error_sigma_y.clear()
    ui_atom.load_pages.lineEdit_atom_error_theta.clear()
    ui_atom.load_pages.lineEdit_atom_error_offset.clear()


def guess_params(atom: Atom, ui_atom: UI_AtomWindow):
    if atom.clearToLoad():
        two_d = TwoD_Function_Fit()
        data = (atom.loadImage(ui_atom.cloud_combo.currentIndex())).ravel()
    else:
        pop_error("images are not loaded", "please load images first")


def add_cloud_parameters(atom: Atom, ui_atom: UI_AtomWindow):
    detuning = float(ui_atom.load_pages.lineEdit_atom_detuning.text())
    sigma_0 = float(ui_atom.load_pages.lineEdit_atom_sigma_0.text())
    f1 = float(ui_atom.load_pages.lineEdit_atom_f1.text())
    f2 = float(ui_atom.load_pages.lineEdit_atom_f2.text())
    pixel_length = float(ui_atom.load_pages.lineEdit_atom_pixel_length.text())
    atom.prm.set_cloud_parameters(detuning, sigma_0, f1, f2, pixel_length)
    atom.setParametersCondition(bool(True))


def clear_cloud_parameters(atom: Atom, ui_atom: UI_AtomWindow):
    ui_atom.load_pages.lineEdit_atom_detuning.clear()
    ui_atom.load_pages.lineEdit_atom_sigma_0.clear()
    ui_atom.load_pages.lineEdit_atom_f1.clear()
    ui_atom.load_pages.lineEdit_atom_f2.clear()
    ui_atom.load_pages.lineEdit_atom_pixel_length.clear()
    atom.prm.set_cloud_parameters(0, 0, 0, 0, 0)
