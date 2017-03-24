# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_geometry_import_form.ui'
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

class Ui_mmqgis_geometry_import_form(object):
    def setupUi(self, mmqgis_geometry_import_form):
        mmqgis_geometry_import_form.setObjectName(_fromUtf8("mmqgis_geometry_import_form"))
        mmqgis_geometry_import_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_geometry_import_form.setEnabled(True)
        mmqgis_geometry_import_form.resize(386, 277)
        mmqgis_geometry_import_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_geometry_import_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 240, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_geometry_import_form)
        self.label.setGeometry(QtCore.QRect(10, 180, 261, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.outfilename = QtGui.QLineEdit(mmqgis_geometry_import_form)
        self.outfilename.setGeometry(QtCore.QRect(10, 200, 261, 21))
        self.outfilename.setReadOnly(False)
        self.outfilename.setObjectName(_fromUtf8("outfilename"))
        self.outfilebrowse = QtGui.QPushButton(mmqgis_geometry_import_form)
        self.outfilebrowse.setGeometry(QtCore.QRect(280, 200, 79, 26))
        self.outfilebrowse.setObjectName(_fromUtf8("outfilebrowse"))
        self.label_2 = QtGui.QLabel(mmqgis_geometry_import_form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 261, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.nodebrowse = QtGui.QPushButton(mmqgis_geometry_import_form)
        self.nodebrowse.setGeometry(QtCore.QRect(280, 30, 79, 26))
        self.nodebrowse.setObjectName(_fromUtf8("nodebrowse"))
        self.nodefilename = QtGui.QLineEdit(mmqgis_geometry_import_form)
        self.nodefilename.setGeometry(QtCore.QRect(10, 30, 261, 21))
        self.nodefilename.setText(_fromUtf8(""))
        self.nodefilename.setReadOnly(False)
        self.nodefilename.setObjectName(_fromUtf8("nodefilename"))
        self.shapeidcol = QtGui.QComboBox(mmqgis_geometry_import_form)
        self.shapeidcol.setGeometry(QtCore.QRect(10, 140, 171, 27))
        self.shapeidcol.setObjectName(_fromUtf8("shapeidcol"))
        self.label_6 = QtGui.QLabel(mmqgis_geometry_import_form)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 117, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.longcol = QtGui.QComboBox(mmqgis_geometry_import_form)
        self.longcol.setGeometry(QtCore.QRect(10, 80, 171, 27))
        self.longcol.setObjectName(_fromUtf8("longcol"))
        self.label_7 = QtGui.QLabel(mmqgis_geometry_import_form)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 117, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(mmqgis_geometry_import_form)
        self.label_8.setGeometry(QtCore.QRect(200, 60, 117, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.latcol = QtGui.QComboBox(mmqgis_geometry_import_form)
        self.latcol.setGeometry(QtCore.QRect(200, 80, 171, 27))
        self.latcol.setObjectName(_fromUtf8("latcol"))
        self.label_9 = QtGui.QLabel(mmqgis_geometry_import_form)
        self.label_9.setGeometry(QtCore.QRect(200, 120, 117, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.geometrytype = QtGui.QComboBox(mmqgis_geometry_import_form)
        self.geometrytype.setGeometry(QtCore.QRect(200, 140, 171, 27))
        self.geometrytype.setObjectName(_fromUtf8("geometrytype"))

        self.retranslateUi(mmqgis_geometry_import_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_geometry_import_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_geometry_import_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_geometry_import_form)
        mmqgis_geometry_import_form.setTabOrder(self.nodefilename, self.nodebrowse)
        mmqgis_geometry_import_form.setTabOrder(self.nodebrowse, self.longcol)
        mmqgis_geometry_import_form.setTabOrder(self.longcol, self.latcol)
        mmqgis_geometry_import_form.setTabOrder(self.latcol, self.shapeidcol)
        mmqgis_geometry_import_form.setTabOrder(self.shapeidcol, self.geometrytype)
        mmqgis_geometry_import_form.setTabOrder(self.geometrytype, self.outfilename)
        mmqgis_geometry_import_form.setTabOrder(self.outfilename, self.outfilebrowse)
        mmqgis_geometry_import_form.setTabOrder(self.outfilebrowse, self.buttonBox)

    def retranslateUi(self, mmqgis_geometry_import_form):
        mmqgis_geometry_import_form.setWindowTitle(_translate("mmqgis_geometry_import_form", "Geometry Import from CSV File", None))
        self.label.setText(_translate("mmqgis_geometry_import_form", "Output Shapefile", None))
        self.outfilename.setText(_translate("mmqgis_geometry_import_form", "geometry.shp", None))
        self.outfilebrowse.setText(_translate("mmqgis_geometry_import_form", "Browse...", None))
        self.label_2.setText(_translate("mmqgis_geometry_import_form", "Input CSV Nodes File", None))
        self.nodebrowse.setText(_translate("mmqgis_geometry_import_form", "Browse...", None))
        self.label_6.setText(_translate("mmqgis_geometry_import_form", "Shape ID Column", None))
        self.label_7.setText(_translate("mmqgis_geometry_import_form", "Longitude Column", None))
        self.label_8.setText(_translate("mmqgis_geometry_import_form", "Latitude Column", None))
        self.label_9.setText(_translate("mmqgis_geometry_import_form", "Geometry Type", None))

