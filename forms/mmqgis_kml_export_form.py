# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_kml_export_form.ui'
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

class Ui_mmqgis_kml_export_form(object):
    def setupUi(self, mmqgis_kml_export_form):
        mmqgis_kml_export_form.setObjectName(_fromUtf8("mmqgis_kml_export_form"))
        mmqgis_kml_export_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_kml_export_form.setEnabled(True)
        mmqgis_kml_export_form.resize(373, 361)
        mmqgis_kml_export_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_kml_export_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 330, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_kml_export_form)
        self.label.setGeometry(QtCore.QRect(10, 270, 108, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.outfilename = QtGui.QLineEdit(mmqgis_kml_export_form)
        self.outfilename.setGeometry(QtCore.QRect(10, 290, 261, 31))
        self.outfilename.setReadOnly(False)
        self.outfilename.setObjectName(_fromUtf8("outfilename"))
        self.browseoutfile = QtGui.QPushButton(mmqgis_kml_export_form)
        self.browseoutfile.setGeometry(QtCore.QRect(280, 290, 79, 26))
        self.browseoutfile.setObjectName(_fromUtf8("browseoutfile"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_kml_export_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_kml_export_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 108, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_2 = QtGui.QLabel(mmqgis_kml_export_form)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 151, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.namefield = QtGui.QComboBox(mmqgis_kml_export_form)
        self.namefield.setGeometry(QtCore.QRect(10, 80, 161, 31))
        self.namefield.setObjectName(_fromUtf8("namefield"))
        self.separator = QtGui.QComboBox(mmqgis_kml_export_form)
        self.separator.setGeometry(QtCore.QRect(200, 80, 161, 31))
        self.separator.setObjectName(_fromUtf8("separator"))
        self.label_3 = QtGui.QLabel(mmqgis_kml_export_form)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 108, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(mmqgis_kml_export_form)
        self.label_5.setGeometry(QtCore.QRect(200, 60, 151, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.description = QtGui.QTextEdit(mmqgis_kml_export_form)
        self.description.setGeometry(QtCore.QRect(10, 140, 351, 81))
        self.description.setObjectName(_fromUtf8("description"))
        self.exportdata = QtGui.QCheckBox(mmqgis_kml_export_form)
        self.exportdata.setGeometry(QtCore.QRect(10, 240, 351, 19))
        self.exportdata.setObjectName(_fromUtf8("exportdata"))

        self.retranslateUi(mmqgis_kml_export_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_kml_export_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_kml_export_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_kml_export_form)
        mmqgis_kml_export_form.setTabOrder(self.sourcelayer, self.namefield)
        mmqgis_kml_export_form.setTabOrder(self.namefield, self.separator)
        mmqgis_kml_export_form.setTabOrder(self.separator, self.outfilename)
        mmqgis_kml_export_form.setTabOrder(self.outfilename, self.browseoutfile)
        mmqgis_kml_export_form.setTabOrder(self.browseoutfile, self.buttonBox)

    def retranslateUi(self, mmqgis_kml_export_form):
        mmqgis_kml_export_form.setWindowTitle(_translate("mmqgis_kml_export_form", "Google Maps KML Export", None))
        self.label.setText(_translate("mmqgis_kml_export_form", "Output KML File", None))
        self.outfilename.setText(_translate("mmqgis_kml_export_form", "data.csv", None))
        self.browseoutfile.setText(_translate("mmqgis_kml_export_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_kml_export_form", "Source Layer", None))
        self.label_2.setText(_translate("mmqgis_kml_export_form", "Description HTML", None))
        self.label_3.setText(_translate("mmqgis_kml_export_form", "Name Field", None))
        self.label_5.setText(_translate("mmqgis_kml_export_form", "Description Separator", None))
        self.exportdata.setText(_translate("mmqgis_kml_export_form", "Export attributes as <Data> (importable by QGIS)", None))

