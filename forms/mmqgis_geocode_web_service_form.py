# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_geocode_web_service_form.ui'
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

class Ui_mmqgis_geocode_web_service_form(object):
    def setupUi(self, mmqgis_geocode_web_service_form):
        mmqgis_geocode_web_service_form.setObjectName(_fromUtf8("mmqgis_geocode_web_service_form"))
        mmqgis_geocode_web_service_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_geocode_web_service_form.setEnabled(True)
        mmqgis_geocode_web_service_form.resize(468, 361)
        mmqgis_geocode_web_service_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_geocode_web_service_form)
        self.buttonBox.setGeometry(QtCore.QRect(150, 320, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_geocode_web_service_form)
        self.label.setGeometry(QtCore.QRect(10, 210, 141, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(mmqgis_geocode_web_service_form)
        self.label_3.setGeometry(QtCore.QRect(240, 60, 111, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.shapefilename = QtGui.QLineEdit(mmqgis_geocode_web_service_form)
        self.shapefilename.setGeometry(QtCore.QRect(10, 230, 341, 21))
        self.shapefilename.setReadOnly(False)
        self.shapefilename.setObjectName(_fromUtf8("shapefilename"))
        self.browse_shapefile = QtGui.QPushButton(mmqgis_geocode_web_service_form)
        self.browse_shapefile.setGeometry(QtCore.QRect(370, 230, 79, 26))
        self.browse_shapefile.setObjectName(_fromUtf8("browse_shapefile"))
        self.cityfield = QtGui.QComboBox(mmqgis_geocode_web_service_form)
        self.cityfield.setGeometry(QtCore.QRect(240, 80, 211, 27))
        self.cityfield.setObjectName(_fromUtf8("cityfield"))
        self.addressfield = QtGui.QComboBox(mmqgis_geocode_web_service_form)
        self.addressfield.setGeometry(QtCore.QRect(10, 80, 211, 27))
        self.addressfield.setObjectName(_fromUtf8("addressfield"))
        self.label_4 = QtGui.QLabel(mmqgis_geocode_web_service_form)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 111, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_2 = QtGui.QLabel(mmqgis_geocode_web_service_form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 151, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.infilename = QtGui.QLineEdit(mmqgis_geocode_web_service_form)
        self.infilename.setGeometry(QtCore.QRect(10, 30, 341, 21))
        self.infilename.setText(_fromUtf8(""))
        self.infilename.setReadOnly(False)
        self.infilename.setObjectName(_fromUtf8("infilename"))
        self.browse_infile = QtGui.QPushButton(mmqgis_geocode_web_service_form)
        self.browse_infile.setGeometry(QtCore.QRect(370, 30, 79, 26))
        self.browse_infile.setObjectName(_fromUtf8("browse_infile"))
        self.label_5 = QtGui.QLabel(mmqgis_geocode_web_service_form)
        self.label_5.setGeometry(QtCore.QRect(10, 260, 171, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.notfoundfilename = QtGui.QLineEdit(mmqgis_geocode_web_service_form)
        self.notfoundfilename.setGeometry(QtCore.QRect(10, 280, 341, 21))
        self.notfoundfilename.setReadOnly(False)
        self.notfoundfilename.setObjectName(_fromUtf8("notfoundfilename"))
        self.browse_notfound = QtGui.QPushButton(mmqgis_geocode_web_service_form)
        self.browse_notfound.setGeometry(QtCore.QRect(370, 270, 79, 26))
        self.browse_notfound.setObjectName(_fromUtf8("browse_notfound"))
        self.statefield = QtGui.QComboBox(mmqgis_geocode_web_service_form)
        self.statefield.setGeometry(QtCore.QRect(10, 130, 211, 27))
        self.statefield.setObjectName(_fromUtf8("statefield"))
        self.label_6 = QtGui.QLabel(mmqgis_geocode_web_service_form)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 171, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.countryfield = QtGui.QComboBox(mmqgis_geocode_web_service_form)
        self.countryfield.setGeometry(QtCore.QRect(240, 130, 211, 27))
        self.countryfield.setObjectName(_fromUtf8("countryfield"))
        self.label_7 = QtGui.QLabel(mmqgis_geocode_web_service_form)
        self.label_7.setGeometry(QtCore.QRect(240, 110, 171, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.servicename = QtGui.QComboBox(mmqgis_geocode_web_service_form)
        self.servicename.setGeometry(QtCore.QRect(10, 180, 211, 27))
        self.servicename.setObjectName(_fromUtf8("servicename"))
        self.label_8 = QtGui.QLabel(mmqgis_geocode_web_service_form)
        self.label_8.setGeometry(QtCore.QRect(10, 160, 171, 22))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.apikey = QtGui.QLineEdit(mmqgis_geocode_web_service_form)
        self.apikey.setGeometry(QtCore.QRect(240, 180, 211, 21))
        self.apikey.setObjectName(_fromUtf8("apikey"))
        self.label_9 = QtGui.QLabel(mmqgis_geocode_web_service_form)
        self.label_9.setGeometry(QtCore.QRect(240, 160, 171, 22))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(mmqgis_geocode_web_service_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_geocode_web_service_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_geocode_web_service_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_geocode_web_service_form)
        mmqgis_geocode_web_service_form.setTabOrder(self.infilename, self.browse_infile)
        mmqgis_geocode_web_service_form.setTabOrder(self.browse_infile, self.addressfield)
        mmqgis_geocode_web_service_form.setTabOrder(self.addressfield, self.cityfield)
        mmqgis_geocode_web_service_form.setTabOrder(self.cityfield, self.statefield)
        mmqgis_geocode_web_service_form.setTabOrder(self.statefield, self.countryfield)
        mmqgis_geocode_web_service_form.setTabOrder(self.countryfield, self.servicename)
        mmqgis_geocode_web_service_form.setTabOrder(self.servicename, self.shapefilename)
        mmqgis_geocode_web_service_form.setTabOrder(self.shapefilename, self.browse_shapefile)
        mmqgis_geocode_web_service_form.setTabOrder(self.browse_shapefile, self.notfoundfilename)
        mmqgis_geocode_web_service_form.setTabOrder(self.notfoundfilename, self.browse_notfound)
        mmqgis_geocode_web_service_form.setTabOrder(self.browse_notfound, self.buttonBox)

    def retranslateUi(self, mmqgis_geocode_web_service_form):
        mmqgis_geocode_web_service_form.setWindowTitle(_translate("mmqgis_geocode_web_service_form", "Web Service Geocode", None))
        self.label.setText(_translate("mmqgis_geocode_web_service_form", "Output Shapefile", None))
        self.label_3.setText(_translate("mmqgis_geocode_web_service_form", "City Field", None))
        self.shapefilename.setText(_translate("mmqgis_geocode_web_service_form", "geocoded.shp", None))
        self.browse_shapefile.setText(_translate("mmqgis_geocode_web_service_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_geocode_web_service_form", "Address Field", None))
        self.label_2.setText(_translate("mmqgis_geocode_web_service_form", "Input CSV File (UTF-8)", None))
        self.browse_infile.setText(_translate("mmqgis_geocode_web_service_form", "Browse...", None))
        self.label_5.setText(_translate("mmqgis_geocode_web_service_form", "Not Found Output List", None))
        self.notfoundfilename.setText(_translate("mmqgis_geocode_web_service_form", "notfound.csv", None))
        self.browse_notfound.setText(_translate("mmqgis_geocode_web_service_form", "Browse...", None))
        self.label_6.setText(_translate("mmqgis_geocode_web_service_form", "State Field", None))
        self.label_7.setText(_translate("mmqgis_geocode_web_service_form", "Country Field", None))
        self.label_8.setText(_translate("mmqgis_geocode_web_service_form", "Web Service", None))
        self.label_9.setText(_translate("mmqgis_geocode_web_service_form", "Google API Key (optional)", None))

