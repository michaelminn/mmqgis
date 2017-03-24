# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_street_address_join_form.ui'
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

class Ui_mmqgis_street_address_join_form(object):
    def setupUi(self, mmqgis_street_address_join_form):
        mmqgis_street_address_join_form.setObjectName(_fromUtf8("mmqgis_street_address_join_form"))
        mmqgis_street_address_join_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_street_address_join_form.setEnabled(True)
        mmqgis_street_address_join_form.resize(378, 369)
        mmqgis_street_address_join_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_street_address_join_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 330, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_street_address_join_form)
        self.label.setGeometry(QtCore.QRect(10, 220, 261, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(mmqgis_street_address_join_form)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 181, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.outfilename = QtGui.QLineEdit(mmqgis_street_address_join_form)
        self.outfilename.setGeometry(QtCore.QRect(10, 240, 261, 21))
        self.outfilename.setReadOnly(False)
        self.outfilename.setObjectName(_fromUtf8("outfilename"))
        self.browse_outfile = QtGui.QPushButton(mmqgis_street_address_join_form)
        self.browse_outfile.setGeometry(QtCore.QRect(280, 240, 79, 26))
        self.browse_outfile.setObjectName(_fromUtf8("browse_outfile"))
        self.shapeaddress = QtGui.QComboBox(mmqgis_street_address_join_form)
        self.shapeaddress.setGeometry(QtCore.QRect(10, 180, 341, 27))
        self.shapeaddress.setObjectName(_fromUtf8("shapeaddress"))
        self.shapelayer = QtGui.QComboBox(mmqgis_street_address_join_form)
        self.shapelayer.setGeometry(QtCore.QRect(10, 130, 341, 27))
        self.shapelayer.setObjectName(_fromUtf8("shapelayer"))
        self.label_4 = QtGui.QLabel(mmqgis_street_address_join_form)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 111, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_2 = QtGui.QLabel(mmqgis_street_address_join_form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 141, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.infilename = QtGui.QLineEdit(mmqgis_street_address_join_form)
        self.infilename.setGeometry(QtCore.QRect(10, 30, 261, 21))
        self.infilename.setText(_fromUtf8(""))
        self.infilename.setReadOnly(False)
        self.infilename.setObjectName(_fromUtf8("infilename"))
        self.browse_infile = QtGui.QPushButton(mmqgis_street_address_join_form)
        self.browse_infile.setGeometry(QtCore.QRect(280, 30, 79, 26))
        self.browse_infile.setObjectName(_fromUtf8("browse_infile"))
        self.label_5 = QtGui.QLabel(mmqgis_street_address_join_form)
        self.label_5.setGeometry(QtCore.QRect(10, 270, 261, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.notfoundfilename = QtGui.QLineEdit(mmqgis_street_address_join_form)
        self.notfoundfilename.setGeometry(QtCore.QRect(10, 290, 261, 21))
        self.notfoundfilename.setReadOnly(False)
        self.notfoundfilename.setObjectName(_fromUtf8("notfoundfilename"))
        self.browse_notfound = QtGui.QPushButton(mmqgis_street_address_join_form)
        self.browse_notfound.setGeometry(QtCore.QRect(280, 290, 79, 26))
        self.browse_notfound.setObjectName(_fromUtf8("browse_notfound"))
        self.csvaddress = QtGui.QComboBox(mmqgis_street_address_join_form)
        self.csvaddress.setGeometry(QtCore.QRect(10, 80, 341, 27))
        self.csvaddress.setObjectName(_fromUtf8("csvaddress"))
        self.label_6 = QtGui.QLabel(mmqgis_street_address_join_form)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 171, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(mmqgis_street_address_join_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_street_address_join_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_street_address_join_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_street_address_join_form)
        mmqgis_street_address_join_form.setTabOrder(self.infilename, self.browse_infile)
        mmqgis_street_address_join_form.setTabOrder(self.browse_infile, self.csvaddress)
        mmqgis_street_address_join_form.setTabOrder(self.csvaddress, self.shapelayer)
        mmqgis_street_address_join_form.setTabOrder(self.shapelayer, self.shapeaddress)
        mmqgis_street_address_join_form.setTabOrder(self.shapeaddress, self.outfilename)
        mmqgis_street_address_join_form.setTabOrder(self.outfilename, self.browse_outfile)
        mmqgis_street_address_join_form.setTabOrder(self.browse_outfile, self.notfoundfilename)
        mmqgis_street_address_join_form.setTabOrder(self.notfoundfilename, self.browse_notfound)
        mmqgis_street_address_join_form.setTabOrder(self.browse_notfound, self.buttonBox)

    def retranslateUi(self, mmqgis_street_address_join_form):
        mmqgis_street_address_join_form.setWindowTitle(_translate("mmqgis_street_address_join_form", "Street Address Join", None))
        self.label.setText(_translate("mmqgis_street_address_join_form", "Output Shapefile", None))
        self.label_3.setText(_translate("mmqgis_street_address_join_form", "Shape Layer Address Field", None))
        self.outfilename.setText(_translate("mmqgis_street_address_join_form", "temp.shp", None))
        self.browse_outfile.setText(_translate("mmqgis_street_address_join_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_street_address_join_form", "Shape Layer", None))
        self.label_2.setText(_translate("mmqgis_street_address_join_form", "Input CSV File (UTF-8)", None))
        self.browse_infile.setText(_translate("mmqgis_street_address_join_form", "Browse...", None))
        self.label_5.setText(_translate("mmqgis_street_address_join_form", "Not Found CSV Output List", None))
        self.notfoundfilename.setText(_translate("mmqgis_street_address_join_form", "notfound.csv", None))
        self.browse_notfound.setText(_translate("mmqgis_street_address_join_form", "Browse...", None))
        self.label_6.setText(_translate("mmqgis_street_address_join_form", "CSV File Address Field", None))

