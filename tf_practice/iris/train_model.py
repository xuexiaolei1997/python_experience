# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'train_model.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(319, 144)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons8-linux-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_model_type = QtWidgets.QLabel(Dialog)
        self.label_model_type.setObjectName("label_model_type")
        self.horizontalLayout_2.addWidget(self.label_model_type)
        self.comboBox_model_type = QtWidgets.QComboBox(Dialog)
        self.comboBox_model_type.setObjectName("comboBox_model_type")
        self.horizontalLayout_2.addWidget(self.comboBox_model_type)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_param = QtWidgets.QLabel(Dialog)
        self.label_param.setAlignment(QtCore.Qt.AlignCenter)
        self.label_param.setObjectName("label_param")
        self.gridLayout.addWidget(self.label_param, 1, 0, 1, 1)
        self.lineEdit_param = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_param.setObjectName("lineEdit_param")
        self.gridLayout.addWidget(self.lineEdit_param, 1, 1, 1, 1)
        self.lineEdit_data = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_data.setObjectName("lineEdit_data")
        self.gridLayout.addWidget(self.lineEdit_data, 0, 1, 1, 1)
        self.toolButton_choosedata = QtWidgets.QToolButton(Dialog)
        self.toolButton_choosedata.setObjectName("toolButton_choosedata")
        self.gridLayout.addWidget(self.toolButton_choosedata, 0, 2, 1, 1)
        self.label_data = QtWidgets.QLabel(Dialog)
        self.label_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data.setObjectName("label_data")
        self.gridLayout.addWidget(self.label_data, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_predict = QtWidgets.QPushButton(Dialog)
        self.pushButton_predict.setObjectName("pushButton_predict")
        self.horizontalLayout.addWidget(self.pushButton_predict)
        self.pushButton_save_model = QtWidgets.QPushButton(Dialog)
        self.pushButton_save_model.setObjectName("pushButton_save_model")
        self.horizontalLayout.addWidget(self.pushButton_save_model)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog_train_model"))
        self.label_model_type.setText(_translate("Dialog", "Model Type:"))
        self.label_param.setText(_translate("Dialog", "Param"))
        self.toolButton_choosedata.setText(_translate("Dialog", "..."))
        self.label_data.setText(_translate("Dialog", "Data:"))
        self.pushButton_predict.setText(_translate("Dialog", "Train"))
        self.pushButton_save_model.setText(_translate("Dialog", "Save Model"))

