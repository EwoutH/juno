# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LensCreator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LensCreator(object):
    def setupUi(self, LensCreator):
        LensCreator.setObjectName("LensCreator")
        LensCreator.resize(1009, 431)
        self.centralwidget = QtWidgets.QWidget(LensCreator)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_Main = QtWidgets.QFrame(self.centralwidget)
        self.frame_Main.setMaximumSize(QtCore.QSize(1536, 1024))
        self.frame_Main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Main.setObjectName("frame_Main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_Main)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_Config = QtWidgets.QFrame(self.frame_Main)
        self.frame_Config.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_Config.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_Config.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Config.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Config.setObjectName("frame_Config")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_Config)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_Config)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_General = QtWidgets.QWidget()
        self.tab_General.setObjectName("tab_General")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_General)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_PixelSize = QtWidgets.QFrame(self.tab_General)
        self.frame_PixelSize.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_PixelSize.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_PixelSize.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_PixelSize.setObjectName("frame_PixelSize")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_PixelSize)
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_PixelSize = QtWidgets.QLabel(self.frame_PixelSize)
        self.label_PixelSize.setObjectName("label_PixelSize")
        self.horizontalLayout_3.addWidget(self.label_PixelSize)
        self.doubleSpinBox_PixelSize = QtWidgets.QDoubleSpinBox(self.frame_PixelSize)
        self.doubleSpinBox_PixelSize.setDecimals(2)
        self.doubleSpinBox_PixelSize.setMinimum(0.01)
        self.doubleSpinBox_PixelSize.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSpinBox_PixelSize.setProperty("value", 0.01)
        self.doubleSpinBox_PixelSize.setObjectName("doubleSpinBox_PixelSize")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_PixelSize)
        self.verticalLayout_3.addWidget(self.frame_PixelSize)
        self.frame_LensDiameter = QtWidgets.QFrame(self.tab_General)
        self.frame_LensDiameter.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_LensDiameter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_LensDiameter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_LensDiameter.setObjectName("frame_LensDiameter")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_LensDiameter)
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_LensDiameter = QtWidgets.QLabel(self.frame_LensDiameter)
        self.label_LensDiameter.setObjectName("label_LensDiameter")
        self.horizontalLayout_4.addWidget(self.label_LensDiameter)
        self.doubleSpinBox_LensDiameter = QtWidgets.QDoubleSpinBox(self.frame_LensDiameter)
        self.doubleSpinBox_LensDiameter.setMinimum(0.1)
        self.doubleSpinBox_LensDiameter.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSpinBox_LensDiameter.setProperty("value", 1.0)
        self.doubleSpinBox_LensDiameter.setObjectName("doubleSpinBox_LensDiameter")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_LensDiameter)
        self.verticalLayout_3.addWidget(self.frame_LensDiameter)
        self.frame_LensHeight = QtWidgets.QFrame(self.tab_General)
        self.frame_LensHeight.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_LensHeight.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_LensHeight.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_LensHeight.setObjectName("frame_LensHeight")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_LensHeight)
        self.horizontalLayout_5.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_LensHeight = QtWidgets.QLabel(self.frame_LensHeight)
        self.label_LensHeight.setObjectName("label_LensHeight")
        self.horizontalLayout_5.addWidget(self.label_LensHeight)
        self.doubleSpinBox_LensHeight = QtWidgets.QDoubleSpinBox(self.frame_LensHeight)
        self.doubleSpinBox_LensHeight.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSpinBox_LensHeight.setProperty("value", 1.0)
        self.doubleSpinBox_LensHeight.setObjectName("doubleSpinBox_LensHeight")
        self.horizontalLayout_5.addWidget(self.doubleSpinBox_LensHeight)
        self.verticalLayout_3.addWidget(self.frame_LensHeight)
        self.frame_LensExponent = QtWidgets.QFrame(self.tab_General)
        self.frame_LensExponent.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_LensExponent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_LensExponent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_LensExponent.setObjectName("frame_LensExponent")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_LensExponent)
        self.horizontalLayout_6.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_LensExponent = QtWidgets.QLabel(self.frame_LensExponent)
        self.label_LensExponent.setObjectName("label_LensExponent")
        self.horizontalLayout_6.addWidget(self.label_LensExponent)
        self.doubleSpinBox_LensExponent = QtWidgets.QDoubleSpinBox(self.frame_LensExponent)
        self.doubleSpinBox_LensExponent.setMaximum(3.0)
        self.doubleSpinBox_LensExponent.setSingleStep(0.1)
        self.doubleSpinBox_LensExponent.setProperty("value", 2.0)
        self.doubleSpinBox_LensExponent.setObjectName("doubleSpinBox_LensExponent")
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_LensExponent)
        self.verticalLayout_3.addWidget(self.frame_LensExponent)
        self.frame_LensMedium = QtWidgets.QFrame(self.tab_General)
        self.frame_LensMedium.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_LensMedium.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_LensMedium.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_LensMedium.setObjectName("frame_LensMedium")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_LensMedium)
        self.horizontalLayout_7.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_LensMedium = QtWidgets.QLabel(self.frame_LensMedium)
        self.label_LensMedium.setObjectName("label_LensMedium")
        self.horizontalLayout_7.addWidget(self.label_LensMedium)
        self.doubleSpinBox_LensMedium = QtWidgets.QDoubleSpinBox(self.frame_LensMedium)
        self.doubleSpinBox_LensMedium.setDecimals(3)
        self.doubleSpinBox_LensMedium.setMinimum(1.0)
        self.doubleSpinBox_LensMedium.setMaximum(5.0)
        self.doubleSpinBox_LensMedium.setSingleStep(0.1)
        self.doubleSpinBox_LensMedium.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSpinBox_LensMedium.setProperty("value", 2.348)
        self.doubleSpinBox_LensMedium.setObjectName("doubleSpinBox_LensMedium")
        self.horizontalLayout_7.addWidget(self.doubleSpinBox_LensMedium)
        self.verticalLayout_3.addWidget(self.frame_LensMedium)
        self.tabWidget.addTab(self.tab_General, "")
        self.tab_Gratings = QtWidgets.QWidget()
        self.tab_Gratings.setObjectName("tab_Gratings")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_Gratings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab_Gratings)
        self.groupBox.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(10, 72, 33, 20))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(10, 147, 33, 20))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_5.setGeometry(QtCore.QRect(10, 222, 33, 20))
        self.spinBox_5.setObjectName("spinBox_5")
        self.frame_6 = QtWidgets.QFrame(self.groupBox)
        self.frame_6.setGeometry(QtCore.QRect(50, 30, 201, 40))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.frame_6)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.horizontalLayout_8.addWidget(self.doubleSpinBox_6)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_Gratings, "")
        self.tab_Truncation = QtWidgets.QWidget()
        self.tab_Truncation.setObjectName("tab_Truncation")
        self.frame_7 = QtWidgets.QFrame(self.tab_Truncation)
        self.frame_7.setGeometry(QtCore.QRect(50, 60, 201, 40))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.frame_7)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.frame_7)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.horizontalLayout_9.addWidget(self.doubleSpinBox_7)
        self.tabWidget.addTab(self.tab_Truncation, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_Config, 0, 0, 2, 1)
        self.frame_Display = QtWidgets.QFrame(self.frame_Main)
        self.frame_Display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Display.setObjectName("frame_Display")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_Display)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_Profile = QtWidgets.QFrame(self.frame_Display)
        self.frame_Profile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Profile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Profile.setObjectName("frame_Profile")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_Profile)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_Profile = QtWidgets.QLabel(self.frame_Profile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Profile.sizePolicy().hasHeightForWidth())
        self.label_Profile.setSizePolicy(sizePolicy)
        self.label_Profile.setMinimumSize(QtCore.QSize(321, 321))
        self.label_Profile.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_Profile.setText("")
        self.label_Profile.setObjectName("label_Profile")
        self.gridLayout_3.addWidget(self.label_Profile, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_Profile)
        self.frame_CrossSection = QtWidgets.QFrame(self.frame_Display)
        self.frame_CrossSection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_CrossSection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_CrossSection.setObjectName("frame_CrossSection")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_CrossSection)
        self.gridLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_CrossSection = QtWidgets.QLabel(self.frame_CrossSection)
        self.label_CrossSection.setMinimumSize(QtCore.QSize(321, 321))
        self.label_CrossSection.setText("")
        self.label_CrossSection.setObjectName("label_CrossSection")
        self.gridLayout_4.addWidget(self.label_CrossSection, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_CrossSection)
        self.gridLayout_2.addWidget(self.frame_Display, 0, 1, 1, 1)
        self.frame_Buttons = QtWidgets.QFrame(self.frame_Main)
        self.frame_Buttons.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_Buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Buttons.setObjectName("frame_Buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_Buttons)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_GenerateProfile = QtWidgets.QPushButton(self.frame_Buttons)
        self.pushButton_GenerateProfile.setObjectName("pushButton_GenerateProfile")
        self.horizontalLayout.addWidget(self.pushButton_GenerateProfile)
        self.pushButton_LoadProfile = QtWidgets.QPushButton(self.frame_Buttons)
        self.pushButton_LoadProfile.setObjectName("pushButton_LoadProfile")
        self.horizontalLayout.addWidget(self.pushButton_LoadProfile)
        self.pushButton_SaveProfile = QtWidgets.QPushButton(self.frame_Buttons)
        self.pushButton_SaveProfile.setObjectName("pushButton_SaveProfile")
        self.horizontalLayout.addWidget(self.pushButton_SaveProfile)
        self.gridLayout_2.addWidget(self.frame_Buttons, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_Main)
        LensCreator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LensCreator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 21))
        self.menubar.setObjectName("menubar")
        LensCreator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LensCreator)
        self.statusbar.setObjectName("statusbar")
        LensCreator.setStatusBar(self.statusbar)

        self.retranslateUi(LensCreator)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LensCreator)

    def retranslateUi(self, LensCreator):
        _translate = QtCore.QCoreApplication.translate
        LensCreator.setWindowTitle(_translate("LensCreator", "MainWindow"))
        self.label_PixelSize.setText(_translate("LensCreator", "Pixel Size"))
        self.label_LensDiameter.setText(_translate("LensCreator", "Lens Diameter"))
        self.label_LensHeight.setText(_translate("LensCreator", "Lens Height"))
        self.label_LensExponent.setText(_translate("LensCreator", "Lens Exponent"))
        self.label_LensMedium.setText(_translate("LensCreator", "Lens Medium"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_General), _translate("LensCreator", "General"))
        self.groupBox.setTitle(_translate("LensCreator", "Grating Parameters"))
        self.label_6.setText(_translate("LensCreator", "Lens Medium"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Gratings), _translate("LensCreator", "Gratings"))
        self.label_7.setText(_translate("LensCreator", "Lens Medium"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Truncation), _translate("LensCreator", "Truncation"))
        self.pushButton_GenerateProfile.setText(_translate("LensCreator", "Generate Profile"))
        self.pushButton_LoadProfile.setText(_translate("LensCreator", "Load Profile"))
        self.pushButton_SaveProfile.setText(_translate("LensCreator", "Save Profile"))
