# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BeamCreator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BeamCreator(object):
    def setupUi(self, BeamCreator):
        BeamCreator.setObjectName("BeamCreator")
        BeamCreator.resize(1239, 875)
        BeamCreator.setMinimumSize(QtCore.QSize(0, 0))
        BeamCreator.setMaximumSize(QtCore.QSize(12312312, 16777215))
        self.centralwidget = QtWidgets.QWidget(BeamCreator)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_Main = QtWidgets.QFrame(self.centralwidget)
        self.frame_Main.setMaximumSize(QtCore.QSize(1600, 2000))
        self.frame_Main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Main.setObjectName("frame_Main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_Main)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_2.setHorizontalSpacing(1)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_Display = QtWidgets.QFrame(self.frame_Main)
        self.frame_Display.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_Display.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_Display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Display.setObjectName("frame_Display")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_Display)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.frame_4 = QtWidgets.QFrame(self.frame_Display)
        self.frame_4.setMinimumSize(QtCore.QSize(361, 45))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_4.setAutoFillBackground(True)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_TitleMask = QtWidgets.QLabel(self.frame_4)
        self.label_TitleMask.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_TitleMask.setAlignment(QtCore.Qt.AlignCenter)
        self.label_TitleMask.setObjectName("label_TitleMask")
        self.gridLayout_13.addWidget(self.label_TitleMask, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.frame_4, 0, 1, 1, 1)
        self.frame_ProfileMask = QtWidgets.QFrame(self.frame_Display)
        self.frame_ProfileMask.setMinimumSize(QtCore.QSize(448, 448))
        self.frame_ProfileMask.setMaximumSize(QtCore.QSize(448, 448))
        self.frame_ProfileMask.setAutoFillBackground(True)
        self.frame_ProfileMask.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ProfileMask.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ProfileMask.setObjectName("frame_ProfileMask")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_ProfileMask)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_Convergence = QtWidgets.QLabel(self.frame_ProfileMask)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Convergence.sizePolicy().hasHeightForWidth())
        self.label_Convergence.setSizePolicy(sizePolicy)
        self.label_Convergence.setMinimumSize(QtCore.QSize(448, 448))
        self.label_Convergence.setMaximumSize(QtCore.QSize(448, 448))
        self.label_Convergence.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_Convergence.setText("")
        self.label_Convergence.setObjectName("label_Convergence")
        self.gridLayout_9.addWidget(self.label_Convergence, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.frame_ProfileMask, 2, 1, 1, 1)
        self.frame_Profile = QtWidgets.QFrame(self.frame_Display)
        self.frame_Profile.setMinimumSize(QtCore.QSize(448, 448))
        self.frame_Profile.setMaximumSize(QtCore.QSize(448, 448))
        self.frame_Profile.setAutoFillBackground(True)
        self.frame_Profile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Profile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Profile.setObjectName("frame_Profile")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_Profile)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_Profile = QtWidgets.QLabel(self.frame_Profile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Profile.sizePolicy().hasHeightForWidth())
        self.label_Profile.setSizePolicy(sizePolicy)
        self.label_Profile.setMinimumSize(QtCore.QSize(448, 448))
        self.label_Profile.setMaximumSize(QtCore.QSize(448, 448))
        self.label_Profile.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_Profile.setText("")
        self.label_Profile.setObjectName("label_Profile")
        self.gridLayout_6.addWidget(self.label_Profile, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.frame_Profile, 2, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_Display)
        self.frame_3.setMinimumSize(QtCore.QSize(361, 45))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_TitleProfile = QtWidgets.QLabel(self.frame_3)
        self.label_TitleProfile.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_TitleProfile.setAlignment(QtCore.Qt.AlignCenter)
        self.label_TitleProfile.setObjectName("label_TitleProfile")
        self.gridLayout_12.addWidget(self.label_TitleProfile, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.frame_3, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem1, 3, 0, 1, 1)
        self.frame_Buttons = QtWidgets.QFrame(self.frame_Display)
        self.frame_Buttons.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame_Buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Buttons.setObjectName("frame_Buttons")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_Buttons)
        self.gridLayout_7.setVerticalSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_LensName = QtWidgets.QFrame(self.frame_Buttons)
        self.frame_LensName.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_LensName.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_LensName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_LensName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_LensName.setObjectName("frame_LensName")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_LensName)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_LensName = QtWidgets.QLabel(self.frame_LensName)
        self.label_LensName.setMinimumSize(QtCore.QSize(60, 0))
        self.label_LensName.setObjectName("label_LensName")
        self.horizontalLayout.addWidget(self.label_LensName)
        self.lineEdit_LensName = QtWidgets.QLineEdit(self.frame_LensName)
        self.lineEdit_LensName.setObjectName("lineEdit_LensName")
        self.horizontalLayout.addWidget(self.lineEdit_LensName)
        self.gridLayout_7.addWidget(self.frame_LensName, 1, 0, 1, 1)
        self.pushButton_SaveProfile = QtWidgets.QPushButton(self.frame_Buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SaveProfile.sizePolicy().hasHeightForWidth())
        self.pushButton_SaveProfile.setSizePolicy(sizePolicy)
        self.pushButton_SaveProfile.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButton_SaveProfile.setMaximumSize(QtCore.QSize(1000, 50))
        self.pushButton_SaveProfile.setObjectName("pushButton_SaveProfile")
        self.gridLayout_7.addWidget(self.pushButton_SaveProfile, 5, 0, 1, 1)
        self.pushButton_GenerateProfile = QtWidgets.QPushButton(self.frame_Buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GenerateProfile.sizePolicy().hasHeightForWidth())
        self.pushButton_GenerateProfile.setSizePolicy(sizePolicy)
        self.pushButton_GenerateProfile.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButton_GenerateProfile.setMaximumSize(QtCore.QSize(1000, 50))
        self.pushButton_GenerateProfile.setObjectName("pushButton_GenerateProfile")
        self.gridLayout_7.addWidget(self.pushButton_GenerateProfile, 2, 0, 1, 1)
        self.pushButton_LoadProfile = QtWidgets.QPushButton(self.frame_Buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_LoadProfile.sizePolicy().hasHeightForWidth())
        self.pushButton_LoadProfile.setSizePolicy(sizePolicy)
        self.pushButton_LoadProfile.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButton_LoadProfile.setMaximumSize(QtCore.QSize(1000, 50))
        self.pushButton_LoadProfile.setObjectName("pushButton_LoadProfile")
        self.gridLayout_7.addWidget(self.pushButton_LoadProfile, 3, 0, 1, 1)
        self.gridLayout_14.addWidget(self.frame_Buttons, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_Display, 0, 2, 2, 1)
        self.frame_Config = QtWidgets.QFrame(self.frame_Main)
        self.frame_Config.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_Config.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_Config.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Config.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Config.setObjectName("frame_Config")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_Config)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_General = QtWidgets.QFrame(self.frame_Config)
        self.frame_General.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_General.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_General.setObjectName("frame_General")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_General)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_General = QtWidgets.QLabel(self.frame_General)
        self.label_General.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_General.setAlignment(QtCore.Qt.AlignCenter)
        self.label_General.setObjectName("label_General")
        self.gridLayout_17.addWidget(self.label_General, 0, 0, 1, 6)
        self.label_ShiftX = QtWidgets.QLabel(self.frame_General)
        self.label_ShiftX.setObjectName("label_ShiftX")
        self.gridLayout_17.addWidget(self.label_ShiftX, 1, 0, 1, 1)
        self.doubleSpinBox_ShiftX = QtWidgets.QDoubleSpinBox(self.frame_General)
        self.doubleSpinBox_ShiftX.setMaximum(99999.0)
        self.doubleSpinBox_ShiftX.setObjectName("doubleSpinBox_ShiftX")
        self.gridLayout_17.addWidget(self.doubleSpinBox_ShiftX, 1, 1, 1, 2)
        self.label_Width = QtWidgets.QLabel(self.frame_General)
        self.label_Width.setObjectName("label_Width")
        self.gridLayout_17.addWidget(self.label_Width, 1, 3, 1, 2)
        self.doubleSpinBox_Width = QtWidgets.QDoubleSpinBox(self.frame_General)
        self.doubleSpinBox_Width.setMaximum(99999.0)
        self.doubleSpinBox_Width.setObjectName("doubleSpinBox_Width")
        self.gridLayout_17.addWidget(self.doubleSpinBox_Width, 1, 5, 1, 1)
        self.label_ShiftY = QtWidgets.QLabel(self.frame_General)
        self.label_ShiftY.setObjectName("label_ShiftY")
        self.gridLayout_17.addWidget(self.label_ShiftY, 2, 0, 1, 1)
        self.doubleSpinBox_ShiftY = QtWidgets.QDoubleSpinBox(self.frame_General)
        self.doubleSpinBox_ShiftY.setMaximum(99999.0)
        self.doubleSpinBox_ShiftY.setObjectName("doubleSpinBox_ShiftY")
        self.gridLayout_17.addWidget(self.doubleSpinBox_ShiftY, 2, 1, 1, 2)
        self.label_Height = QtWidgets.QLabel(self.frame_General)
        self.label_Height.setObjectName("label_Height")
        self.gridLayout_17.addWidget(self.label_Height, 2, 3, 1, 2)
        self.doubleSpinBox_Height = QtWidgets.QDoubleSpinBox(self.frame_General)
        self.doubleSpinBox_Height.setMaximum(99999.0)
        self.doubleSpinBox_Height.setObjectName("doubleSpinBox_Height")
        self.gridLayout_17.addWidget(self.doubleSpinBox_Height, 2, 5, 1, 1)
        self.label_NSlices = QtWidgets.QLabel(self.frame_General)
        self.label_NSlices.setObjectName("label_NSlices")
        self.gridLayout_17.addWidget(self.label_NSlices, 3, 0, 1, 1)
        self.spinBox_NSlices = QtWidgets.QSpinBox(self.frame_General)
        self.spinBox_NSlices.setMaximum(99999)
        self.spinBox_NSlices.setObjectName("spinBox_NSlices")
        self.gridLayout_17.addWidget(self.spinBox_NSlices, 3, 1, 1, 2)
        self.label_LensType = QtWidgets.QLabel(self.frame_General)
        self.label_LensType.setObjectName("label_LensType")
        self.gridLayout_17.addWidget(self.label_LensType, 3, 3, 1, 1)
        self.comboBox_LensType = QtWidgets.QComboBox(self.frame_General)
        self.comboBox_LensType.setObjectName("comboBox_LensType")
        self.comboBox_LensType.addItem("")
        self.comboBox_LensType.addItem("")
        self.gridLayout_17.addWidget(self.comboBox_LensType, 3, 4, 1, 2)
        self.verticalLayout_2.addWidget(self.frame_General)
        self.frame_BeamSpread = QtWidgets.QFrame(self.frame_Config)
        self.frame_BeamSpread.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_BeamSpread.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_BeamSpread.setObjectName("frame_BeamSpread")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_BeamSpread)
        self.gridLayout.setObjectName("gridLayout")
        self.label_BeamSpread = QtWidgets.QLabel(self.frame_BeamSpread)
        self.label_BeamSpread.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_BeamSpread.setAlignment(QtCore.Qt.AlignCenter)
        self.label_BeamSpread.setObjectName("label_BeamSpread")
        self.gridLayout.addWidget(self.label_BeamSpread, 0, 0, 1, 1)
        self.comboBox_BeamSpread = QtWidgets.QComboBox(self.frame_BeamSpread)
        self.comboBox_BeamSpread.setObjectName("comboBox_BeamSpread")
        self.comboBox_BeamSpread.addItem("")
        self.comboBox_BeamSpread.addItem("")
        self.comboBox_BeamSpread.addItem("")
        self.gridLayout.addWidget(self.comboBox_BeamSpread, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_BeamSpread)
        self.frame_BeamAngle = QtWidgets.QFrame(self.frame_Config)
        self.frame_BeamAngle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_BeamAngle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_BeamAngle.setObjectName("frame_BeamAngle")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_BeamAngle)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_BeamAngle = QtWidgets.QLabel(self.frame_BeamAngle)
        self.label_BeamAngle.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_BeamAngle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_BeamAngle.setObjectName("label_BeamAngle")
        self.gridLayout_15.addWidget(self.label_BeamAngle, 0, 0, 1, 2)
        self.comboBox_BeamAngle = QtWidgets.QComboBox(self.frame_BeamAngle)
        self.comboBox_BeamAngle.setObjectName("comboBox_BeamAngle")
        self.comboBox_BeamAngle.addItem("")
        self.comboBox_BeamAngle.addItem("")
        self.gridLayout_15.addWidget(self.comboBox_BeamAngle, 1, 0, 1, 1)
        self.doubleSpinBox_BeamAngle = QtWidgets.QDoubleSpinBox(self.frame_BeamAngle)
        self.doubleSpinBox_BeamAngle.setMinimum(0.01)
        self.doubleSpinBox_BeamAngle.setMaximum(89.99)
        self.doubleSpinBox_BeamAngle.setObjectName("doubleSpinBox_BeamAngle")
        self.gridLayout_15.addWidget(self.doubleSpinBox_BeamAngle, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_BeamAngle)
        self.frame_BeamShape = QtWidgets.QFrame(self.frame_Config)
        self.frame_BeamShape.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_BeamShape.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_BeamShape.setObjectName("frame_BeamShape")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_BeamShape)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_BeamShape = QtWidgets.QLabel(self.frame_BeamShape)
        self.label_BeamShape.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_BeamShape.setAlignment(QtCore.Qt.AlignCenter)
        self.label_BeamShape.setObjectName("label_BeamShape")
        self.gridLayout_5.addWidget(self.label_BeamShape, 0, 0, 1, 1)
        self.comboBox_BeamShape = QtWidgets.QComboBox(self.frame_BeamShape)
        self.comboBox_BeamShape.setObjectName("comboBox_BeamShape")
        self.comboBox_BeamShape.addItem("")
        self.comboBox_BeamShape.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_BeamShape, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_BeamShape)
        self.frame_Distance = QtWidgets.QFrame(self.frame_Config)
        self.frame_Distance.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Distance.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Distance.setObjectName("frame_Distance")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_Distance)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_Distance = QtWidgets.QLabel(self.frame_Distance)
        self.label_Distance.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_Distance.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Distance.setObjectName("label_Distance")
        self.gridLayout_8.addWidget(self.label_Distance, 0, 0, 1, 2)
        self.comboBox_DistanceMode = QtWidgets.QComboBox(self.frame_Distance)
        self.comboBox_DistanceMode.setObjectName("comboBox_DistanceMode")
        self.comboBox_DistanceMode.addItem("")
        self.comboBox_DistanceMode.addItem("")
        self.comboBox_DistanceMode.addItem("")
        self.gridLayout_8.addWidget(self.comboBox_DistanceMode, 1, 0, 1, 1)
        self.doubleSpinBox_Distance = QtWidgets.QDoubleSpinBox(self.frame_Distance)
        self.doubleSpinBox_Distance.setMaximum(99999.0)
        self.doubleSpinBox_Distance.setObjectName("doubleSpinBox_Distance")
        self.gridLayout_8.addWidget(self.doubleSpinBox_Distance, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_Distance)
        self.frame_BeamTilt = QtWidgets.QFrame(self.frame_Config)
        self.frame_BeamTilt.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_BeamTilt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_BeamTilt.setObjectName("frame_BeamTilt")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.frame_BeamTilt)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_BeamTilt = QtWidgets.QLabel(self.frame_BeamTilt)
        self.label_BeamTilt.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_BeamTilt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_BeamTilt.setObjectName("label_BeamTilt")
        self.gridLayout_18.addWidget(self.label_BeamTilt, 0, 0, 1, 2)
        self.label_BeamTiltX = QtWidgets.QLabel(self.frame_BeamTilt)
        self.label_BeamTiltX.setObjectName("label_BeamTiltX")
        self.gridLayout_18.addWidget(self.label_BeamTiltX, 1, 0, 1, 1)
        self.doubleSpinBox_BeamTiltX = QtWidgets.QDoubleSpinBox(self.frame_BeamTilt)
        self.doubleSpinBox_BeamTiltX.setObjectName("doubleSpinBox_BeamTiltX")
        self.gridLayout_18.addWidget(self.doubleSpinBox_BeamTiltX, 1, 1, 1, 1)
        self.label_BeamTiltY = QtWidgets.QLabel(self.frame_BeamTilt)
        self.label_BeamTiltY.setObjectName("label_BeamTiltY")
        self.gridLayout_18.addWidget(self.label_BeamTiltY, 2, 0, 1, 1)
        self.doubleSpinBox_BeamTiltY = QtWidgets.QDoubleSpinBox(self.frame_BeamTilt)
        self.doubleSpinBox_BeamTiltY.setObjectName("doubleSpinBox_BeamTiltY")
        self.gridLayout_18.addWidget(self.doubleSpinBox_BeamTiltY, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_BeamTilt)
        self.frame_BeamTilt_2 = QtWidgets.QFrame(self.frame_Config)
        self.frame_BeamTilt_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_BeamTilt_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_BeamTilt_2.setObjectName("frame_BeamTilt_2")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.frame_BeamTilt_2)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_SimParameters = QtWidgets.QLabel(self.frame_BeamTilt_2)
        self.label_SimParameters.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_SimParameters.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SimParameters.setObjectName("label_SimParameters")
        self.gridLayout_19.addWidget(self.label_SimParameters, 0, 0, 1, 2)
        self.doubleSpinBox_SimWidth = QtWidgets.QDoubleSpinBox(self.frame_BeamTilt_2)
        self.doubleSpinBox_SimWidth.setMaximum(99999.0)
        self.doubleSpinBox_SimWidth.setObjectName("doubleSpinBox_SimWidth")
        self.gridLayout_19.addWidget(self.doubleSpinBox_SimWidth, 2, 1, 1, 1)
        self.doubleSpinBox_PixelSize = QtWidgets.QDoubleSpinBox(self.frame_BeamTilt_2)
        self.doubleSpinBox_PixelSize.setMaximum(99999.0)
        self.doubleSpinBox_PixelSize.setObjectName("doubleSpinBox_PixelSize")
        self.gridLayout_19.addWidget(self.doubleSpinBox_PixelSize, 1, 1, 1, 1)
        self.label_PixelSize = QtWidgets.QLabel(self.frame_BeamTilt_2)
        self.label_PixelSize.setObjectName("label_PixelSize")
        self.gridLayout_19.addWidget(self.label_PixelSize, 1, 0, 1, 1)
        self.label_SimWidth = QtWidgets.QLabel(self.frame_BeamTilt_2)
        self.label_SimWidth.setObjectName("label_SimWidth")
        self.gridLayout_19.addWidget(self.label_SimWidth, 2, 0, 1, 1)
        self.doubleSpinBox_SimHeight = QtWidgets.QDoubleSpinBox(self.frame_BeamTilt_2)
        self.doubleSpinBox_SimHeight.setMaximum(99999.0)
        self.doubleSpinBox_SimHeight.setObjectName("doubleSpinBox_SimHeight")
        self.gridLayout_19.addWidget(self.doubleSpinBox_SimHeight, 3, 1, 1, 1)
        self.label_SimHeight = QtWidgets.QLabel(self.frame_BeamTilt_2)
        self.label_SimHeight.setObjectName("label_SimHeight")
        self.gridLayout_19.addWidget(self.label_SimHeight, 3, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_BeamTilt_2)
        self.frame = QtWidgets.QFrame(self.frame_Config)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_17.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_Units = QtWidgets.QLabel(self.frame)
        self.label_Units.setEnabled(True)
        self.label_Units.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_Units.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Units.setObjectName("label_Units")
        self.horizontalLayout_17.addWidget(self.label_Units)
        self.comboBox_Units = QtWidgets.QComboBox(self.frame)
        self.comboBox_Units.setMaximumSize(QtCore.QSize(40, 16777215))
        self.comboBox_Units.setEditable(False)
        self.comboBox_Units.setObjectName("comboBox_Units")
        self.comboBox_Units.addItem("")
        self.comboBox_Units.addItem("")
        self.comboBox_Units.addItem("")
        self.horizontalLayout_17.addWidget(self.comboBox_Units)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem2)
        self.checkBox_LiveUpdate = QtWidgets.QCheckBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_LiveUpdate.sizePolicy().hasHeightForWidth())
        self.checkBox_LiveUpdate.setSizePolicy(sizePolicy)
        self.checkBox_LiveUpdate.setMinimumSize(QtCore.QSize(0, 20))
        self.checkBox_LiveUpdate.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_LiveUpdate.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_LiveUpdate.setChecked(True)
        self.checkBox_LiveUpdate.setObjectName("checkBox_LiveUpdate")
        self.horizontalLayout_17.addWidget(self.checkBox_LiveUpdate)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_2.addWidget(self.frame_Config, 0, 0, 2, 1)
        self.verticalLayout.addWidget(self.frame_Main)
        BeamCreator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BeamCreator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1239, 21))
        self.menubar.setObjectName("menubar")
        BeamCreator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BeamCreator)
        self.statusbar.setObjectName("statusbar")
        BeamCreator.setStatusBar(self.statusbar)

        self.retranslateUi(BeamCreator)
        QtCore.QMetaObject.connectSlotsByName(BeamCreator)

    def retranslateUi(self, BeamCreator):
        _translate = QtCore.QCoreApplication.translate
        BeamCreator.setWindowTitle(_translate("BeamCreator", "MainWindow"))
        self.label_TitleMask.setText(_translate("BeamCreator", "Convergence/Divergence"))
        self.label_TitleProfile.setText(_translate("BeamCreator", "Beam Profile + Tilt"))
        self.label_LensName.setText(_translate("BeamCreator", "Beam Name:"))
        self.lineEdit_LensName.setText(_translate("BeamCreator", "Beam"))
        self.pushButton_SaveProfile.setText(_translate("BeamCreator", "Save Profile"))
        self.pushButton_GenerateProfile.setText(_translate("BeamCreator", "Generate Profile"))
        self.pushButton_LoadProfile.setText(_translate("BeamCreator", "Load Profile"))
        self.label_General.setText(_translate("BeamCreator", "General Parameters"))
        self.label_ShiftX.setText(_translate("BeamCreator", "Shift X"))
        self.label_Width.setText(_translate("BeamCreator", "Width"))
        self.label_ShiftY.setText(_translate("BeamCreator", "Shift Y"))
        self.label_Height.setText(_translate("BeamCreator", "Height"))
        self.label_NSlices.setText(_translate("BeamCreator", "N Slices"))
        self.label_LensType.setText(_translate("BeamCreator", "Lens Type"))
        self.comboBox_LensType.setItemText(0, _translate("BeamCreator", "Spherical"))
        self.comboBox_LensType.setItemText(1, _translate("BeamCreator", "Cylindrical"))
        self.label_BeamSpread.setText(_translate("BeamCreator", "Beam Spread"))
        self.comboBox_BeamSpread.setItemText(0, _translate("BeamCreator", "Planar"))
        self.comboBox_BeamSpread.setItemText(1, _translate("BeamCreator", "Converging"))
        self.comboBox_BeamSpread.setItemText(2, _translate("BeamCreator", "Diverging"))
        self.label_BeamAngle.setText(_translate("BeamCreator", "Convergence Angle"))
        self.comboBox_BeamAngle.setItemText(0, _translate("BeamCreator", "Theta"))
        self.comboBox_BeamAngle.setItemText(1, _translate("BeamCreator", "Numerical Aperture"))
        self.label_BeamShape.setText(_translate("BeamCreator", "Beam Shape"))
        self.comboBox_BeamShape.setItemText(0, _translate("BeamCreator", "Circular"))
        self.comboBox_BeamShape.setItemText(1, _translate("BeamCreator", "Rectangular"))
        self.label_Distance.setText(_translate("BeamCreator", "Distance Parameters"))
        self.comboBox_DistanceMode.setItemText(0, _translate("BeamCreator", "Absolute Distance"))
        self.comboBox_DistanceMode.setItemText(1, _translate("BeamCreator", "Final Beam Width"))
        self.comboBox_DistanceMode.setItemText(2, _translate("BeamCreator", "Focal Length Multiple"))
        self.label_BeamTilt.setText(_translate("BeamCreator", "Tilt Parameters"))
        self.label_BeamTiltX.setText(_translate("BeamCreator", "Theta X"))
        self.label_BeamTiltY.setText(_translate("BeamCreator", "Theta Y"))
        self.label_SimParameters.setText(_translate("BeamCreator", "Sim Parameters"))
        self.label_PixelSize.setText(_translate("BeamCreator", "Pixel Size"))
        self.label_SimWidth.setText(_translate("BeamCreator", "Sim Width"))
        self.label_SimHeight.setText(_translate("BeamCreator", "Sim Height"))
        self.label_Units.setText(_translate("BeamCreator", "Units:"))
        self.comboBox_Units.setCurrentText(_translate("BeamCreator", "nm"))
        self.comboBox_Units.setItemText(0, _translate("BeamCreator", "nm"))
        self.comboBox_Units.setItemText(1, _translate("BeamCreator", "um"))
        self.comboBox_Units.setItemText(2, _translate("BeamCreator", "mm"))
        self.checkBox_LiveUpdate.setText(_translate("BeamCreator", "Live Update"))
