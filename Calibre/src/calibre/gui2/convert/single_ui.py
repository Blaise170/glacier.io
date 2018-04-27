# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/single.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("convert.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_label = QtWidgets.QLabel(Dialog)
        self.input_label.setObjectName("input_label")
        self.horizontalLayout.addWidget(self.input_label)
        self.input_formats = QtWidgets.QComboBox(Dialog)
        self.input_formats.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.input_formats.setMinimumContentsLength(5)
        self.input_formats.setObjectName("input_formats")
        self.horizontalLayout.addWidget(self.input_formats)
        self.opt_individual_saved_settings = QtWidgets.QCheckBox(Dialog)
        self.opt_individual_saved_settings.setObjectName("opt_individual_saved_settings")
        self.horizontalLayout.addWidget(self.opt_individual_saved_settings)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.output_formats = QtWidgets.QComboBox(Dialog)
        self.output_formats.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.output_formats.setMinimumContentsLength(5)
        self.output_formats.setObjectName("output_formats")
        self.horizontalLayout.addWidget(self.output_formats)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.groups = QtWidgets.QListView(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groups.sizePolicy().hasHeightForWidth())
        self.groups.setSizePolicy(sizePolicy)
        self.groups.setTabKeyNavigation(True)
        self.groups.setIconSize(QtCore.QSize(48, 48))
        self.groups.setWordWrap(True)
        self.groups.setObjectName("groups")
        self.gridLayout.addWidget(self.groups, 1, 0, 3, 1)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 810, 494))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stack = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy)
        self.stack.setObjectName("stack")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stack.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stack.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.stack)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)
        self.help = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help.sizePolicy().hasHeightForWidth())
        self.help.setSizePolicy(sizePolicy)
        self.help.setMaximumSize(QtCore.QSize(16777215, 130))
        self.help.setObjectName("help")
        self.gridLayout.addWidget(self.help, 2, 1, 1, 1)
        self.input_label.setBuddy(self.input_formats)
        self.label_2.setBuddy(self.output_formats)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(_("Dialog"))
        self.input_label.setText(_("&Input format:"))
        self.opt_individual_saved_settings.setText(_("Use &saved conversion settings for individual books"))
        self.label_2.setText(_("&Output format:"))


