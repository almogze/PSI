# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagestHnMxo.ui'
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
        MainPages.resize(1206, 868)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
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
        self.frame_atom_graph.setMaximumSize(QSize(800, 450))
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
        self.vboxLayout = QVBoxLayout(self.frame_atom_analysis)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_atom_graph_btns = QFrame(self.frame_atom_analysis)
        self.frame_atom_graph_btns.setObjectName(u"frame_atom_graph_btns")
        self.frame_atom_graph_btns.setMaximumSize(QSize(16777215, 40))
        self.frame_atom_graph_btns.setFrameShape(QFrame.NoFrame)
        self.frame_atom_graph_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_atom_graph_btns)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_atom_graph_btn_gen = QFrame(self.frame_atom_graph_btns)
        self.frame_atom_graph_btn_gen.setObjectName(u"frame_atom_graph_btn_gen")
        self.frame_atom_graph_btn_gen.setMaximumSize(QSize(100, 16777215))
        self.frame_atom_graph_btn_gen.setFrameShape(QFrame.StyledPanel)
        self.frame_atom_graph_btn_gen.setFrameShadow(QFrame.Raised)
        self.btn_atom_graph_gen_layout = QHBoxLayout(self.frame_atom_graph_btn_gen)
        self.btn_atom_graph_gen_layout.setSpacing(0)
        self.btn_atom_graph_gen_layout.setObjectName(u"btn_atom_graph_gen_layout")
        self.btn_atom_graph_gen_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_atom_graph_btn_gen)

        self.frame_4 = QFrame(self.frame_atom_graph_btns)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(100, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.btn_atom_clear_layout = QVBoxLayout(self.frame_4)
        self.btn_atom_clear_layout.setSpacing(0)
        self.btn_atom_clear_layout.setObjectName(u"btn_atom_clear_layout")
        self.btn_atom_clear_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_4)


        self.vboxLayout.addWidget(self.frame_atom_graph_btns)

        self.frame_2 = QFrame(self.frame_atom_analysis)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.vboxLayout.addWidget(self.frame_2)


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
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_atom_results_fix = QFrame(self.frame_atom_results)
        self.frame_atom_results_fix.setObjectName(u"frame_atom_results_fix")
        self.frame_atom_results_fix.setMinimumSize(QSize(350, 383))
        self.frame_atom_results_fix.setMaximumSize(QSize(350, 383))
        self.frame_atom_results_fix.setFrameShape(QFrame.StyledPanel)
        self.frame_atom_results_fix.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_atom_results_fix)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.frame_atom_results_fix)
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
        self.label_atom_number = QLabel(self.frame_6)
        self.label_atom_number.setObjectName(u"label_atom_number")
        self.label_atom_number.setGeometry(QRect(10, 10, 101, 21))

        self.horizontalLayout_4.addWidget(self.frame_6)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_atom_results_fix)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame)


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

        self.verticalLayout_2.addWidget(self.frame_analysis_main)

        self.pages.addWidget(self.page_analysis)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To PSI Experiment", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Fringes Measurements", None))
        self.atom_page_label.setText(QCoreApplication.translate("MainPages", u"Atom Measurements", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Atoms Number:", None))
        self.label_atom_number.setText(QCoreApplication.translate("MainPages", u"0", None))
        self.title_label_2.setText(QCoreApplication.translate("MainPages", u"Analysis Measurements", None))
    # retranslateUi

