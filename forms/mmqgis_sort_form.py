# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_sort_form.ui'
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

class Ui_mmqgis_sort_form(object):
    def setupUi(self, mmqgis_sort_form):
        mmqgis_sort_form.setObjectName(_fromUtf8("mmqgis_sort_form"))
        mmqgis_sort_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_sort_form.setEnabled(True)
        mmqgis_sort_form.resize(372, 261)
        mmqgis_sort_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_sort_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 230, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_sort_form)
        self.label.setGeometry(QtCore.QRect(10, 170, 261, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(mmqgis_sort_form)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 131, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.filename = QtGui.QLineEdit(mmqgis_sort_form)
        self.filename.setGeometry(QtCore.QRect(10, 190, 261, 21))
        self.filename.setReadOnly(False)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.browse = QtGui.QPushButton(mmqgis_sort_form)
        self.browse.setGeometry(QtCore.QRect(280, 190, 79, 26))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.sortattribute = QtGui.QComboBox(mmqgis_sort_form)
        self.sortattribute.setGeometry(QtCore.QRect(10, 80, 351, 27))
        self.sortattribute.setObjectName(_fromUtf8("sortattribute"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_sort_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_sort_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 121, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.direction = QtGui.QComboBox(mmqgis_sort_form)
        self.direction.setGeometry(QtCore.QRect(10, 130, 351, 27))
        self.direction.setObjectName(_fromUtf8("direction"))
        self.direction.addItem(_fromUtf8(""))
        self.direction.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(mmqgis_sort_form)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 131, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(mmqgis_sort_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_sort_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_sort_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_sort_form)
        mmqgis_sort_form.setTabOrder(self.sourcelayer, self.sortattribute)
        mmqgis_sort_form.setTabOrder(self.sortattribute, self.direction)
        mmqgis_sort_form.setTabOrder(self.direction, self.filename)
        mmqgis_sort_form.setTabOrder(self.filename, self.browse)
        mmqgis_sort_form.setTabOrder(self.browse, self.buttonBox)

    def retranslateUi(self, mmqgis_sort_form):
        mmqgis_sort_form.setWindowTitle(_translate("mmqgis_sort_form", "Sort Attributes", None))
        self.label.setText(_translate("mmqgis_sort_form", "Output Shapefile", None))
        self.label_3.setText(_translate("mmqgis_sort_form", "Sort Attribute", None))
        self.filename.setText(_translate("mmqgis_sort_form", "sorted.shp", None))
        self.browse.setText(_translate("mmqgis_sort_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_sort_form", "Source Layer", None))
        self.direction.setItemText(0, _translate("mmqgis_sort_form", "Ascending", None))
        self.direction.setItemText(1, _translate("mmqgis_sort_form", "Descending", None))
        self.label_5.setText(_translate("mmqgis_sort_form", "Direction", None))

