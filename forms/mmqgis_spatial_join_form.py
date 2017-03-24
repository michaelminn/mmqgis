# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_spatial_join_form.ui'
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

class Ui_mmqgis_spatial_join_form(object):
    def setupUi(self, mmqgis_spatial_join_form):
        mmqgis_spatial_join_form.setObjectName(_fromUtf8("mmqgis_spatial_join_form"))
        mmqgis_spatial_join_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_spatial_join_form.setEnabled(True)
        mmqgis_spatial_join_form.resize(440, 324)
        mmqgis_spatial_join_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_spatial_join_form)
        self.buttonBox.setGeometry(QtCore.QRect(150, 280, 160, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_spatial_join_form)
        self.label.setGeometry(QtCore.QRect(10, 220, 108, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.outfilename = QtGui.QLineEdit(mmqgis_spatial_join_form)
        self.outfilename.setGeometry(QtCore.QRect(10, 240, 321, 31))
        self.outfilename.setReadOnly(False)
        self.outfilename.setObjectName(_fromUtf8("outfilename"))
        self.browseoutfile = QtGui.QPushButton(mmqgis_spatial_join_form)
        self.browseoutfile.setGeometry(QtCore.QRect(350, 240, 79, 31))
        self.browseoutfile.setObjectName(_fromUtf8("browseoutfile"))
        self.targetlayer = QtGui.QComboBox(mmqgis_spatial_join_form)
        self.targetlayer.setGeometry(QtCore.QRect(10, 30, 241, 31))
        self.targetlayer.setObjectName(_fromUtf8("targetlayer"))
        self.label_4 = QtGui.QLabel(mmqgis_spatial_join_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 201, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.joinlayer = QtGui.QComboBox(mmqgis_spatial_join_form)
        self.joinlayer.setGeometry(QtCore.QRect(10, 130, 241, 31))
        self.joinlayer.setObjectName(_fromUtf8("joinlayer"))
        self.spatialop = QtGui.QComboBox(mmqgis_spatial_join_form)
        self.spatialop.setGeometry(QtCore.QRect(10, 80, 241, 31))
        self.spatialop.setObjectName(_fromUtf8("spatialop"))
        self.spatialop.addItem(_fromUtf8(""))
        self.spatialop.addItem(_fromUtf8(""))
        self.spatialop.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(mmqgis_spatial_join_form)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 108, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(mmqgis_spatial_join_form)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 108, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.fieldop = QtGui.QComboBox(mmqgis_spatial_join_form)
        self.fieldop.setGeometry(QtCore.QRect(10, 180, 241, 31))
        self.fieldop.setObjectName(_fromUtf8("fieldop"))
        self.label_6 = QtGui.QLabel(mmqgis_spatial_join_form)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 141, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.fieldnames = QtGui.QListWidget(mmqgis_spatial_join_form)
        self.fieldnames.setGeometry(QtCore.QRect(270, 80, 161, 131))
        self.fieldnames.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.fieldnames.setObjectName(_fromUtf8("fieldnames"))
        item = QtGui.QListWidgetItem()
        self.fieldnames.addItem(item)
        item = QtGui.QListWidgetItem()
        self.fieldnames.addItem(item)
        item = QtGui.QListWidgetItem()
        self.fieldnames.addItem(item)
        item = QtGui.QListWidgetItem()
        self.fieldnames.addItem(item)
        item = QtGui.QListWidgetItem()
        self.fieldnames.addItem(item)
        self.label_7 = QtGui.QLabel(mmqgis_spatial_join_form)
        self.label_7.setGeometry(QtCore.QRect(270, 60, 108, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(mmqgis_spatial_join_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_spatial_join_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_spatial_join_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_spatial_join_form)
        mmqgis_spatial_join_form.setTabOrder(self.targetlayer, self.spatialop)
        mmqgis_spatial_join_form.setTabOrder(self.spatialop, self.joinlayer)
        mmqgis_spatial_join_form.setTabOrder(self.joinlayer, self.fieldop)
        mmqgis_spatial_join_form.setTabOrder(self.fieldop, self.fieldnames)
        mmqgis_spatial_join_form.setTabOrder(self.fieldnames, self.outfilename)
        mmqgis_spatial_join_form.setTabOrder(self.outfilename, self.browseoutfile)
        mmqgis_spatial_join_form.setTabOrder(self.browseoutfile, self.buttonBox)

    def retranslateUi(self, mmqgis_spatial_join_form):
        mmqgis_spatial_join_form.setWindowTitle(_translate("mmqgis_spatial_join_form", "Spatial Join", None))
        self.label.setText(_translate("mmqgis_spatial_join_form", "Output File", None))
        self.outfilename.setText(_translate("mmqgis_spatial_join_form", "data.csv", None))
        self.browseoutfile.setText(_translate("mmqgis_spatial_join_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_spatial_join_form", "Output Shape (Target) Layer", None))
        self.spatialop.setItemText(0, _translate("mmqgis_spatial_join_form", "Intersects", None))
        self.spatialop.setItemText(1, _translate("mmqgis_spatial_join_form", "Within", None))
        self.spatialop.setItemText(2, _translate("mmqgis_spatial_join_form", "Contains", None))
        self.label_3.setText(_translate("mmqgis_spatial_join_form", "Data (Join) Layer", None))
        self.label_5.setText(_translate("mmqgis_spatial_join_form", "Spatial Operation", None))
        self.label_6.setText(_translate("mmqgis_spatial_join_form", "Attribute Operation", None))
        __sortingEnabled = self.fieldnames.isSortingEnabled()
        self.fieldnames.setSortingEnabled(False)
        item = self.fieldnames.item(0)
        item.setText(_translate("mmqgis_spatial_join_form", "Alpha", None))
        item = self.fieldnames.item(1)
        item.setText(_translate("mmqgis_spatial_join_form", "Beta", None))
        item = self.fieldnames.item(2)
        item.setText(_translate("mmqgis_spatial_join_form", "Gamma", None))
        item = self.fieldnames.item(3)
        item.setText(_translate("mmqgis_spatial_join_form", "Delta", None))
        item = self.fieldnames.item(4)
        item.setText(_translate("mmqgis_spatial_join_form", "Epsilon", None))
        self.fieldnames.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("mmqgis_spatial_join_form", "Fields", None))

