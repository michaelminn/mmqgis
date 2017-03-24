# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_hub_distance_form.ui'
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

class Ui_mmqgis_hub_distance_form(object):
    def setupUi(self, mmqgis_hub_distance_form):
        mmqgis_hub_distance_form.setObjectName(_fromUtf8("mmqgis_hub_distance_form"))
        mmqgis_hub_distance_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_hub_distance_form.setEnabled(True)
        mmqgis_hub_distance_form.resize(373, 343)
        mmqgis_hub_distance_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_hub_distance_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 310, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_hub_distance_form)
        self.label.setGeometry(QtCore.QRect(10, 250, 261, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(mmqgis_hub_distance_form)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 171, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.filename = QtGui.QLineEdit(mmqgis_hub_distance_form)
        self.filename.setGeometry(QtCore.QRect(10, 270, 261, 21))
        self.filename.setReadOnly(False)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.browse = QtGui.QPushButton(mmqgis_hub_distance_form)
        self.browse.setGeometry(QtCore.QRect(280, 270, 79, 26))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.hubslayerbox = QtGui.QComboBox(mmqgis_hub_distance_form)
        self.hubslayerbox.setGeometry(QtCore.QRect(10, 80, 351, 27))
        self.hubslayerbox.setObjectName(_fromUtf8("hubslayerbox"))
        self.sourcelayerbox = QtGui.QComboBox(mmqgis_hub_distance_form)
        self.sourcelayerbox.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.sourcelayerbox.setObjectName(_fromUtf8("sourcelayerbox"))
        self.label_4 = QtGui.QLabel(mmqgis_hub_distance_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 161, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.nameattributebox = QtGui.QComboBox(mmqgis_hub_distance_form)
        self.nameattributebox.setGeometry(QtCore.QRect(10, 130, 351, 27))
        self.nameattributebox.setObjectName(_fromUtf8("nameattributebox"))
        self.label_5 = QtGui.QLabel(mmqgis_hub_distance_form)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 171, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.outputtype = QtGui.QComboBox(mmqgis_hub_distance_form)
        self.outputtype.setGeometry(QtCore.QRect(10, 180, 161, 27))
        self.outputtype.setObjectName(_fromUtf8("outputtype"))
        self.label_6 = QtGui.QLabel(mmqgis_hub_distance_form)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 171, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.measurement = QtGui.QComboBox(mmqgis_hub_distance_form)
        self.measurement.setGeometry(QtCore.QRect(200, 180, 161, 27))
        self.measurement.setObjectName(_fromUtf8("measurement"))
        self.label_7 = QtGui.QLabel(mmqgis_hub_distance_form)
        self.label_7.setGeometry(QtCore.QRect(200, 160, 161, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.distribute = QtGui.QCheckBox(mmqgis_hub_distance_form)
        self.distribute.setGeometry(QtCore.QRect(10, 220, 261, 19))
        self.distribute.setObjectName(_fromUtf8("distribute"))

        self.retranslateUi(mmqgis_hub_distance_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_hub_distance_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_hub_distance_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_hub_distance_form)
        mmqgis_hub_distance_form.setTabOrder(self.sourcelayerbox, self.hubslayerbox)
        mmqgis_hub_distance_form.setTabOrder(self.hubslayerbox, self.nameattributebox)
        mmqgis_hub_distance_form.setTabOrder(self.nameattributebox, self.outputtype)
        mmqgis_hub_distance_form.setTabOrder(self.outputtype, self.measurement)
        mmqgis_hub_distance_form.setTabOrder(self.measurement, self.distribute)
        mmqgis_hub_distance_form.setTabOrder(self.distribute, self.filename)
        mmqgis_hub_distance_form.setTabOrder(self.filename, self.browse)
        mmqgis_hub_distance_form.setTabOrder(self.browse, self.buttonBox)

    def retranslateUi(self, mmqgis_hub_distance_form):
        mmqgis_hub_distance_form.setWindowTitle(_translate("mmqgis_hub_distance_form", "Distance to Nearest Hub", None))
        self.label.setText(_translate("mmqgis_hub_distance_form", "Output Shapefile", None))
        self.label_3.setText(_translate("mmqgis_hub_distance_form", "Destination Hubs Layer", None))
        self.filename.setText(_translate("mmqgis_hub_distance_form", "distances.shp", None))
        self.browse.setText(_translate("mmqgis_hub_distance_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_hub_distance_form", "Source Points Layer", None))
        self.label_5.setText(_translate("mmqgis_hub_distance_form", "Hub Layer Name Attribute", None))
        self.label_6.setText(_translate("mmqgis_hub_distance_form", "Output Shape Type", None))
        self.label_7.setText(_translate("mmqgis_hub_distance_form", "Measurement Unit", None))
        self.distribute.setText(_translate("mmqgis_hub_distance_form", "Equally Distribute Points Across Hubs", None))

