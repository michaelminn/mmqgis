# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_delete_columns_form.ui'
#
# Created: Tue Dec 27 15:33:18 2016
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

class Ui_mmqgis_delete_columns_form(object):
    def setupUi(self, mmqgis_delete_columns_form):
        mmqgis_delete_columns_form.setObjectName(_fromUtf8("mmqgis_delete_columns_form"))
        mmqgis_delete_columns_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_delete_columns_form.setEnabled(True)
        mmqgis_delete_columns_form.resize(372, 349)
        mmqgis_delete_columns_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_delete_columns_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 310, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_delete_columns_form)
        self.label.setGeometry(QtCore.QRect(10, 250, 261, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.filename = QtGui.QLineEdit(mmqgis_delete_columns_form)
        self.filename.setGeometry(QtCore.QRect(10, 270, 261, 21))
        self.filename.setReadOnly(False)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.browse = QtGui.QPushButton(mmqgis_delete_columns_form)
        self.browse.setGeometry(QtCore.QRect(280, 270, 79, 26))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_delete_columns_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_delete_columns_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 121, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.fieldnames = QtGui.QListWidget(mmqgis_delete_columns_form)
        self.fieldnames.setGeometry(QtCore.QRect(10, 90, 351, 151))
        self.fieldnames.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.fieldnames.setObjectName(_fromUtf8("fieldnames"))
        self.label_5 = QtGui.QLabel(mmqgis_delete_columns_form)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 121, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(mmqgis_delete_columns_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_delete_columns_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_delete_columns_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_delete_columns_form)
        mmqgis_delete_columns_form.setTabOrder(self.sourcelayer, self.fieldnames)
        mmqgis_delete_columns_form.setTabOrder(self.fieldnames, self.filename)
        mmqgis_delete_columns_form.setTabOrder(self.filename, self.browse)
        mmqgis_delete_columns_form.setTabOrder(self.browse, self.buttonBox)

    def retranslateUi(self, mmqgis_delete_columns_form):
        mmqgis_delete_columns_form.setWindowTitle(_translate("mmqgis_delete_columns_form", "Delete Columns", None))
        self.label.setText(_translate("mmqgis_delete_columns_form", "Output Shapefile", None))
        self.filename.setText(_translate("mmqgis_delete_columns_form", "temp.shp", None))
        self.browse.setText(_translate("mmqgis_delete_columns_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_delete_columns_form", "Source Layer", None))
        self.label_5.setText(_translate("mmqgis_delete_columns_form", "Fields to Delete", None))

