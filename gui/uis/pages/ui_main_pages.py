# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesICxQCL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(848, 888)
        self.excel_settings_load_btn_layout = QVBoxLayout(MainPages)
        self.excel_settings_load_btn_layout.setSpacing(0)
        self.excel_settings_load_btn_layout.setObjectName(u"excel_settings_load_btn_layout")
        self.excel_settings_load_btn_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.page_main.setStyleSheet(u"font-size: 14pt")
        self.horizontalLayout_2 = QHBoxLayout(self.page_main)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_main)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 330))
        self.welcome_base.setMaximumSize(QSize(300, 330))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 300))
        self.logo.setMaximumSize(QSize(300, 300))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.welcome_base)

        self.pages.addWidget(self.page_main)
        self.page_fringes = QWidget()
        self.page_fringes.setObjectName(u"page_fringes")
        self.page_2_layout = QVBoxLayout(self.page_fringes)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.page_fringes)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.page_2_layout.addWidget(self.title_label)

        self.frame_fringes_main = QFrame(self.page_fringes)
        self.frame_fringes_main.setObjectName(u"frame_fringes_main")
        self.frame_fringes_main.setFrameShape(QFrame.StyledPanel)
        self.frame_fringes_main.setFrameShadow(QFrame.Raised)

        self.page_2_layout.addWidget(self.frame_fringes_main)

        self.pages.addWidget(self.page_fringes)
        self.page_atom = QWidget()
        self.page_atom.setObjectName(u"page_atom")
        self.page_atom.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_atom)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.atom_page_label = QLabel(self.page_atom)
        self.atom_page_label.setObjectName(u"atom_page_label")
        self.atom_page_label.setMaximumSize(QSize(16777215, 40))
        self.atom_page_label.setFont(font)
        self.atom_page_label.setAlignment(Qt.AlignCenter)

        self.page_3_layout.addWidget(self.atom_page_label)

        self.frame_atom_main = QFrame(self.page_atom)
        self.frame_atom_main.setObjectName(u"frame_atom_main")
        self.frame_atom_main.setFrameShape(QFrame.NoFrame)
        self.frame_atom_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_atom_main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_atom_1 = QFrame(self.frame_atom_main)
        self.frame_atom_1.setObjectName(u"frame_atom_1")
        self.frame_atom_1.setMaximumSize(QSize(800, 16777215))
        self.frame_atom_1.setFrameShape(QFrame.StyledPanel)
        self.frame_atom_1.setFrameShadow(QFrame.Raised)
        self.no_frame = QVBoxLayout(self.frame_atom_1)
        self.no_frame.setSpacing(0)
        self.no_frame.setObjectName(u"no_frame")
        self.no_frame.setContentsMargins(0, 0, 0, 0)
        self.frame_atom_graph = QFrame(self.frame_atom_1)
        self.frame_atom_graph.setObjectName(u"frame_atom_graph")
        self.frame_atom_graph.setMaximumSize(QSize(800, 600))
        self.frame_atom_graph.setFrameShape(QFrame.NoFrame)
        self.frame_atom_graph.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_atom_graph)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ImageView_Atom = ImageView(self.frame_atom_graph)
        self.ImageView_Atom.setObjectName(u"ImageView_Atom")

        self.verticalLayout.addWidget(self.ImageView_Atom)


        self.no_frame.addWidget(self.frame_atom_graph)

        self.frame_atom_analysis = QFrame(self.frame_atom_1)
        self.frame_atom_analysis.setObjectName(u"frame_atom_analysis")
        self.frame_atom_analysis.setFrameShape(QFrame.NoFrame)
        self.frame_atom_analysis.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_atom_analysis)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_atom_graph_btns = QFrame(self.frame_atom_analysis)
        self.frame_atom_graph_btns.setObjectName(u"frame_atom_graph_btns")
        self.frame_atom_graph_btns.setMaximumSize(QSize(16777215, 40))
        self.frame_atom_graph_btns.setFrameShape(QFrame.NoFrame)
        self.frame_atom_graph_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_atom_graph_btns)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_atom_graph_btn_load = QFrame(self.frame_atom_graph_btns)
        self.frame_atom_graph_btn_load.setObjectName(u"frame_atom_graph_btn_load")
        self.frame_atom_graph_btn_load.setMaximumSize(QSize(100, 16777215))
        self.frame_atom_graph_btn_load.setFrameShape(QFrame.NoFrame)
        self.frame_atom_graph_btn_load.setFrameShadow(QFrame.Raised)
        self.btn_atom_graph_load_layout = QHBoxLayout(self.frame_atom_graph_btn_load)
        self.btn_atom_graph_load_layout.setSpacing(0)
        self.btn_atom_graph_load_layout.setObjectName(u"btn_atom_graph_load_layout")
        self.btn_atom_graph_load_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_atom_graph_btn_load)

        self.frame_btn_atom_clear = QFrame(self.frame_atom_graph_btns)
        self.frame_btn_atom_clear.setObjectName(u"frame_btn_atom_clear")
        self.frame_btn_atom_clear.setMaximumSize(QSize(100, 16777215))
        self.frame_btn_atom_clear.setFrameShape(QFrame.NoFrame)
        self.frame_btn_atom_clear.setFrameShadow(QFrame.Raised)
        self.btn_atom_clear_layout = QVBoxLayout(self.frame_btn_atom_clear)
        self.btn_atom_clear_layout.setSpacing(0)
        self.btn_atom_clear_layout.setObjectName(u"btn_atom_clear_layout")
        self.btn_atom_clear_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_btn_atom_clear)

        self.cloud_comboBox = QComboBox(self.frame_atom_graph_btns)
        self.cloud_comboBox.setObjectName(u"cloud_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cloud_comboBox.sizePolicy().hasHeightForWidth())
        self.cloud_comboBox.setSizePolicy(sizePolicy)
        self.cloud_comboBox.setMaximumSize(QSize(16777215, 19))
        self.cloud_comboBox.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.cloud_comboBox.setEditable(False)
        self.cloud_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.cloud_comboBox.setIconSize(QSize(16, 16))
        self.cloud_comboBox.setFrame(True)

        self.horizontalLayout_3.addWidget(self.cloud_comboBox)


        self.verticalLayout_27.addWidget(self.frame_atom_graph_btns)

        self.frame_40 = QFrame(self.frame_atom_analysis)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(16777215, 40))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_wit_cloud_path = QLabel(self.frame_40)
        self.label_wit_cloud_path.setObjectName(u"label_wit_cloud_path")
        self.label_wit_cloud_path.setMinimumSize(QSize(180, 0))
        self.label_wit_cloud_path.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_wit_cloud_path)

        self.lineEdit_with_cloud_path = QLineEdit(self.frame_40)
        self.lineEdit_with_cloud_path.setObjectName(u"lineEdit_with_cloud_path")

        self.horizontalLayout_14.addWidget(self.lineEdit_with_cloud_path)


        self.verticalLayout_27.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_atom_analysis)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(16777215, 40))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_without_cloud_path = QLabel(self.frame_41)
        self.label_without_cloud_path.setObjectName(u"label_without_cloud_path")
        self.label_without_cloud_path.setMinimumSize(QSize(180, 0))
        self.label_without_cloud_path.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_without_cloud_path)

        self.lineEdit_without_cloud_path = QLineEdit(self.frame_41)
        self.lineEdit_without_cloud_path.setObjectName(u"lineEdit_without_cloud_path")

        self.horizontalLayout_15.addWidget(self.lineEdit_without_cloud_path)


        self.verticalLayout_27.addWidget(self.frame_41)

        self.frame_2 = QFrame(self.frame_atom_analysis)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_27.addWidget(self.frame_2)


        self.no_frame.addWidget(self.frame_atom_analysis)


        self.horizontalLayout.addWidget(self.frame_atom_1)

        self.frame_atom_2 = QFrame(self.frame_atom_main)
        self.frame_atom_2.setObjectName(u"frame_atom_2")
        self.frame_atom_2.setFrameShape(QFrame.StyledPanel)
        self.frame_atom_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_atom_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_atom_results = QFrame(self.frame_atom_2)
        self.frame_atom_results.setObjectName(u"frame_atom_results")
        self.frame_atom_results.setFrameShape(QFrame.StyledPanel)
        self.frame_atom_results.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_atom_results)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_atom_results_fix = QFrame(self.frame_atom_results)
        self.frame_atom_results_fix.setObjectName(u"frame_atom_results_fix")
        self.frame_atom_results_fix.setMinimumSize(QSize(350, 383))
        self.frame_atom_results_fix.setMaximumSize(QSize(16777215, 16777215))
        self.frame_atom_results_fix.setFrameShape(QFrame.StyledPanel)
        self.frame_atom_results_fix.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_atom_results_fix)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_Atom_results = QGroupBox(self.frame_atom_results_fix)
        self.groupBox_Atom_results.setObjectName(u"groupBox_Atom_results")
        self.groupBox_Atom_results.setAutoFillBackground(False)
        self.groupBox_Atom_results.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_Atom_results)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.groupBox_Atom_results)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 151, 21))

        self.horizontalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_atom_number = QLabel(self.frame_6)
        self.label_atom_number.setObjectName(u"label_atom_number")
        self.label_atom_number.setLayoutDirection(Qt.LeftToRight)
        self.label_atom_number.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_atom_number)


        self.horizontalLayout_4.addWidget(self.frame_6)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame_44 = QFrame(self.groupBox_Atom_results)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMaximumSize(QSize(16777215, 50))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(150, 0))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_45)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_13 = QLabel(self.frame_45)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_29.addWidget(self.label_13)


        self.horizontalLayout_11.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frame_44)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_cloud_temperature = QLabel(self.frame_46)
        self.label_cloud_temperature.setObjectName(u"label_cloud_temperature")
        self.label_cloud_temperature.setLayoutDirection(Qt.LeftToRight)
        self.label_cloud_temperature.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_cloud_temperature)


        self.horizontalLayout_11.addWidget(self.frame_46)


        self.verticalLayout_6.addWidget(self.frame_44)

        self.frame = QFrame(self.groupBox_Atom_results)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame)

        self.frame_47 = QFrame(self.groupBox_Atom_results)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMaximumSize(QSize(16777215, 40))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_47)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.absorption_imaging_layout = QHBoxLayout(self.frame_49)
        self.absorption_imaging_layout.setSpacing(0)
        self.absorption_imaging_layout.setObjectName(u"absorption_imaging_layout")
        self.absorption_imaging_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_12.addWidget(self.frame_49)

        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.flouracence_imaging_layout = QHBoxLayout(self.frame_48)
        self.flouracence_imaging_layout.setSpacing(0)
        self.flouracence_imaging_layout.setObjectName(u"flouracence_imaging_layout")
        self.flouracence_imaging_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_12.addWidget(self.frame_48)


        self.verticalLayout_6.addWidget(self.frame_47)


        self.verticalLayout_5.addWidget(self.groupBox_Atom_results)


        self.verticalLayout_4.addWidget(self.frame_atom_results_fix)


        self.verticalLayout_3.addWidget(self.frame_atom_results)

        self.frame_atom_spear = QFrame(self.frame_atom_2)
        self.frame_atom_spear.setObjectName(u"frame_atom_spear")
        self.frame_atom_spear.setFrameShape(QFrame.StyledPanel)
        self.frame_atom_spear.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_atom_spear)


        self.horizontalLayout.addWidget(self.frame_atom_2)


        self.page_3_layout.addWidget(self.frame_atom_main)

        self.pages.addWidget(self.page_atom)
        self.page_analysis = QWidget()
        self.page_analysis.setObjectName(u"page_analysis")
        self.verticalLayout_2 = QVBoxLayout(self.page_analysis)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_label_2 = QLabel(self.page_analysis)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setMaximumSize(QSize(16777215, 40))
        self.title_label_2.setFont(font)
        self.title_label_2.setStyleSheet(u"font-size: 16pt")
        self.title_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title_label_2)

        self.frame_analysis_main = QFrame(self.page_analysis)
        self.frame_analysis_main.setObjectName(u"frame_analysis_main")
        self.frame_analysis_main.setFrameShape(QFrame.StyledPanel)
        self.frame_analysis_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_analysis_main)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_analysis_main_2 = QFrame(self.frame_analysis_main)
        self.frame_analysis_main_2.setObjectName(u"frame_analysis_main_2")
        self.frame_analysis_main_2.setFrameShape(QFrame.NoFrame)
        self.frame_analysis_main_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_analysis_main_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_analysis_3 = QFrame(self.frame_analysis_main_2)
        self.frame_analysis_3.setObjectName(u"frame_analysis_3")
        self.frame_analysis_3.setMaximumSize(QSize(800, 16777215))
        self.frame_analysis_3.setFrameShape(QFrame.StyledPanel)
        self.frame_analysis_3.setFrameShadow(QFrame.Raised)
        self.no_frame_2 = QVBoxLayout(self.frame_analysis_3)
        self.no_frame_2.setSpacing(0)
        self.no_frame_2.setObjectName(u"no_frame_2")
        self.no_frame_2.setContentsMargins(0, 0, 0, 0)
        self.frame_analysis_graph = QFrame(self.frame_analysis_3)
        self.frame_analysis_graph.setObjectName(u"frame_analysis_graph")
        self.frame_analysis_graph.setMaximumSize(QSize(800, 600))
        self.frame_analysis_graph.setFrameShape(QFrame.NoFrame)
        self.frame_analysis_graph.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_analysis_graph)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.graphicsView_analysis = PlotWidget(self.frame_analysis_graph)
        self.graphicsView_analysis.setObjectName(u"graphicsView_analysis")

        self.verticalLayout_7.addWidget(self.graphicsView_analysis)


        self.no_frame_2.addWidget(self.frame_analysis_graph)

        self.frame_down_analysis_2 = QFrame(self.frame_analysis_3)
        self.frame_down_analysis_2.setObjectName(u"frame_down_analysis_2")
        self.frame_down_analysis_2.setFrameShape(QFrame.NoFrame)
        self.frame_down_analysis_2.setFrameShadow(QFrame.Raised)
        self.excel_setting_analysis_layout = QVBoxLayout(self.frame_down_analysis_2)
        self.excel_setting_analysis_layout.setSpacing(0)
        self.excel_setting_analysis_layout.setObjectName(u"excel_setting_analysis_layout")
        self.excel_setting_analysis_layout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_analysis_excel = QGroupBox(self.frame_down_analysis_2)
        self.groupBox_analysis_excel.setObjectName(u"groupBox_analysis_excel")
        self.groupBox_analysis_excel.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_analysis_excel)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_4 = QFrame(self.groupBox_analysis_excel)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_4)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_16)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(70, 25))
        self.frame_18.setMaximumSize(QSize(16777215, 30))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_18)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 81, 21))

        self.verticalLayout_16.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 35))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.excel_file_analysis_location_layout = QHBoxLayout(self.frame_19)
        self.excel_file_analysis_location_layout.setSpacing(0)
        self.excel_file_analysis_location_layout.setObjectName(u"excel_file_analysis_location_layout")
        self.excel_file_analysis_location_layout.setContentsMargins(5, 5, 5, 5)
        self.lineEdit_analysis_excel_name = QLineEdit(self.frame_19)
        self.lineEdit_analysis_excel_name.setObjectName(u"lineEdit_analysis_excel_name")

        self.excel_file_analysis_location_layout.addWidget(self.lineEdit_analysis_excel_name)


        self.verticalLayout_16.addWidget(self.frame_19)


        self.verticalLayout_15.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_17)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(70, 25))
        self.frame_20.setMaximumSize(QSize(16777215, 30))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_20)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 0, 81, 21))

        self.verticalLayout_17.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_17)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 35))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.sheet_name_analysis_layout = QHBoxLayout(self.frame_21)
        self.sheet_name_analysis_layout.setSpacing(0)
        self.sheet_name_analysis_layout.setObjectName(u"sheet_name_analysis_layout")
        self.sheet_name_analysis_layout.setContentsMargins(5, 5, 5, 5)
        self.lineEdit_analysis_sheet_name = QLineEdit(self.frame_21)
        self.lineEdit_analysis_sheet_name.setObjectName(u"lineEdit_analysis_sheet_name")

        self.sheet_name_analysis_layout.addWidget(self.lineEdit_analysis_sheet_name)


        self.verticalLayout_17.addWidget(self.frame_21)


        self.verticalLayout_15.addWidget(self.frame_17)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.load_excel_settings_layout = QHBoxLayout(self.frame_9)
        self.load_excel_settings_layout.setObjectName(u"load_excel_settings_layout")
        self.load_excel_settings_layout.setContentsMargins(4, -1, 4, -1)
        self.analysis_clean_all_btn = QPushButton(self.frame_9)
        self.analysis_clean_all_btn.setObjectName(u"analysis_clean_all_btn")

        self.load_excel_settings_layout.addWidget(self.analysis_clean_all_btn)


        self.verticalLayout_15.addWidget(self.frame_9)


        self.horizontalLayout_6.addWidget(self.frame_4)

        self.frame_15 = QFrame(self.groupBox_analysis_excel)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_15)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_23)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_23)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.layout_send_excel_parameters = QVBoxLayout(self.frame_38)
        self.layout_send_excel_parameters.setSpacing(0)
        self.layout_send_excel_parameters.setObjectName(u"layout_send_excel_parameters")
        self.layout_send_excel_parameters.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_25.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_23)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.layout_send_excel_parameters_2 = QHBoxLayout(self.frame_39)
        self.layout_send_excel_parameters_2.setSpacing(0)
        self.layout_send_excel_parameters_2.setObjectName(u"layout_send_excel_parameters_2")
        self.layout_send_excel_parameters_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_25.addWidget(self.frame_39)


        self.horizontalLayout_10.addWidget(self.frame_23)


        self.horizontalLayout_6.addWidget(self.frame_15)


        self.excel_setting_analysis_layout.addWidget(self.groupBox_analysis_excel)


        self.no_frame_2.addWidget(self.frame_down_analysis_2)


        self.horizontalLayout_5.addWidget(self.frame_analysis_3)

        self.frame_atom_4 = QFrame(self.frame_analysis_main_2)
        self.frame_atom_4.setObjectName(u"frame_atom_4")
        self.frame_atom_4.setFrameShape(QFrame.StyledPanel)
        self.frame_atom_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_atom_4)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_analysis_graph_settings = QFrame(self.frame_atom_4)
        self.frame_analysis_graph_settings.setObjectName(u"frame_analysis_graph_settings")
        self.frame_analysis_graph_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_analysis_graph_settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_analysis_graph_settings)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_analysis_graph_settings_2 = QFrame(self.frame_analysis_graph_settings)
        self.frame_analysis_graph_settings_2.setObjectName(u"frame_analysis_graph_settings_2")
        self.frame_analysis_graph_settings_2.setMinimumSize(QSize(350, 383))
        self.frame_analysis_graph_settings_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_analysis_graph_settings_2.setFrameShape(QFrame.StyledPanel)
        self.frame_analysis_graph_settings_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_analysis_graph_settings_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.groupBox_analysis_graph_settings = QGroupBox(self.frame_analysis_graph_settings_2)
        self.groupBox_analysis_graph_settings.setObjectName(u"groupBox_analysis_graph_settings")
        self.groupBox_analysis_graph_settings.setAutoFillBackground(False)
        self.groupBox_analysis_graph_settings.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_analysis_graph_settings)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_7 = QFrame(self.groupBox_analysis_graph_settings)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 40))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QFrame(self.frame_7)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_14 = QLabel(self.frame_50)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_25.addWidget(self.label_14)

        self.lineEdit_analysis_main_title = QLineEdit(self.frame_50)
        self.lineEdit_analysis_main_title.setObjectName(u"lineEdit_analysis_main_title")

        self.horizontalLayout_25.addWidget(self.lineEdit_analysis_main_title)


        self.horizontalLayout_24.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.frame_7)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_24.addWidget(self.frame_51)


        self.verticalLayout_11.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.groupBox_analysis_graph_settings)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 40))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.frame_8)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_15 = QLabel(self.frame_52)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_28.addWidget(self.label_15)

        self.lineEdit_analysis_x_title = QLineEdit(self.frame_52)
        self.lineEdit_analysis_x_title.setObjectName(u"lineEdit_analysis_x_title")

        self.horizontalLayout_28.addWidget(self.lineEdit_analysis_x_title)


        self.horizontalLayout_26.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_8)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_16 = QLabel(self.frame_53)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_27.addWidget(self.label_16)

        self.lineEdit_analysis_y_title = QLineEdit(self.frame_53)
        self.lineEdit_analysis_y_title.setObjectName(u"lineEdit_analysis_y_title")

        self.horizontalLayout_27.addWidget(self.lineEdit_analysis_y_title)


        self.horizontalLayout_26.addWidget(self.frame_53)


        self.verticalLayout_11.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.groupBox_analysis_graph_settings)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_10)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, -1, 0)
        self.frame_54 = QFrame(self.frame_10)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_54)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_61 = QFrame(self.frame_54)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_17 = QLabel(self.frame_61)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_29.addWidget(self.label_17)

        self.comboBox_analysis_box_location = QComboBox(self.frame_61)
        self.comboBox_analysis_box_location.setObjectName(u"comboBox_analysis_box_location")

        self.horizontalLayout_29.addWidget(self.comboBox_analysis_box_location)


        self.verticalLayout_33.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.frame_54)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)

        self.verticalLayout_33.addWidget(self.frame_62)


        self.gridLayout.addWidget(self.frame_54, 0, 0, 1, 1)

        self.frame_60 = QFrame(self.frame_10)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_60)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")

        self.gridLayout.addWidget(self.frame_60, 0, 1, 1, 1)

        self.frame_55 = QFrame(self.frame_10)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_55)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.frame_55, 1, 0, 1, 1)

        self.frame_59 = QFrame(self.frame_10)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_59)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")

        self.gridLayout.addWidget(self.frame_59, 1, 1, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_10)


        self.verticalLayout_10.addWidget(self.groupBox_analysis_graph_settings)


        self.verticalLayout_9.addWidget(self.frame_analysis_graph_settings_2)


        self.verticalLayout_8.addWidget(self.frame_analysis_graph_settings)

        self.frame_analysis_fit_settings = QFrame(self.frame_atom_4)
        self.frame_analysis_fit_settings.setObjectName(u"frame_analysis_fit_settings")
        self.frame_analysis_fit_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_analysis_fit_settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_analysis_fit_settings)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_analysis_graph_settings_3 = QFrame(self.frame_analysis_fit_settings)
        self.frame_analysis_graph_settings_3.setObjectName(u"frame_analysis_graph_settings_3")
        self.frame_analysis_graph_settings_3.setMinimumSize(QSize(350, 383))
        self.frame_analysis_graph_settings_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_analysis_graph_settings_3.setFrameShape(QFrame.StyledPanel)
        self.frame_analysis_graph_settings_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_analysis_graph_settings_3)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.groupBox_analysis_fit_settings = QGroupBox(self.frame_analysis_graph_settings_3)
        self.groupBox_analysis_fit_settings.setObjectName(u"groupBox_analysis_fit_settings")
        self.groupBox_analysis_fit_settings.setAutoFillBackground(False)
        self.groupBox_analysis_fit_settings.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_analysis_fit_settings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.groupBox_analysis_fit_settings)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 40))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(80, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_12)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 151, 21))

        self.horizontalLayout_9.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.comboBox_analysis_x_axis = QComboBox(self.frame_13)
        self.comboBox_analysis_x_axis.setObjectName(u"comboBox_analysis_x_axis")

        self.horizontalLayout_16.addWidget(self.comboBox_analysis_x_axis)


        self.horizontalLayout_9.addWidget(self.frame_13)


        self.verticalLayout_13.addWidget(self.frame_11)

        self.frame_22 = QFrame(self.groupBox_analysis_fit_settings)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 40))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_22)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(80, 16777215))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_26)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 151, 21))

        self.horizontalLayout_20.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_22)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.comboBox_analysis_y_axis = QComboBox(self.frame_27)
        self.comboBox_analysis_y_axis.setObjectName(u"comboBox_analysis_y_axis")

        self.horizontalLayout_17.addWidget(self.comboBox_analysis_y_axis)


        self.horizontalLayout_20.addWidget(self.frame_27)


        self.verticalLayout_13.addWidget(self.frame_22)

        self.frame_24 = QFrame(self.groupBox_analysis_fit_settings)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 40))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_24)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(80, 16777215))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_28)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 151, 21))

        self.horizontalLayout_21.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_24)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.comboBox_analysis_x_error = QComboBox(self.frame_29)
        self.comboBox_analysis_x_error.setObjectName(u"comboBox_analysis_x_error")

        self.horizontalLayout_18.addWidget(self.comboBox_analysis_x_error)


        self.horizontalLayout_21.addWidget(self.frame_29)


        self.verticalLayout_13.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.groupBox_analysis_fit_settings)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(16777215, 40))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_25)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(80, 16777215))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_30)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 151, 21))

        self.horizontalLayout_22.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_25)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.comboBox_analysis_y_error = QComboBox(self.frame_31)
        self.comboBox_analysis_y_error.setObjectName(u"comboBox_analysis_y_error")

        self.horizontalLayout_19.addWidget(self.comboBox_analysis_y_error)


        self.horizontalLayout_22.addWidget(self.frame_31)


        self.verticalLayout_13.addWidget(self.frame_25)

        self.frame_14 = QFrame(self.groupBox_analysis_fit_settings)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_14)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_14)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_33)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_33)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_11 = QLabel(self.frame_42)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_31.addWidget(self.label_11)

        self.lineEdit_analysis_initial_a = QLineEdit(self.frame_42)
        self.lineEdit_analysis_initial_a.setObjectName(u"lineEdit_analysis_initial_a")

        self.horizontalLayout_31.addWidget(self.lineEdit_analysis_initial_a)


        self.verticalLayout_19.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_33)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_18 = QLabel(self.frame_43)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_33.addWidget(self.label_18)

        self.lineEdit_analysis_initial_b = QLineEdit(self.frame_43)
        self.lineEdit_analysis_initial_b.setObjectName(u"lineEdit_analysis_initial_b")

        self.horizontalLayout_33.addWidget(self.lineEdit_analysis_initial_b)


        self.verticalLayout_19.addWidget(self.frame_43)


        self.gridLayout_2.addWidget(self.frame_33, 1, 0, 1, 1)

        self.frame_34 = QFrame(self.frame_14)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_34)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_34, 1, 1, 1, 1)

        self.frame_32 = QFrame(self.frame_14)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_32)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.frame_32)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_3 = QLabel(self.frame_36)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_23.addWidget(self.label_3)

        self.comboBox_analysis_fit_function = QComboBox(self.frame_36)
        self.comboBox_analysis_fit_function.setObjectName(u"comboBox_analysis_fit_function")

        self.horizontalLayout_23.addWidget(self.comboBox_analysis_fit_function)


        self.verticalLayout_18.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_32)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_10 = QLabel(self.frame_37)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_30.addWidget(self.label_10)

        self.comboBox_analysis_cost_function = QComboBox(self.frame_37)
        self.comboBox_analysis_cost_function.setObjectName(u"comboBox_analysis_cost_function")

        self.horizontalLayout_30.addWidget(self.comboBox_analysis_cost_function)


        self.verticalLayout_18.addWidget(self.frame_37)


        self.gridLayout_2.addWidget(self.frame_32, 0, 0, 1, 1)

        self.frame_35 = QFrame(self.frame_14)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.frame_65 = QFrame(self.frame_35)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_65)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_67 = QFrame(self.frame_65)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_38 = QLabel(self.frame_67)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(80, 16777215))
        self.label_38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.label_38)

        self.label_39 = QLabel(self.frame_67)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(10, 16777215))

        self.horizontalLayout_42.addWidget(self.label_39)

        self.lineEdit_analysis_s_limit_a = QLineEdit(self.frame_67)
        self.lineEdit_analysis_s_limit_a.setObjectName(u"lineEdit_analysis_s_limit_a")
        self.lineEdit_analysis_s_limit_a.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_42.addWidget(self.lineEdit_analysis_s_limit_a)

        self.label_40 = QLabel(self.frame_67)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(10, 16777215))
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.label_40)

        self.lineEdit_analysis_f_limit_a = QLineEdit(self.frame_67)
        self.lineEdit_analysis_f_limit_a.setObjectName(u"lineEdit_analysis_f_limit_a")
        self.lineEdit_analysis_f_limit_a.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_42.addWidget(self.lineEdit_analysis_f_limit_a)


        self.verticalLayout_21.addWidget(self.frame_67)

        self.frame_analysis_f_limit_b = QFrame(self.frame_65)
        self.frame_analysis_f_limit_b.setObjectName(u"frame_analysis_f_limit_b")
        self.frame_analysis_f_limit_b.setFrameShape(QFrame.StyledPanel)
        self.frame_analysis_f_limit_b.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_analysis_f_limit_b)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_35 = QLabel(self.frame_analysis_f_limit_b)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(80, 16777215))
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_analysis_f_limit_b)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(10, 16777215))

        self.horizontalLayout_41.addWidget(self.label_36)

        self.lineEdit_analysis_s_limit_b = QLineEdit(self.frame_analysis_f_limit_b)
        self.lineEdit_analysis_s_limit_b.setObjectName(u"lineEdit_analysis_s_limit_b")
        self.lineEdit_analysis_s_limit_b.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_41.addWidget(self.lineEdit_analysis_s_limit_b)

        self.label_37 = QLabel(self.frame_analysis_f_limit_b)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(10, 16777215))
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.label_37)

        self.lineEdit_19 = QLineEdit(self.frame_analysis_f_limit_b)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_41.addWidget(self.lineEdit_19)


        self.verticalLayout_21.addWidget(self.frame_analysis_f_limit_b)


        self.horizontalLayout_43.addWidget(self.frame_65)

        self.frame_63 = QFrame(self.frame_35)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_63)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.fit_analysis_btn = QPushButton(self.frame_63)
        self.fit_analysis_btn.setObjectName(u"fit_analysis_btn")

        self.verticalLayout_22.addWidget(self.fit_analysis_btn)

        self.matplotlib_fit_analsis_btn = QPushButton(self.frame_63)
        self.matplotlib_fit_analsis_btn.setObjectName(u"matplotlib_fit_analsis_btn")

        self.verticalLayout_22.addWidget(self.matplotlib_fit_analsis_btn)


        self.horizontalLayout_43.addWidget(self.frame_63)


        self.gridLayout_2.addWidget(self.frame_35, 0, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_14)


        self.verticalLayout_12.addWidget(self.groupBox_analysis_fit_settings)


        self.verticalLayout_14.addWidget(self.frame_analysis_graph_settings_3)


        self.verticalLayout_8.addWidget(self.frame_analysis_fit_settings)


        self.horizontalLayout_5.addWidget(self.frame_atom_4)


        self.horizontalLayout_8.addWidget(self.frame_analysis_main_2)


        self.verticalLayout_2.addWidget(self.frame_analysis_main)

        self.pages.addWidget(self.page_analysis)

        self.excel_settings_load_btn_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To PSI Experiment", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Fringes Measurements", None))
        self.atom_page_label.setText(QCoreApplication.translate("MainPages", u"Atom Measurements", None))
        self.label_wit_cloud_path.setText(QCoreApplication.translate("MainPages", u"With cloud path:", None))
        self.label_without_cloud_path.setText(QCoreApplication.translate("MainPages", u"Without cloud path:", None))
        self.groupBox_Atom_results.setTitle(QCoreApplication.translate("MainPages", u"Results", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Atoms Number:", None))
        self.label_atom_number.setText(QCoreApplication.translate("MainPages", u"0", None))
        self.label_13.setText(QCoreApplication.translate("MainPages", u"Cloud Temperature:", None))
        self.label_cloud_temperature.setText(QCoreApplication.translate("MainPages", u"0", None))
        self.title_label_2.setText(QCoreApplication.translate("MainPages", u"Analysis Measurements", None))
        self.groupBox_analysis_excel.setTitle(QCoreApplication.translate("MainPages", u"Excel Settings", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"Excel location:", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"Sheet name:", None))
        self.analysis_clean_all_btn.setText(QCoreApplication.translate("MainPages", u"Clean All", None))
        self.groupBox_analysis_graph_settings.setTitle(QCoreApplication.translate("MainPages", u"Graph Settings", None))
        self.label_14.setText(QCoreApplication.translate("MainPages", u"Main Title:", None))
        self.label_15.setText(QCoreApplication.translate("MainPages", u"X label title:", None))
        self.label_16.setText(QCoreApplication.translate("MainPages", u"Y label title:", None))
        self.label_17.setText(QCoreApplication.translate("MainPages", u"Box Location:", None))
        self.groupBox_analysis_fit_settings.setTitle(QCoreApplication.translate("MainPages", u"Fit Settings", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"X Axis:", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"Y Axis:", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"X error:", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"Y error:", None))
        self.label_11.setText(QCoreApplication.translate("MainPages", u"Initial Value a: ", None))
        self.label_18.setText(QCoreApplication.translate("MainPages", u"Initial Value b: ", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Fit Function:", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"Cost Function:", None))
        self.label_38.setText(QCoreApplication.translate("MainPages", u"Limits a:", None))
        self.label_39.setText(QCoreApplication.translate("MainPages", u"s", None))
        self.label_40.setText(QCoreApplication.translate("MainPages", u"f", None))
        self.label_35.setText(QCoreApplication.translate("MainPages", u"Limits b:", None))
        self.label_36.setText(QCoreApplication.translate("MainPages", u"s", None))
        self.label_37.setText(QCoreApplication.translate("MainPages", u"f", None))
        self.fit_analysis_btn.setText(QCoreApplication.translate("MainPages", u"Fit", None))
        self.matplotlib_fit_analsis_btn.setText(QCoreApplication.translate("MainPages", u"Export fit to MatPlotLib", None))
    # retranslateUi

