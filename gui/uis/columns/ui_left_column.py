# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'left_columnTtKlMH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(296, 641)
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(LeftColumn)
        self.menus.setObjectName(u"menus")
        self.menu_empty = QWidget()
        self.menu_empty.setObjectName(u"menu_empty")
        self.verticalLayout = QVBoxLayout(self.menu_empty)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.menus.addWidget(self.menu_empty)
        self.menu_atom = QWidget()
        self.menu_atom.setObjectName(u"menu_atom")
        self.verticalLayout_3 = QVBoxLayout(self.menu_atom)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_no_cloud = QFrame(self.menu_atom)
        self.frame_no_cloud.setObjectName(u"frame_no_cloud")
        self.frame_no_cloud.setMaximumSize(QSize(16777215, 80))
        self.frame_no_cloud.setFrameShape(QFrame.StyledPanel)
        self.frame_no_cloud.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_no_cloud)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_no_cloud = QLabel(self.frame_no_cloud)
        self.label_no_cloud.setObjectName(u"label_no_cloud")
        self.label_no_cloud.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_4.addWidget(self.label_no_cloud)

        self.frame_no_cloud_dialog = QFrame(self.frame_no_cloud)
        self.frame_no_cloud_dialog.setObjectName(u"frame_no_cloud_dialog")
        self.frame_no_cloud_dialog.setMinimumSize(QSize(0, 40))
        self.frame_no_cloud_dialog.setMaximumSize(QSize(16777215, 40))
        self.frame_no_cloud_dialog.setFrameShape(QFrame.StyledPanel)
        self.frame_no_cloud_dialog.setFrameShadow(QFrame.Raised)
        self.no_cloud_layout = QHBoxLayout(self.frame_no_cloud_dialog)
        self.no_cloud_layout.setObjectName(u"no_cloud_layout")
        self.no_cloud_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.frame_no_cloud_dialog)


        self.verticalLayout_3.addWidget(self.frame_no_cloud)

        self.frame_with_cloud = QFrame(self.menu_atom)
        self.frame_with_cloud.setObjectName(u"frame_with_cloud")
        self.frame_with_cloud.setMaximumSize(QSize(16777215, 80))
        self.frame_with_cloud.setFrameShape(QFrame.StyledPanel)
        self.frame_with_cloud.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_with_cloud)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_with_cloud = QLabel(self.frame_with_cloud)
        self.label_with_cloud.setObjectName(u"label_with_cloud")
        self.label_with_cloud.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_5.addWidget(self.label_with_cloud)

        self.frame_with_cloud_dialog = QFrame(self.frame_with_cloud)
        self.frame_with_cloud_dialog.setObjectName(u"frame_with_cloud_dialog")
        self.frame_with_cloud_dialog.setMinimumSize(QSize(0, 40))
        self.frame_with_cloud_dialog.setMaximumSize(QSize(16777215, 40))
        self.frame_with_cloud_dialog.setFrameShape(QFrame.StyledPanel)
        self.frame_with_cloud_dialog.setFrameShadow(QFrame.Raised)
        self.with_cloud_layout = QVBoxLayout(self.frame_with_cloud_dialog)
        self.with_cloud_layout.setObjectName(u"with_cloud_layout")
        self.with_cloud_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_with_cloud_dialog)


        self.verticalLayout_3.addWidget(self.frame_with_cloud)

        self.frame_with_cloud_2 = QFrame(self.menu_atom)
        self.frame_with_cloud_2.setObjectName(u"frame_with_cloud_2")
        self.frame_with_cloud_2.setMaximumSize(QSize(16777215, 80))
        self.frame_with_cloud_2.setFrameShape(QFrame.StyledPanel)
        self.frame_with_cloud_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_with_cloud_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_with_cloud_2 = QLabel(self.frame_with_cloud_2)
        self.label_with_cloud_2.setObjectName(u"label_with_cloud_2")
        self.label_with_cloud_2.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_6.addWidget(self.label_with_cloud_2)

        self.frame_atom_automatic_dialog = QFrame(self.frame_with_cloud_2)
        self.frame_atom_automatic_dialog.setObjectName(u"frame_atom_automatic_dialog")
        self.frame_atom_automatic_dialog.setMinimumSize(QSize(0, 40))
        self.frame_atom_automatic_dialog.setMaximumSize(QSize(16777215, 40))
        self.frame_atom_automatic_dialog.setFrameShape(QFrame.StyledPanel)
        self.frame_atom_automatic_dialog.setFrameShadow(QFrame.Raised)
        self.aoutomatic_pull_atom_layout = QVBoxLayout(self.frame_atom_automatic_dialog)
        self.aoutomatic_pull_atom_layout.setObjectName(u"aoutomatic_pull_atom_layout")
        self.aoutomatic_pull_atom_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_6.addWidget(self.frame_atom_automatic_dialog)


        self.verticalLayout_3.addWidget(self.frame_with_cloud_2)

        self.frame_atom_temp = QFrame(self.menu_atom)
        self.frame_atom_temp.setObjectName(u"frame_atom_temp")
        self.frame_atom_temp.setFrameShape(QFrame.StyledPanel)
        self.frame_atom_temp.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_atom_temp)

        self.menus.addWidget(self.menu_atom)
        self.menu_fringes = QWidget()
        self.menu_fringes.setObjectName(u"menu_fringes")
        self.verticalLayout_2 = QVBoxLayout(self.menu_fringes)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.btn_4_widget = QWidget(self.menu_fringes)
        self.btn_4_widget.setObjectName(u"btn_4_widget")
        self.btn_4_widget.setMinimumSize(QSize(0, 40))
        self.btn_4_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_4_layout = QVBoxLayout(self.btn_4_widget)
        self.btn_4_layout.setSpacing(0)
        self.btn_4_layout.setObjectName(u"btn_4_layout")
        self.btn_4_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_4_widget)

        self.label_2 = QLabel(self.menu_fringes)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 16pt")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.menu_fringes)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font-size: 9pt")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.menus.addWidget(self.menu_fringes)
        self.menu_analysis = QWidget()
        self.menu_analysis.setObjectName(u"menu_analysis")
        self.verticalLayout_8 = QVBoxLayout(self.menu_analysis)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_excel_dialog = QFrame(self.menu_analysis)
        self.frame_excel_dialog.setObjectName(u"frame_excel_dialog")
        self.frame_excel_dialog.setMinimumSize(QSize(0, 40))
        self.frame_excel_dialog.setMaximumSize(QSize(16777215, 40))
        self.frame_excel_dialog.setFrameShape(QFrame.StyledPanel)
        self.frame_excel_dialog.setFrameShadow(QFrame.Raised)
        self.excel_file_path_btn_layout = QHBoxLayout(self.frame_excel_dialog)
        self.excel_file_path_btn_layout.setObjectName(u"excel_file_path_btn_layout")
        self.excel_file_path_btn_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.frame_excel_dialog)

        self.frame_upload_sheet_name = QFrame(self.menu_analysis)
        self.frame_upload_sheet_name.setObjectName(u"frame_upload_sheet_name")
        self.frame_upload_sheet_name.setMaximumSize(QSize(16777215, 80))
        self.frame_upload_sheet_name.setFrameShape(QFrame.StyledPanel)
        self.frame_upload_sheet_name.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_upload_sheet_name)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)

        self.verticalLayout_8.addWidget(self.frame_upload_sheet_name)

        self.frame_analysis_load = QFrame(self.menu_analysis)
        self.frame_analysis_load.setObjectName(u"frame_analysis_load")
        self.frame_analysis_load.setMaximumSize(QSize(16777215, 40))
        self.frame_analysis_load.setFrameShape(QFrame.StyledPanel)
        self.frame_analysis_load.setFrameShadow(QFrame.Raised)
        self.load_btn_analysis_layout = QHBoxLayout(self.frame_analysis_load)
        self.load_btn_analysis_layout.setSpacing(0)
        self.load_btn_analysis_layout.setObjectName(u"load_btn_analysis_layout")
        self.load_btn_analysis_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.frame_analysis_load)

        self.frame_analysis_temp_2 = QFrame(self.menu_analysis)
        self.frame_analysis_temp_2.setObjectName(u"frame_analysis_temp_2")
        self.frame_analysis_temp_2.setFrameShape(QFrame.StyledPanel)
        self.frame_analysis_temp_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_analysis_temp_2)

        self.menus.addWidget(self.menu_analysis)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(LeftColumn)
    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
        self.label_no_cloud.setText(QCoreApplication.translate("LeftColumn", u"Open image - no cloud", None))
        self.label_with_cloud.setText(QCoreApplication.translate("LeftColumn", u"Open image - with cloud", None))
        self.label_with_cloud_2.setText(QCoreApplication.translate("LeftColumn", u"Automatic pull", None))
        self.label_2.setText(QCoreApplication.translate("LeftColumn", u"Menu 2 - Left Menu", None))
        self.label_3.setText(QCoreApplication.translate("LeftColumn", u"This is just an example menu.\n"
"Add Qt Widgets or your custom widgets here.", None))
    # retranslateUi

