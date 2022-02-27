from PIL import Image
import numpy as np
import os
from os import walk
from gui.uis.api.parameters import Parameters
import threading


class Atom(object):
    _instance = None

    def __new__(self):
        if not Atom._instance:
            self._instance = super(Atom, self).__new__(self)
            self._instance.prm = Parameters()
            self._instance.no_cloud_path = None
            self._instance.with_cloud_path = None
            self._instance.no_cloud_image_array = None
            self._instance.cloud_image_array = None
            # Automatic Series
            self._instance.directory_path = None
            self._instance.automatic_with_cloud = []
            self._instance.automatic_without_cloud = []
            self._instance.automatic_data_number = []
            self._instance.last_plot_x = []
            self._instance.last_plot_y = []
            self._instance.data_param = None
            # Initial Parameters
            self._instance.first_initiate = bool(False)
            self._instance.x_0 = None
            self._instance.y_0 = None
            self._instance.sigma_x = None
            self._instance.sigma_y = None
        return Atom._instance

    def setNoCloudPath(self, path):
        self._instance.no_cloud_path = path

    def getNoCloudPath(self):
        return self._instance.no_cloud_path

    def setCloudPath(self, path):
        self._instance.with_cloud_path = path

    def getCloudPath(self):
        return self._instance.with_cloud_path

    def setImageJPG(self):
        self._instance.no_cloud_image_array = np.asarray(Image.open(self.no_cloud_path).convert('L'))
        self._instance.cloud_image_array = np.asarray(Image.open(self.with_cloud_path).convert('L'))

    def setCloudArray(self, cloud_array):
        self._instance.cloud_image_array = cloud_array

    def setNonCloudArray(self, non_cloud_array):
        self._instance.no_cloud_image_array = non_cloud_array

    def setDataParam(self, param):
        self._instance.data_param = param

    def getCloudArray(self):
        return self._instance.cloud_image_array

    def getNonCloudArray(self):
        return self._instance.no_cloud_image_array

    def getAutomaticCloudArray(self):
        return self._instance.automatic_with_cloud

    def getAutomaticNonCloudArray(self):
        return self._instance.automatic_without_cloud

    def getAutomaticDataArray(self):
        return self._instance.automatic_data_number

    def getDataParam(self):
        return self._instance.data_param

    def addCloudFile(self, file):
        self._instance.automatic_with_cloud.append(file)

    def addNoCloudFile(self, file):
        self._instance.automatic_without_cloud.append(file)

    def addDataFile(self, file):
        self._instance.automatic_data_number.append(file)

    def setDirectoryPath(self, path):
        self._instance.directory_path = path

    def getDirectoryPath(self):
        return self._instance.directory_path

    def clearAutomaticGraph(self):
        self._instance.automatic_with_cloud = []
        self._instance.automatic_without_cloud = []
        self._instance.automatic_data_number = []
        self._instance.data_param = None
        self.setLastPlot([], [])
        self.setDirectoryPath(None)

    def setLastPlot(self, x, y):
        self._instance.last_plot_x = x
        self._instance.last_plot_y = y

    def getLastPlot(self):
        return self._instance.last_plot_x, self._instance.last_plot_y

    def getParametersCondition(self):
        return self._instance.first_initiate

    def setParametersCondition(self, condition):
        self._instance.first_initiate = condition

    def addAndSortAutomaticData(self) -> bool:
        if self.getDirectoryPath() is None:
            return bool(False)
        else:
            for (dirpath, dirnames, filenames) in walk(self.getDirectoryPath()):
                for file in filenames:
                    name, end = os.path.splitext(file)
                    if 'Without' in name and end == '.bin':
                        self.addNoCloudFile(file)
                    elif 'With' in name and end == '.bin':
                        self.addCloudFile(file)
                    elif 'data' in name and end == '.lvm':
                        self.addDataFile(file)
            self._instance.automatic_with_cloud.sort(key=lambda file_1: int(file_1[4:len(file_1) - 4]))
            self._instance.automatic_without_cloud.sort(key=lambda file_1: int(file_1[7:len(file_1) - 4]))
            self._instance.automatic_data_number.sort(key=lambda file_1: int(file_1[:len(file_1) - 8]))

            print(self._instance.automatic_with_cloud)
            print(self._instance.automatic_without_cloud)
            print(self._instance.automatic_data_number)
            return bool(True)

    def setImageBIN(self):
        # Camera: Prosilica GC 2450
        # Pixel size: 3.45 X 3.45 [micro meter]
        # Resolution: 2050 X 2448

        # Bin file format:
        # pixel represented as a floating point of 4 byte
        # first byte is a parameter byte and therefore removed from the array
        file_no_cloud = open(self._instance.no_cloud_path, 'rb')
        file_with_cloud = open(self._instance.with_cloud_path, 'rb')
        self._instance.no_cloud_image_array = np.reshape(np.fromfile(file_no_cloud, dtype='int16')[2:], (2050, 2448))
        self._instance.cloud_image_array = np.reshape(np.fromfile(file_with_cloud, dtype='int16')[2:], (2050, 2448))
        file_no_cloud.close()
        file_with_cloud.close()

    def path_to_array(self, name):
        bin_file = open(self.getDirectoryPath() + "\\" + name, 'rb')
        print(self.getDirectoryPath() + "\\" + name)
        array = np.reshape(np.fromfile(bin_file, dtype='int16')[2:], (2050, 2448))
        bin_file.close()
        return array

    def path_to_data(self, name):
        file = open(self.getDirectoryPath() + "\\" + name, 'r')
        line = file.readline().split(" ")
        return line[0], int(line[1].split(".")[0])

    def loadImage(self, ind: int) -> np.array:
        if ind == 2:
            return self._instance.cloud_image_array
        elif ind == 1:
            return self._instance.no_cloud_image_array
        elif ind == 0:
            return self._instance.no_cloud_image_array - self._instance.cloud_image_array
        elif ind == 3:
            return self.normSignal()
        else:
            return None

    def clearToLoad(self) -> bool:
        if self._instance.cloud_image_array is None or self._instance.no_cloud_image_array is None:
            return bool(False)
        return bool(True)

    def clearToSet(self) -> bool:
        if self._instance.with_cloud_path is None or self._instance.no_cloud_path is None:
            return bool(False)
        return bool(True)

    def checkImageFormatJPG(self) -> bool:
        iname1, iend1 = os.path.splitext(self._instance.no_cloud_path)
        iname2, iend2 = os.path.splitext(self._instance.with_cloud_path)
        if (iend1 == '.jpg' and iend2 == '.jpg') or (iend1 == '.jpeg' and iend2 == '.jpeg'):
            return bool(True)
        return bool(False)

    def checkImageFormatBIN(self) -> bool:
        iname1, iend1 = os.path.splitext(self._instance.no_cloud_path)
        iname2, iend2 = os.path.splitext(self._instance.with_cloud_path)
        if iend1 != '.bin' or iend2 != '.bin':
            return bool(False)
        return bool(True)

    def clearImage(self):
        self._instance.no_cloud_path = None
        self._instance.with_cloud_path = None
        self._instance.no_cloud_image_array = None
        self._instance.cloud_image_array = None
        self._instance.directory_path = None
        self._instance.automatic_with_cloud = []
        self._instance.automatic_without_cloud = []
        self._instance.automatic_data_number = []
        self._instance.data_param = None
        self._instance.first_initiate = bool(False)

    def calculateAtomNumber(self, cloud_array, without_cloud_array):
        # setting an ROI of 2 sigma_x horizontally and 2 sigma_y vertically around the center (x_0,y_0)
        cloud_area = np.array(cloud_array)[
                     self.getX_0() - 2 * self.get_sigma_X():self.getX_0() + 2 * self.get_sigma_X() + 1,
                     self.getY_0() - 2 * self.get_sigma_Y():self.getY_0() + 2 * self.get_sigma_Y() + 1]
        non_cloud_area = np.array(without_cloud_array)[
                         self.getX_0() - 2 * self.get_sigma_X():self.getX_0() + 2 * self.get_sigma_X() + 1,
                         self.getY_0() - 2 * self.get_sigma_Y():self.getY_0() + 2 * self.get_sigma_Y() + 1]
        log = np.log(np.array(cloud_area / non_cloud_area))
        condition = log < 0  # filter irrelevant values
        number_of_atoms = - np.sum(log[condition]) * (self._instance.prm.ccd_pixel_length * (
                    self._instance.prm.lens_1 / self._instance.prm.lens_2)) ** 2 / self._instance.prm.sigma_0
        return number_of_atoms

    def normSignal(self) -> np.array:
        sub = self._instance.no_cloud_image_array - self._instance.cloud_image_array
        return np.divide(sub.astype(float), self._instance.no_cloud_image_array.astype(float),
                         out=np.zeros_like(sub.astype(float)), where=self._instance.no_cloud_image_array.astype(float) != 0)

    # This method calculate the center of the cloud by iterating in the vertical and horizontal indices
    # and searching of the maximum intensity
    def calculateCenterOfCloud(self, cloud_array, without_cloud_array):
        print("calculate center of cloud")
        sub = without_cloud_array - cloud_array

        middle_state_vertical = {None: int(len(sub[0]) / 2)}
        middle_state_horizontal = {None: int(len(sub) / 2)}
        i_f_h = len(sub) - 1
        i_f_v = len(sub[0]) - 1
        try:
            middle_h = middle_state_horizontal[self.getX_0()]
            middle_v = middle_state_vertical[self.getY_0()]
        except KeyError:
            middle_h = int(self.getX_0())
            middle_v = int(self.getY_0())

        # index_array aggregate the result form each thread (which is the center of cloud according to each thread)
        index_array = [0, 0, 0, 0]
        # 2 threads for vertical iterations (start -> center, center -> end)
        # 2 threads for horizontal iterations (start -> center, center -> end)
        threads = [BinarySearchThread(0, sub, "right", 5, middle_h, index_array),
                   BinarySearchThread(1, sub, "left", middle_h, i_f_h - 5, index_array),
                   BinarySearchThread(2, sub, "up", 5, middle_v, index_array),
                   BinarySearchThread(3, sub, "down", middle_v, i_f_v - 5, index_array)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        # print(index_array)
        sum_0 = np.sum(np.where(sub[index_array[0]] > 0, sub[index_array[0]], 0))
        sum_1 = np.sum(np.where(sub[index_array[1]] > 0, sub[index_array[1]], 0))
        sum_2 = np.sum(np.where(sub[:, index_array[2]] > 0, sub[:, index_array[2]], 0))
        sum_3 = np.sum(np.where(sub[:, index_array[3]] > 0, sub[:, index_array[3]], 0))

        if sum_0 > sum_1:
            self.setX_0(index_array[0])
        else:
            self.setX_0(index_array[1])

        if sum_2 > sum_3:
            self.setY_0(index_array[2])
        else:
            self.setY_0(index_array[3])

    def setX_0(self, x_0: int):
        self._instance.x_0 = x_0

    def setY_0(self, y_0: int):
        self._instance.y_0 = y_0

    def getX_0(self):
        return self._instance.x_0

    def getY_0(self):
        return self._instance.y_0

    def set_sigma_X(self, sigma_x: float):
        self._instance.sigma_x = sigma_x

    def set_sigma_Y(self, sigma_y: float):
        self._instance.sigma_y = sigma_y

    def get_sigma_X(self):
        return self._instance.sigma_x

    def get_sigma_Y(self):
        return self._instance.sigma_y

    def CheckCloudParams(self) -> bool:
        if self.getX_0() is None or self.getY_0() is None or self.get_sigma_X() is None or self.get_sigma_Y() is None:
            return bool(False)
        return bool(True)

    def getRealSigmaX(self):
        return self.get_sigma_X() * self._instance.prm.ccd_pixel_length * (self._instance.prm.lens_1 / self._instance.prm.lens_2)

    def getRealSigmaY(self):
        return self.get_sigma_Y() * self._instance.prm.ccd_pixel_length * (self._instance.prm.lens_1 / self._instance.prm.lens_2)


class BinarySearchThread(threading.Thread):
    def __init__(self, threadID, array: np.array, condition, i_0, i_f, result_array):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.array = array
        self.condition = condition
        self.i_0 = i_0
        self.i_f = i_f
        self.result_array = result_array

    def run(self) -> None:
        # print("enter thread " + str(self.threadID))
        operations = {
            'up': self.searchVertical_up,
            'down': self.searchVertical_down,
            'left': self.searchHorizontal_left,
            'right': self.searchHorizontal_right
        }

        index = operations[self.condition](self.array, self.i_0, self.i_f)
        self.result_array[self.threadID] = index

    @staticmethod
    def searchVertical_up(array, i_0, i_f) -> int:
        while i_f > i_0 + 1:
            # print("vertical indices: {0} {1}".format(i_0, i_f))
            current_index = int((i_0 + i_f) / 2)
            if np.sum(np.where(array[:, i_f] > 0, array[:, i_f], 0)) > np.sum(
                    np.where(array[:, current_index] > 0, array[:, current_index], 0)):
                i_0 = current_index
            else:
                i_f = current_index
        return i_0

    @staticmethod
    def searchVertical_down(array, i_0, i_f) -> int:
        while i_f > i_0 + 1:
            # print("vertical indices: {0} {1}".format(i_0, i_f))
            current_index = int((i_0 + i_f) / 2)
            if np.sum(np.where(array[:, i_0 - 5:i_0 + 6] > 0, array[:, i_0 - 5:i_0 + 6], 0)) > np.sum(
                    np.where(array[:, current_index - 5:current_index + 6] > 0,
                             array[:, current_index - 5:current_index + 6], 0)):
                i_f = current_index
            else:
                i_0 = current_index
        return i_0

    @staticmethod
    def searchHorizontal_right(array, i_0, i_f) -> int:
        while i_f > i_0 + 1:
            current_index = int((i_0 + i_f) / 2)
            # sum_l = np.sum(np.where(array[i_0 - 5:i_0 + 6] > 0, array[i_0 - 5:i_0 + 6], 0)) / 10
            # sum_r = np.sum(np.where(array[i_f - 5:i_f + 6] > 0, array[i_f - 5:i_f + 6], 0)) / 10
            # sum_center = np.sum(np.where(array[current_index - 5:current_index + 6] > 0, array[current_index - 5:current_index + 6], 0)) / 10
            # print("Horizontal indices: left {0} right {1} center {2}".format(i_0, i_f, current_index))
            # print("Horizontal sums: left {0} right {1} center {2}".format(sum_l, sum_r, sum_center))
            if np.sum(np.where(array[i_f - 5:i_f + 6] > 0, array[i_f - 5:i_f + 6], 0)) > np.sum(
                    np.where(array[current_index - 5:current_index + 6] > 0, array[current_index - 5:current_index + 6],
                             0)):
                i_0 = current_index
            else:
                i_f = current_index
        return i_0

    @staticmethod
    def searchHorizontal_left(array, i_0, i_f) -> int:
        while i_f > i_0 + 1:
            current_index = int((i_0 + i_f) / 2)
            # print("vertical indices: {0} {1}".format(i_0, i_f))
            # print(current_index)
            if np.sum(np.where(array[i_0 - 5:i_0 + 6] > 0, array[i_0 - 5:i_0 + 6], 0)) > np.sum(
                    np.where(array[current_index - 5:current_index + 6] > 0, array[current_index - 5:current_index + 6],
                             0)):
                i_f = current_index
            else:
                i_0 = current_index
        return i_0
