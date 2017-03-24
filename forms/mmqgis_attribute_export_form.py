# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_attribute_export_form.ui'
#
# Created: Tue Dec 27 15:33:17 2016
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

class Ui_mmqgis_attribute_export_form(object):
    def setupUi(self, mmqgis_attribute_export_form):
        mmqgis_attribute_export_form.setObjectName(_fromUtf8("mmqgis_attribute_export_form"))
        mmqgis_attribute_export_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_attribute_export_form.setEnabled(True)
        mmqgis_attribute_export_form.resize(372, 397)
        mmqgis_attribute_export_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_attribute_export_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 350, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_attribute_export_form)
        self.label.setGeometry(QtCore.QRect(10, 290, 108, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.outfilename = QtGui.QLineEdit(mmqgis_attribute_export_form)
        self.outfilename.setGeometry(QtCore.QRect(10, 310, 261, 21))
        self.outfilename.setReadOnly(False)
        self.outfilename.setObjectName(_fromUtf8("outfilename"))
        self.browseoutfile = QtGui.QPushButton(mmqgis_attribute_export_form)
        self.browseoutfile.setGeometry(QtCore.QRect(280, 310, 79, 26))
        self.browseoutfile.setObjectName(_fromUtf8("browseoutfile"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_attribute_export_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_attribute_export_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 108, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_2 = QtGui.QLabel(mmqgis_attribute_export_form)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 108, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.attributes = QtGui.QListWidget(mmqgis_attribute_export_form)
        self.attributes.setGeometry(QtCore.QRect(10, 80, 341, 151))
        self.attributes.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.attributes.setObjectName(_fromUtf8("attributes"))
        item = QtGui.QListWidgetItem()
        self.attributes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.attributes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.attributes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.attributes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.attributes.addItem(item)
        self.delimiter = QtGui.QComboBox(mmqgis_attribute_export_form)
        self.delimiter.setGeometry(QtCore.QRect(10, 260, 111, 22))
        self.delimiter.setObjectName(_fromUtf8("delimiter"))
        self.delimiter.addItem(_fromUtf8(""))
        self.delimiter.addItem(_fromUtf8(""))
        self.delimiter.addItem(_fromUtf8(""))
        self.delimiter.addItem(_fromUtf8(""))
        self.lineterminator = QtGui.QComboBox(mmqgis_attribute_export_form)
        self.lineterminator.setGeometry(QtCore.QRect(260, 260, 91, 22))
        self.lineterminator.setObjectName(_fromUtf8("lineterminator"))
        self.lineterminator.addItem(_fromUtf8(""))
        self.lineterminator.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(mmqgis_attribute_export_form)
        self.label_3.setGeometry(QtCore.QRect(10, 240, 81, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(mmqgis_attribute_export_form)
        self.label_5.setGeometry(QtCore.QRect(260, 240, 108, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.decimalmark = QtGui.QComboBox(mmqgis_attribute_export_form)
        self.decimalmark.setGeometry(QtCore.QRect(130, 260, 111, 22))
        self.decimalmark.setObjectName(_fromUtf8("decimalmark"))
        self.decimalmark.addItem(_fromUtf8(""))
        self.decimalmark.addItem(_fromUtf8(""))
        self.label_6 = QtGui.QLabel(mmqgis_attribute_export_form)
        self.label_6.setGeometry(QtCore.QRect(130, 240, 91, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(mmqgis_attribute_export_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_attribute_export_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_attribute_export_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_attribute_export_form)
        mmqgis_attribute_export_form.setTabOrder(self.sourcelayer, self.attributes)
        mmqgis_attribute_export_form.setTabOrder(self.attributes, self.delimiter)
        mmqgis_attribute_export_form.setTabOrder(self.delimiter, self.lineterminator)
        mmqgis_attribute_export_form.setTabOrder(self.lineterminator, self.outfilename)
        mmqgis_attribute_export_form.setTabOrder(self.outfilename, self.browseoutfile)
        mmqgis_attribute_export_form.setTabOrder(self.browseoutfile, self.buttonBox)

    def retranslateUi(self, mmqgis_attribute_export_form):
        mmqgis_attribute_export_form.setWindowTitle(_translate("mmqgis_attribute_export_form", "Export Attributes", None))
        self.label.setText(_translate("mmqgis_attribute_export_form", "Output CSV File", None))
        self.outfilename.setText(_translate("mmqgis_attribute_export_form", "data.csv", None))
        self.browseoutfile.setText(_translate("mmqgis_attribute_export_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_attribute_export_form", "Source Layer", None))
        self.label_2.setText(_translate("mmqgis_attribute_export_form", "Attributes", None))
        __sortingEnabled = self.attributes.isSortingEnabled()
        self.attributes.setSortingEnabled(False)
        item = self.attributes.item(0)
        item.setText(_translate("mmqgis_attribute_export_form", "Alpha", None))
        item = self.attributes.item(1)
        item.setText(_translate("mmqgis_attribute_export_form", "Beta", None))
        item = self.attributes.item(2)
        item.setText(_translate("mmqgis_attribute_export_form", "Gamma", None))
        item = self.attributes.item(3)
        item.setText(_translate("mmqgis_attribute_export_form", "Delta", None))
        item = self.attributes.item(4)
        item.setText(_translate("mmqgis_attribute_export_form", "Epsilon", None))
        self.attributes.setSortingEnabled(__sortingEnabled)
        self.delimiter.setItemText(0, _translate("mmqgis_attribute_export_form", "(comma)", None))
        self.delimiter.setItemText(1, _translate("mmqgis_attribute_export_form", "(bar)", None))
        self.delimiter.setItemText(2, _translate("mmqgis_attribute_export_form", "(space)", None))
        self.delimiter.setItemText(3, _translate("mmqgis_attribute_export_form", "(semicolon)", None))
        self.lineterminator.setItemText(0, _translate("mmqgis_attribute_export_form", "CR-LF", None))
        self.lineterminator.setItemText(1, _translate("mmqgis_attribute_export_form", "LF", None))
        self.label_3.setText(_translate("mmqgis_attribute_export_form", "Delimiter", None))
        self.label_5.setText(_translate("mmqgis_attribute_export_form", "Line Terminator", None))
        self.decimalmark.setItemText(0, _translate("mmqgis_attribute_export_form", "(period)", None))
        self.decimalmark.setItemText(1, _translate("mmqgis_attribute_export_form", "(comma)", None))
        self.label_6.setText(_translate("mmqgis_attribute_export_form", "Decimal Mark", None))

