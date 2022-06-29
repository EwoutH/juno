# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\LensSimulation.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 230)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_setup_sim = QtWidgets.QPushButton(self.frame)
        self.pushButton_setup_sim.setObjectName("pushButton_setup_sim")
        self.gridLayout_2.addWidget(self.pushButton_setup_sim, 3, 0, 1, 2)
        self.label_title = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.gridLayout_2.addWidget(self.label_title, 0, 0, 1, 1)
        self.pushButton_create_lens = QtWidgets.QPushButton(self.frame)
        self.pushButton_create_lens.setObjectName("pushButton_create_lens")
        self.gridLayout_2.addWidget(self.pushButton_create_lens, 1, 0, 1, 2)
        self.pushButton_create_beam = QtWidgets.QPushButton(self.frame)
        self.pushButton_create_beam.setObjectName("pushButton_create_beam")
        self.gridLayout_2.addWidget(self.pushButton_create_beam, 2, 0, 1, 2)
        self.pushButton_view_results = QtWidgets.QPushButton(self.frame)
        self.pushButton_view_results.setObjectName("pushButton_view_results")
        self.gridLayout_2.addWidget(self.pushButton_view_results, 5, 0, 1, 2)
        self.label_logo = QtWidgets.QLabel(self.frame)
        self.label_logo.setObjectName("label_logo")
        self.gridLayout_2.addWidget(self.label_logo, 0, 1, 1, 1)
        self.pushButton_run_simulation = QtWidgets.QPushButton(self.frame)
        self.pushButton_run_simulation.setObjectName("pushButton_run_simulation")
        self.gridLayout_2.addWidget(self.pushButton_run_simulation, 4, 0, 1, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_setup_sim.setText(_translate("MainWindow", "Setup Simulation"))
        self.label_title.setText(_translate("MainWindow", "Lens Simulation Package (TBD)"))
        self.pushButton_create_lens.setText(_translate("MainWindow", "Create Lens"))
        self.pushButton_create_beam.setText(_translate("MainWindow", "Create Beam"))
        self.pushButton_view_results.setText(_translate("MainWindow", "View Results"))
        self.label_logo.setText(_translate("MainWindow", "LOGO"))
        self.pushButton_run_simulation.setText(_translate("MainWindow", "Run Simulation"))
