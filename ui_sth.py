# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sth.ui'
#
# Created: Thu Sep 10 13:37:36 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_STH(object):
    def setupUi(self, STH):
        STH.setObjectName(_fromUtf8("STH"))
        STH.resize(406, 247)
        self.verticalLayout = QtGui.QVBoxLayout(STH)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelInput = QtGui.QLabel(STH)
        self.labelInput.setObjectName(_fromUtf8("labelInput"))
        self.horizontalLayout_2.addWidget(self.labelInput)
        self.lineEditInput = QtGui.QLineEdit(STH)
        self.lineEditInput.setObjectName(_fromUtf8("lineEditInput"))
        self.horizontalLayout_2.addWidget(self.lineEditInput)
        self.pushButton_2 = QtGui.QPushButton(STH)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(STH)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEditOutput = QtGui.QLineEdit(STH)
        self.lineEditOutput.setText(_fromUtf8(""))
        self.lineEditOutput.setObjectName(_fromUtf8("lineEditOutput"))
        self.horizontalLayout.addWidget(self.lineEditOutput)
        self.pushButton_3 = QtGui.QPushButton(STH)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.labelControlProgram = QtGui.QLabel(STH)
        self.labelControlProgram.setObjectName(_fromUtf8("labelControlProgram"))
        self.horizontalLayout_5.addWidget(self.labelControlProgram)
        self.comboBoxProgram = QtGui.QComboBox(STH)
        self.comboBoxProgram.setObjectName(_fromUtf8("comboBoxProgram"))
        self.horizontalLayout_5.addWidget(self.comboBoxProgram)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButtonAdjustControlProgram = QtGui.QPushButton(STH)
        self.pushButtonAdjustControlProgram.setObjectName(_fromUtf8("pushButtonAdjustControlProgram"))
        self.horizontalLayout_4.addWidget(self.pushButtonAdjustControlProgram)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelTimeStep = QtGui.QLabel(STH)
        self.labelTimeStep.setObjectName(_fromUtf8("labelTimeStep"))
        self.horizontalLayout_3.addWidget(self.labelTimeStep)
        self.spinBox = QtGui.QSpinBox(STH)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_3.addWidget(self.spinBox)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtGui.QDialogButtonBox(STH)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(STH)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), STH.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), STH.reject)
        QtCore.QMetaObject.connectSlotsByName(STH)

    def retranslateUi(self, STH):
        STH.setWindowTitle(_translate("STH", "STH", None))
        self.labelInput.setText(_translate("STH", "Input-File:", None))
        self.pushButton_2.setText(_translate("STH", "Select", None))
        self.label_3.setText(_translate("STH", "Output-File:", None))
        self.pushButton_3.setText(_translate("STH", "Select", None))
        self.labelControlProgram.setText(_translate("STH", "Control Program:", None))
        self.pushButtonAdjustControlProgram.setText(_translate("STH", "Adjust Control Program", None))
        self.labelTimeStep.setText(_translate("STH", "Time Step (years):", None))

