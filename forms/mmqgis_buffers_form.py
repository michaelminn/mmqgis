# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_buffers_form.ui'
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

class Ui_mmqgis_buffers_form(object):
    def setupUi(self, mmqgis_buffers_form):
        mmqgis_buffers_form.setObjectName(_fromUtf8("mmqgis_buffers_form"))
        mmqgis_buffers_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_buffers_form.setEnabled(True)
        mmqgis_buffers_form.resize(432, 377)
        mmqgis_buffers_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_buffers_form)
        self.buttonBox.setGeometry(QtCore.QRect(140, 340, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_buffers_form)
        self.label.setGeometry(QtCore.QRect(10, 280, 261, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.filename = QtGui.QLineEdit(mmqgis_buffers_form)
        self.filename.setGeometry(QtCore.QRect(10, 300, 321, 31))
        self.filename.setReadOnly(False)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.browse = QtGui.QPushButton(mmqgis_buffers_form)
        self.browse.setGeometry(QtCore.QRect(340, 300, 79, 26))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_buffers_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 411, 31))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 121, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.edgeattribute = QtGui.QComboBox(mmqgis_buffers_form)
        self.edgeattribute.setGeometry(QtCore.QRect(10, 180, 181, 31))
        self.edgeattribute.setObjectName(_fromUtf8("edgeattribute"))
        self.label_6 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 121, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.radius = QtGui.QLineEdit(mmqgis_buffers_form)
        self.radius.setGeometry(QtCore.QRect(210, 120, 81, 31))
        self.radius.setObjectName(_fromUtf8("radius"))
        self.label_8 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_8.setGeometry(QtCore.QRect(210, 100, 91, 22))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.radiusunit = QtGui.QComboBox(mmqgis_buffers_form)
        self.radiusunit.setGeometry(QtCore.QRect(310, 120, 111, 31))
        self.radiusunit.setObjectName(_fromUtf8("radiusunit"))
        self.label_9 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_9.setGeometry(QtCore.QRect(310, 100, 81, 22))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_7 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 121, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.radiusattribute = QtGui.QComboBox(mmqgis_buffers_form)
        self.radiusattribute.setGeometry(QtCore.QRect(10, 120, 181, 31))
        self.radiusattribute.setObjectName(_fromUtf8("radiusattribute"))
        self.selectedonly = QtGui.QCheckBox(mmqgis_buffers_form)
        self.selectedonly.setGeometry(QtCore.QRect(20, 70, 181, 20))
        self.selectedonly.setObjectName(_fromUtf8("selectedonly"))
        self.edgecount = QtGui.QComboBox(mmqgis_buffers_form)
        self.edgecount.setGeometry(QtCore.QRect(210, 180, 211, 31))
        self.edgecount.setObjectName(_fromUtf8("edgecount"))
        self.label_10 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_10.setGeometry(QtCore.QRect(210, 160, 161, 22))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_11.setGeometry(QtCore.QRect(10, 220, 121, 22))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.rotationattribute = QtGui.QComboBox(mmqgis_buffers_form)
        self.rotationattribute.setGeometry(QtCore.QRect(10, 240, 181, 31))
        self.rotationattribute.setObjectName(_fromUtf8("rotationattribute"))
        self.rotation = QtGui.QLineEdit(mmqgis_buffers_form)
        self.rotation.setGeometry(QtCore.QRect(210, 240, 211, 31))
        self.rotation.setObjectName(_fromUtf8("rotation"))
        self.label_12 = QtGui.QLabel(mmqgis_buffers_form)
        self.label_12.setGeometry(QtCore.QRect(210, 220, 181, 22))
        self.label_12.setObjectName(_fromUtf8("label_12"))

        self.retranslateUi(mmqgis_buffers_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_buffers_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_buffers_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_buffers_form)
        mmqgis_buffers_form.setTabOrder(self.sourcelayer, self.radiusunit)
        mmqgis_buffers_form.setTabOrder(self.radiusunit, self.edgeattribute)
        mmqgis_buffers_form.setTabOrder(self.edgeattribute, self.radius)
        mmqgis_buffers_form.setTabOrder(self.radius, self.radiusattribute)
        mmqgis_buffers_form.setTabOrder(self.radiusattribute, self.selectedonly)
        mmqgis_buffers_form.setTabOrder(self.selectedonly, self.filename)
        mmqgis_buffers_form.setTabOrder(self.filename, self.browse)
        mmqgis_buffers_form.setTabOrder(self.browse, self.buttonBox)

    def retranslateUi(self, mmqgis_buffers_form):
        mmqgis_buffers_form.setWindowTitle(_translate("mmqgis_buffers_form", "Create Buffers", None))
        self.label.setText(_translate("mmqgis_buffers_form", "Output Shapefile", None))
        self.filename.setText(_translate("mmqgis_buffers_form", "temp.shp", None))
        self.browse.setText(_translate("mmqgis_buffers_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_buffers_form", "Source Layer", None))
        self.label_6.setText(_translate("mmqgis_buffers_form", "Edges Attribute", None))
        self.label_8.setText(_translate("mmqgis_buffers_form", "Fixed Radius", None))
        self.label_9.setText(_translate("mmqgis_buffers_form", "Radius Unit", None))
        self.label_7.setText(_translate("mmqgis_buffers_form", "Radius Attribute", None))
        self.selectedonly.setText(_translate("mmqgis_buffers_form", "Selected Features Only", None))
        self.label_10.setText(_translate("mmqgis_buffers_form", "Fixed Number of Edges", None))
        self.label_11.setText(_translate("mmqgis_buffers_form", "Rotation Attribute", None))
        self.label_12.setText(_translate("mmqgis_buffers_form", "Fixed Rotation (Degrees)", None))

