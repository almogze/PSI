# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesSteJIh.ui'
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
        MainPages.resize(858, 592)
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
        self.scroll_area = QScrollArea(self.page_fringes)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 838, 572))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

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
        self.atom_page_label.setFont(font)
        self.atom_page_label.setAlignment(Qt.AlignCenter)

        self.page_3_layout.addWidget(self.atom_page_label)

        self.pages.addWidget(self.page_atom)
        self.page_analysis = QWidget()
        self.page_analysis.setObjectName(u"page_analysis")
        self.horizontalLayout = QHBoxLayout(self.page_analysis)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title_label_2 = QLabel(self.page_analysis)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setMaximumSize(QSize(16777215, 40))
        self.title_label_2.setFont(font)
        self.title_label_2.setStyleSheet(u"font-size: 16pt")
        self.title_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.title_label_2)

        self.pages.addWidget(self.page_analysis)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To PSI Experiment", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Fringes Measurements", None))
        self.atom_page_label.setText(QCoreApplication.translate("MainPages", u"Atom Measurements", None))
        self.title_label_2.setText(QCoreApplication.translate("MainPages", u"Analysis Measurements", None))
    # retranslateUi

