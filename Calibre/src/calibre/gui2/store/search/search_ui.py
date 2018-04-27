# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/store/search/search.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(872, 610)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("store.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.search_title = HistoryLineEdit2(Dialog)
        self.search_title.setClearButtonEnabled(True)
        self.search_title.setObjectName("search_title")
        self.gridLayout.addWidget(self.search_title, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.search_author = HistoryLineEdit2(Dialog)
        self.search_author.setClearButtonEnabled(True)
        self.search_author.setObjectName("search_author")
        self.gridLayout.addWidget(self.search_author, 1, 2, 1, 1)
        self.adv_search_button = QtWidgets.QToolButton(Dialog)
        self.adv_search_button.setObjectName("adv_search_button")
        self.gridLayout.addWidget(self.adv_search_button, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.search_edit = HistoryLineEdit2(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_edit.sizePolicy().hasHeightForWidth())
        self.search_edit.setSizePolicy(sizePolicy)
        self.search_edit.setClearButtonEnabled(True)
        self.search_edit.setObjectName("search_edit")
        self.gridLayout.addWidget(self.search_edit, 2, 2, 1, 1)
        self.store_splitter = QtWidgets.QSplitter(Dialog)
        self.store_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.store_splitter.setObjectName("store_splitter")
        self.groupBox = QtWidgets.QGroupBox(self.store_splitter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.store_list = QtWidgets.QScrollArea(self.groupBox)
        self.store_list.setWidgetResizable(True)
        self.store_list.setObjectName("store_list")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 205, 147))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.store_list.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.store_list)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.select_all_stores = QtWidgets.QPushButton(self.groupBox)
        self.select_all_stores.setObjectName("select_all_stores")
        self.verticalLayout.addWidget(self.select_all_stores)
        self.select_invert_stores = QtWidgets.QPushButton(self.groupBox)
        self.select_invert_stores.setObjectName("select_invert_stores")
        self.verticalLayout.addWidget(self.select_invert_stores)
        self.select_none_stores = QtWidgets.QPushButton(self.groupBox)
        self.select_none_stores.setObjectName("select_none_stores")
        self.verticalLayout.addWidget(self.select_none_stores)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.store_splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.results_view = ResultsView(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.results_view.sizePolicy().hasHeightForWidth())
        self.results_view.setSizePolicy(sizePolicy)
        self.results_view.setMinimumSize(QtCore.QSize(0, 0))
        self.results_view.setAlternatingRowColors(True)
        self.results_view.setIconSize(QtCore.QSize(32, 32))
        self.results_view.setRootIsDecorated(False)
        self.results_view.setUniformRowHeights(False)
        self.results_view.setItemsExpandable(False)
        self.results_view.setSortingEnabled(True)
        self.results_view.setExpandsOnDoubleClick(False)
        self.results_view.setObjectName("results_view")
        self.results_view.header().setStretchLastSection(False)
        self.verticalLayout_4.addWidget(self.results_view)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.configure = QtWidgets.QToolButton(self.verticalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(I("config.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.configure.setIcon(icon1)
        self.configure.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.configure.setObjectName("configure")
        self.horizontalLayout.addWidget(self.configure)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.open_external = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.open_external.setObjectName("open_external")
        self.horizontalLayout.addWidget(self.open_external)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.store_splitter, 3, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.button_layout = QtWidgets.QVBoxLayout()
        self.button_layout.setObjectName("button_layout")
        self.widget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setBaseSize(QtCore.QSize(24, 24))
        self.widget.setObjectName("widget")
        self.button_layout.addWidget(self.widget)
        self.search = QtWidgets.QPushButton(Dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(I("search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon2)
        self.search.setObjectName("search")
        self.button_layout.addWidget(self.search)
        self.gridLayout.addLayout(self.button_layout, 0, 3, 3, 1)
        self.bottom_layout = QtWidgets.QHBoxLayout()
        self.bottom_layout.setObjectName("bottom_layout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.bottom_layout.addWidget(self.label_2)
        self.total = QtWidgets.QLabel(Dialog)
        self.total.setObjectName("total")
        self.bottom_layout.addWidget(self.total)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_layout.addItem(spacerItem1)
        self.close = QtWidgets.QPushButton(Dialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(I("window-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon3)
        self.close.setObjectName("close")
        self.bottom_layout.addWidget(self.close)
        self.gridLayout.addLayout(self.bottom_layout, 4, 0, 1, 4)
        self.label_3.setBuddy(self.search_author)
        self.label.setBuddy(self.search_edit)
        self.label_4.setBuddy(self.search_title)

        self.retranslateUi(Dialog)
        self.close.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.search_title, self.search_author)
        Dialog.setTabOrder(self.search_author, self.adv_search_button)
        Dialog.setTabOrder(self.adv_search_button, self.search_edit)
        Dialog.setTabOrder(self.search_edit, self.search)
        Dialog.setTabOrder(self.search, self.store_list)
        Dialog.setTabOrder(self.store_list, self.select_all_stores)
        Dialog.setTabOrder(self.select_all_stores, self.select_invert_stores)
        Dialog.setTabOrder(self.select_invert_stores, self.select_none_stores)
        Dialog.setTabOrder(self.select_none_stores, self.results_view)
        Dialog.setTabOrder(self.results_view, self.configure)
        Dialog.setTabOrder(self.configure, self.open_external)
        Dialog.setTabOrder(self.open_external, self.close)

    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(_("Get books"))
        self.search_title.setPlaceholderText(_("Search by title"))
        self.label_3.setText(_("&Author:"))
        self.search_author.setPlaceholderText(_("Search by author"))
        self.adv_search_button.setText(_("..."))
        self.label.setText(_("&Keyword:"))
        self.search_edit.setPlaceholderText(_("Search by any keyword"))
        self.groupBox.setTitle(_("Stores"))
        self.select_all_stores.setText(_("Select &all"))
        self.select_invert_stores.setText(_("&Invert selection"))
        self.select_none_stores.setText(_("Select &none"))
        self.configure.setToolTip(_("Configure Get books behavior"))
        self.configure.setText(_("&Configure"))
        self.open_external.setToolTip(_("Open a selected book in the system\'s web browser"))
        self.open_external.setText(_("Open in &external browser"))
        self.label_4.setText(_("&Title:"))
        self.search.setText(_("&Search"))
        self.label_2.setText(_("Books:"))
        self.total.setText(_("0"))
        self.close.setText(_("&Close"))

from calibre.gui2.widgets2 import HistoryLineEdit2
from results_view import ResultsView
