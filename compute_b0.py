# Form implementation generated from reading ui file 'compute_b0.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ComputeB0(object):
    def setupUi(self, ComputeB0):
        ComputeB0.setObjectName("ComputeB0")
        ComputeB0.resize(522, 361)
        ComputeB0.setStyleSheet("* {\n"
"    font-size: 16px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(ComputeB0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=ComputeB0)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_choose_bin = QtWidgets.QPushButton(parent=ComputeB0)
        self.pushButton_choose_bin.setObjectName("pushButton_choose_bin")
        self.horizontalLayout.addWidget(self.pushButton_choose_bin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lineEdit_bin_path = QtWidgets.QLineEdit(parent=ComputeB0)
        self.lineEdit_bin_path.setObjectName("lineEdit_bin_path")
        self.verticalLayout.addWidget(self.lineEdit_bin_path)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=ComputeB0)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_det = QtWidgets.QLineEdit(parent=ComputeB0)
        self.lineEdit_det.setObjectName("lineEdit_det")
        self.horizontalLayout_2.addWidget(self.lineEdit_det)
        self.label_4 = QtWidgets.QLabel(parent=ComputeB0)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_b0 = QtWidgets.QLineEdit(parent=ComputeB0)
        self.lineEdit_b0.setObjectName("lineEdit_b0")
        self.horizontalLayout_2.addWidget(self.lineEdit_b0)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=ComputeB0)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_temp_start = QtWidgets.QLineEdit(parent=ComputeB0)
        self.lineEdit_temp_start.setObjectName("lineEdit_temp_start")
        self.horizontalLayout_3.addWidget(self.lineEdit_temp_start)
        self.label_6 = QtWidgets.QLabel(parent=ComputeB0)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_temp_end = QtWidgets.QLineEdit(parent=ComputeB0)
        self.lineEdit_temp_end.setObjectName("lineEdit_temp_end")
        self.horizontalLayout_3.addWidget(self.lineEdit_temp_end)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=ComputeB0)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.pushButton_choose_output_dir = QtWidgets.QPushButton(parent=ComputeB0)
        self.pushButton_choose_output_dir.setObjectName("pushButton_choose_output_dir")
        self.horizontalLayout_4.addWidget(self.pushButton_choose_output_dir)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.lineEdit_output_dir = QtWidgets.QLineEdit(parent=ComputeB0)
        self.lineEdit_output_dir.setObjectName("lineEdit_output_dir")
        self.verticalLayout.addWidget(self.lineEdit_output_dir)
        self.pushButton_do_deal = QtWidgets.QPushButton(parent=ComputeB0)
        self.pushButton_do_deal.setObjectName("pushButton_do_deal")
        self.verticalLayout.addWidget(self.pushButton_do_deal)

        self.retranslateUi(ComputeB0)
        QtCore.QMetaObject.connectSlotsByName(ComputeB0)

    def retranslateUi(self, ComputeB0):
        _translate = QtCore.QCoreApplication.translate
        ComputeB0.setWindowTitle(_translate("ComputeB0", "B0_vs_Temp_fitting"))
        self.label.setText(_translate("ComputeB0", "请选择 Look up table:"))
        self.pushButton_choose_bin.setText(_translate("ComputeB0", "选择文件"))
        self.label_3.setText(_translate("ComputeB0", "Det 温度行:"))
        self.lineEdit_det.setText(_translate("ComputeB0", "0"))
        self.label_4.setText(_translate("ComputeB0", "B0 行:"))
        self.lineEdit_b0.setText(_translate("ComputeB0", "0"))
        self.label_5.setText(_translate("ComputeB0", "Temp 起始列:"))
        self.lineEdit_temp_start.setText(_translate("ComputeB0", "0"))
        self.label_6.setText(_translate("ComputeB0", "Temp 结束列:"))
        self.lineEdit_temp_end.setText(_translate("ComputeB0", "0"))
        self.label_2.setText(_translate("ComputeB0", "请选择图片存储位置:"))
        self.pushButton_choose_output_dir.setText(_translate("ComputeB0", "选择文件夹"))
        self.pushButton_do_deal.setText(_translate("ComputeB0", "执行处理"))
