# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_merge_form.ui'
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

class Ui_mmqgis_merge_form(object):
    def setupUi(self, mmqgis_merge_form):
        mmqgis_merge_form.setObjectName(_fromUtf8("mmqgis_merge_form"))
        mmqgis_merge_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_merge_form.setEnabled(True)
        mmqgis_merge_form.resize(372, 346)
        mmqgis_merge_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_merge_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 310, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_merge_form)
        self.label.setGeometry(QtCore.QRect(10, 250, 121, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.outfilename = QtGui.QLineEdit(mmqgis_merge_form)
        self.outfilename.setGeometry(QtCore.QRect(10, 270, 261, 21))
        self.outfilename.setReadOnly(False)
        self.outfilename.setObjectName(_fromUtf8("outfilename"))
        self.browseoutfile = QtGui.QPushButton(mmqgis_merge_form)
        self.browseoutfile.setGeometry(QtCore.QRect(280, 270, 79, 26))
        self.browseoutfile.setObjectName(_fromUtf8("browseoutfile"))
        self.label_4 = QtGui.QLabel(mmqgis_merge_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 141, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.sourcelayers = QtGui.QListWidget(mmqgis_merge_form)
        self.sourcelayers.setGeometry(QtCore.QRect(10, 30, 341, 211))
        self.sourcelayers.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.sourcelayers.setObjectName(_fromUtf8("sourcelayers"))
        item = QtGui.QListWidgetItem()
        self.sourcelayers.addItem(item)
        item = QtGui.QListWidgetItem()
        self.sourcelayers.addItem(item)
        item = QtGui.QListWidgetItem()
        self.sourcelayers.addItem(item)
        item = QtGui.QListWidgetItem()
        self.sourcelayers.addItem(item)
        item = QtGui.QListWidgetItem()
        self.sourcelayers.addItem(item)

        self.retranslateUi(mmqgis_merge_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_merge_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_merge_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_merge_form)
        mmqgis_merge_form.setTabOrder(self.sourcelayers, self.outfilename)
        mmqgis_merge_form.setTabOrder(self.outfilename, self.browseoutfile)
        mmqgis_merge_form.setTabOrder(self.browseoutfile, self.buttonBox)

    def retranslateUi(self, mmqgis_merge_form):
        mmqgis_merge_form.setWindowTitle(_translate("mmqgis_merge_form", "Merge Layers", None))
        self.label.setText(_translate("mmqgis_merge_form", "Output Shapefile", None))
        self.outfilename.setText(_translate("mmqgis_merge_form", "merge.csv", None))
        self.browseoutfile.setText(_translate("mmqgis_merge_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_merge_form", "Select Source Layers", None))
        __sortingEnabled = self.sourcelayers.isSortingEnabled()
        self.sourcelayers.setSortingEnabled(False)
        item = self.sourcelayers.item(0)
        item.setText(_translate("mmqgis_merge_form", "Alpha", None))
        item = self.sourcelayers.item(1)
        item.setText(_translate("mmqgis_merge_form", "Beta", None))
        item = self.sourcelayers.item(2)
        item.setText(_translate("mmqgis_merge_form", "Gamma", None))
        item = self.sourcelayers.item(3)
        item.setText(_translate("mmqgis_merge_form", "Delta", None))
        item = self.sourcelayers.item(4)
        item.setText(_translate("mmqgis_merge_form", "Epsilon", None))
        self.sourcelayers.setSortingEnabled(__sortingEnabled)

