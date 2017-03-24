# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_animate_columns_form.ui'
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

class Ui_mmqgis_animate_columns_form(object):
    def setupUi(self, mmqgis_animate_columns_form):
        mmqgis_animate_columns_form.setObjectName(_fromUtf8("mmqgis_animate_columns_form"))
        mmqgis_animate_columns_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_animate_columns_form.setEnabled(True)
        mmqgis_animate_columns_form.resize(380, 310)
        mmqgis_animate_columns_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_animate_columns_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 270, 160, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_animate_columns_form)
        self.label.setGeometry(QtCore.QRect(10, 210, 161, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.outdirname = QtGui.QLineEdit(mmqgis_animate_columns_form)
        self.outdirname.setGeometry(QtCore.QRect(10, 230, 271, 31))
        self.outdirname.setReadOnly(False)
        self.outdirname.setObjectName(_fromUtf8("outdirname"))
        self.browseoutfile = QtGui.QPushButton(mmqgis_animate_columns_form)
        self.browseoutfile.setGeometry(QtCore.QRect(290, 230, 79, 31))
        self.browseoutfile.setObjectName(_fromUtf8("browseoutfile"))
        self.layername = QtGui.QComboBox(mmqgis_animate_columns_form)
        self.layername.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.layername.setObjectName(_fromUtf8("layername"))
        self.label_4 = QtGui.QLabel(mmqgis_animate_columns_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 108, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.durationframes = QtGui.QLineEdit(mmqgis_animate_columns_form)
        self.durationframes.setGeometry(QtCore.QRect(10, 180, 111, 21))
        self.durationframes.setReadOnly(False)
        self.durationframes.setObjectName(_fromUtf8("durationframes"))
        self.label_7 = QtGui.QLabel(mmqgis_animate_columns_form)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 121, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_6 = QtGui.QLabel(mmqgis_animate_columns_form)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 151, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.latoffsetcol = QtGui.QComboBox(mmqgis_animate_columns_form)
        self.latoffsetcol.setGeometry(QtCore.QRect(10, 80, 351, 27))
        self.latoffsetcol.setObjectName(_fromUtf8("latoffsetcol"))
        self.longoffsetcol = QtGui.QComboBox(mmqgis_animate_columns_form)
        self.longoffsetcol.setGeometry(QtCore.QRect(10, 130, 351, 27))
        self.longoffsetcol.setObjectName(_fromUtf8("longoffsetcol"))
        self.label_9 = QtGui.QLabel(mmqgis_animate_columns_form)
        self.label_9.setGeometry(QtCore.QRect(10, 110, 161, 22))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(mmqgis_animate_columns_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_animate_columns_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_animate_columns_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_animate_columns_form)
        mmqgis_animate_columns_form.setTabOrder(self.layername, self.latoffsetcol)
        mmqgis_animate_columns_form.setTabOrder(self.latoffsetcol, self.longoffsetcol)
        mmqgis_animate_columns_form.setTabOrder(self.longoffsetcol, self.durationframes)
        mmqgis_animate_columns_form.setTabOrder(self.durationframes, self.outdirname)
        mmqgis_animate_columns_form.setTabOrder(self.outdirname, self.browseoutfile)
        mmqgis_animate_columns_form.setTabOrder(self.browseoutfile, self.buttonBox)

    def retranslateUi(self, mmqgis_animate_columns_form):
        mmqgis_animate_columns_form.setWindowTitle(_translate("mmqgis_animate_columns_form", "Animate Columns", None))
        self.label.setText(_translate("mmqgis_animate_columns_form", "Image Output Directory", None))
        self.outdirname.setText(_translate("mmqgis_animate_columns_form", "frames", None))
        self.browseoutfile.setText(_translate("mmqgis_animate_columns_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_animate_columns_form", "Animation Layer", None))
        self.durationframes.setText(_translate("mmqgis_animate_columns_form", "50", None))
        self.label_7.setText(_translate("mmqgis_animate_columns_form", "Duration (Frames)", None))
        self.label_6.setText(_translate("mmqgis_animate_columns_form", "Latitude Offset Column", None))
        self.label_9.setText(_translate("mmqgis_animate_columns_form", "Longitude Offset Column", None))

