# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_gridify_form.ui'
#
# Created: Tue Dec 27 15:33:19 2016
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_mmqgis_gridify_form(object):
    def setupUi(self, mmqgis_gridify_form):
        mmqgis_gridify_form.setObjectName(_fromUtf8("mmqgis_gridify_form"))
        mmqgis_gridify_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_gridify_form.setEnabled(True)
        mmqgis_gridify_form.resize(368, 240)
        mmqgis_gridify_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_gridify_form)
        self.buttonBox.setGeometry(QtCore.QRect(100, 200, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_gridify_form)
        self.label.setGeometry(QtCore.QRect(10, 130, 108, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(mmqgis_gridify_form)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 67, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(mmqgis_gridify_form)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 68, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.filename = QtGui.QLineEdit(mmqgis_gridify_form)
        self.filename.setGeometry(QtCore.QRect(10, 150, 261, 28))
        self.filename.setReadOnly(False)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.browse = QtGui.QPushButton(mmqgis_gridify_form)
        self.browse.setGeometry(QtCore.QRect(280, 150, 79, 26))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.vspacing = QtGui.QLineEdit(mmqgis_gridify_form)
        self.vspacing.setGeometry(QtCore.QRect(190, 90, 171, 28))
        self.vspacing.setObjectName(_fromUtf8("vspacing"))
        self.hspacing = QtGui.QLineEdit(mmqgis_gridify_form)
        self.hspacing.setGeometry(QtCore.QRect(10, 90, 151, 28))
        self.hspacing.setObjectName(_fromUtf8("hspacing"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_gridify_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_gridify_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 108, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(mmqgis_gridify_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_gridify_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_gridify_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_gridify_form)
        mmqgis_gridify_form.setTabOrder(self.sourcelayer, self.hspacing)
        mmqgis_gridify_form.setTabOrder(self.hspacing, self.vspacing)
        mmqgis_gridify_form.setTabOrder(self.vspacing, self.filename)
        mmqgis_gridify_form.setTabOrder(self.filename, self.browse)
        mmqgis_gridify_form.setTabOrder(self.browse, self.buttonBox)

    def retranslateUi(self, mmqgis_gridify_form):
        mmqgis_gridify_form.setWindowTitle(_translate("mmqgis_gridify_form", "Gridify", None))
        self.label.setText(_translate("mmqgis_gridify_form", "Output Shapefile", None))
        self.label_2.setText(_translate("mmqgis_gridify_form", "V Spacing", None))
        self.label_3.setText(_translate("mmqgis_gridify_form", "H Spacing", None))
        self.filename.setText(_translate("mmqgis_gridify_form", "grid.shp", None))
        self.browse.setText(_translate("mmqgis_gridify_form", "Browse...", None))
        self.vspacing.setText(_translate("mmqgis_gridify_form", "10", None))
        self.hspacing.setText(_translate("mmqgis_gridify_form", "10", None))
        self.label_4.setText(_translate("mmqgis_gridify_form", "Source Layer", None))

