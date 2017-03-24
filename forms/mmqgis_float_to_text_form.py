# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_float_to_text_form.ui'
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

class Ui_mmqgis_float_to_text_form(object):
    def setupUi(self, mmqgis_float_to_text_form):
        mmqgis_float_to_text_form.setObjectName(_fromUtf8("mmqgis_float_to_text_form"))
        mmqgis_float_to_text_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_float_to_text_form.setEnabled(True)
        mmqgis_float_to_text_form.resize(372, 403)
        mmqgis_float_to_text_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_float_to_text_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 370, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_float_to_text_form)
        self.label.setGeometry(QtCore.QRect(10, 320, 261, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.filename = QtGui.QLineEdit(mmqgis_float_to_text_form)
        self.filename.setGeometry(QtCore.QRect(10, 340, 261, 21))
        self.filename.setReadOnly(False)
        self.filename.setObjectName(_fromUtf8("filename"))
        self.browse = QtGui.QPushButton(mmqgis_float_to_text_form)
        self.browse.setGeometry(QtCore.QRect(280, 340, 79, 26))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.sourcelayer = QtGui.QComboBox(mmqgis_float_to_text_form)
        self.sourcelayer.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.sourcelayer.setObjectName(_fromUtf8("sourcelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_float_to_text_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 121, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.fieldnames = QtGui.QListWidget(mmqgis_float_to_text_form)
        self.fieldnames.setGeometry(QtCore.QRect(10, 90, 341, 121))
        self.fieldnames.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.fieldnames.setObjectName(_fromUtf8("fieldnames"))
        self.label_5 = QtGui.QLabel(mmqgis_float_to_text_form)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 121, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.separator = QtGui.QComboBox(mmqgis_float_to_text_form)
        self.separator.setGeometry(QtCore.QRect(10, 240, 131, 22))
        self.separator.setObjectName(_fromUtf8("separator"))
        self.separator.addItem(_fromUtf8(""))
        self.separator.addItem(_fromUtf8(""))
        self.separator.addItem(_fromUtf8(""))
        self.label_6 = QtGui.QLabel(mmqgis_float_to_text_form)
        self.label_6.setGeometry(QtCore.QRect(10, 220, 121, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.decimals = QtGui.QComboBox(mmqgis_float_to_text_form)
        self.decimals.setGeometry(QtCore.QRect(210, 240, 131, 22))
        self.decimals.setObjectName(_fromUtf8("decimals"))
        self.decimals.addItem(_fromUtf8(""))
        self.decimals.addItem(_fromUtf8(""))
        self.decimals.addItem(_fromUtf8(""))
        self.decimals.addItem(_fromUtf8(""))
        self.decimals.addItem(_fromUtf8(""))
        self.decimals.addItem(_fromUtf8(""))
        self.decimals.addItem(_fromUtf8(""))
        self.decimals.addItem(_fromUtf8(""))
        self.decimals.addItem(_fromUtf8(""))
        self.decimals.addItem(_fromUtf8(""))
        self.decimals.addItem(_fromUtf8(""))
        self.decimals.addItem(_fromUtf8(""))
        self.decimals.addItem(_fromUtf8(""))
        self.label_7 = QtGui.QLabel(mmqgis_float_to_text_form)
        self.label_7.setGeometry(QtCore.QRect(210, 220, 121, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.prefix = QtGui.QLineEdit(mmqgis_float_to_text_form)
        self.prefix.setGeometry(QtCore.QRect(10, 290, 131, 21))
        self.prefix.setObjectName(_fromUtf8("prefix"))
        self.label_8 = QtGui.QLabel(mmqgis_float_to_text_form)
        self.label_8.setGeometry(QtCore.QRect(10, 270, 121, 22))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(mmqgis_float_to_text_form)
        self.label_9.setGeometry(QtCore.QRect(210, 270, 121, 22))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.suffix = QtGui.QLineEdit(mmqgis_float_to_text_form)
        self.suffix.setGeometry(QtCore.QRect(210, 290, 131, 21))
        self.suffix.setObjectName(_fromUtf8("suffix"))

        self.retranslateUi(mmqgis_float_to_text_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_float_to_text_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_float_to_text_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_float_to_text_form)
        mmqgis_float_to_text_form.setTabOrder(self.sourcelayer, self.fieldnames)
        mmqgis_float_to_text_form.setTabOrder(self.fieldnames, self.separator)
        mmqgis_float_to_text_form.setTabOrder(self.separator, self.decimals)
        mmqgis_float_to_text_form.setTabOrder(self.decimals, self.prefix)
        mmqgis_float_to_text_form.setTabOrder(self.prefix, self.suffix)
        mmqgis_float_to_text_form.setTabOrder(self.suffix, self.filename)
        mmqgis_float_to_text_form.setTabOrder(self.filename, self.browse)
        mmqgis_float_to_text_form.setTabOrder(self.browse, self.buttonBox)

    def retranslateUi(self, mmqgis_float_to_text_form):
        mmqgis_float_to_text_form.setWindowTitle(_translate("mmqgis_float_to_text_form", "Float to Text", None))
        self.label.setText(_translate("mmqgis_float_to_text_form", "Output Shapefile", None))
        self.filename.setText(_translate("mmqgis_float_to_text_form", "temp.shp", None))
        self.browse.setText(_translate("mmqgis_float_to_text_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_float_to_text_form", "Source Layer", None))
        self.label_5.setText(_translate("mmqgis_float_to_text_form", "Fields to Convert", None))
        self.separator.setItemText(0, _translate("mmqgis_float_to_text_form", "None", None))
        self.separator.setItemText(1, _translate("mmqgis_float_to_text_form", "Comma", None))
        self.separator.setItemText(2, _translate("mmqgis_float_to_text_form", "Space", None))
        self.label_6.setText(_translate("mmqgis_float_to_text_form", "000\'s Separator", None))
        self.decimals.setItemText(0, _translate("mmqgis_float_to_text_form", "0", None))
        self.decimals.setItemText(1, _translate("mmqgis_float_to_text_form", "1", None))
        self.decimals.setItemText(2, _translate("mmqgis_float_to_text_form", "2", None))
        self.decimals.setItemText(3, _translate("mmqgis_float_to_text_form", "3", None))
        self.decimals.setItemText(4, _translate("mmqgis_float_to_text_form", "4", None))
        self.decimals.setItemText(5, _translate("mmqgis_float_to_text_form", "5", None))
        self.decimals.setItemText(6, _translate("mmqgis_float_to_text_form", "6", None))
        self.decimals.setItemText(7, _translate("mmqgis_float_to_text_form", "7", None))
        self.decimals.setItemText(8, _translate("mmqgis_float_to_text_form", "8", None))
        self.decimals.setItemText(9, _translate("mmqgis_float_to_text_form", "9", None))
        self.decimals.setItemText(10, _translate("mmqgis_float_to_text_form", "10", None))
        self.decimals.setItemText(11, _translate("mmqgis_float_to_text_form", "11", None))
        self.decimals.setItemText(12, _translate("mmqgis_float_to_text_form", "12", None))
        self.label_7.setText(_translate("mmqgis_float_to_text_form", "Decimal Places", None))
        self.label_8.setText(_translate("mmqgis_float_to_text_form", "Prefix", None))
        self.label_9.setText(_translate("mmqgis_float_to_text_form", "Suffix", None))

