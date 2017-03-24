# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_voronoi_form.ui'
#
# Created: Tue Dec 27 15:33:20 2016
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

class Ui_mmqgis_voronoi_form(object):
    def setupUi(self, mmqgis_voronoi_form):
        mmqgis_voronoi_form.setObjectName(_fromUtf8("mmqgis_voronoi_form"))
        mmqgis_voronoi_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_voronoi_form.setEnabled(True)
        mmqgis_voronoi_form.resize(368, 179)
        mmqgis_voronoi_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_voronoi_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 140, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_voronoi_form)
        self.label.setGeometry(QtCore.QRect(10, 70, 151, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.filename = QtGui.QLineEdit(mmqgis_voronoi_form)
        self.filename.setGeometry(QtCore.QRect(10, 90, 261, 28))
        self.filename.setReadOnly(False)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.browse = QtGui.QPushButton(mmqgis_voronoi_form)
        self.browse.setGeometry(QtCore.QRect(280, 90, 79, 26))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_voronoi_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_voronoi_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 131, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(mmqgis_voronoi_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_voronoi_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_voronoi_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_voronoi_form)
        mmqgis_voronoi_form.setTabOrder(self.sourcelayer, self.filename)
        mmqgis_voronoi_form.setTabOrder(self.filename, self.browse)
        mmqgis_voronoi_form.setTabOrder(self.browse, self.buttonBox)

    def retranslateUi(self, mmqgis_voronoi_form):
        mmqgis_voronoi_form.setWindowTitle(_translate("mmqgis_voronoi_form", "Voronoi Diagram", None))
        self.label.setText(_translate("mmqgis_voronoi_form", "Output Shapefile", None))
        self.filename.setText(_translate("mmqgis_voronoi_form", "voronoi.shp", None))
        self.browse.setText(_translate("mmqgis_voronoi_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_voronoi_form", "Source Layer", None))

