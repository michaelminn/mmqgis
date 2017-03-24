# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_animate_lines_form.ui'
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

class Ui_mmqgis_animate_lines_form(object):
    def setupUi(self, mmqgis_animate_lines_form):
        mmqgis_animate_lines_form.setObjectName(_fromUtf8("mmqgis_animate_lines_form"))
        mmqgis_animate_lines_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_animate_lines_form.setEnabled(True)
        mmqgis_animate_lines_form.resize(380, 260)
        mmqgis_animate_lines_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_animate_lines_form)
        self.buttonBox.setGeometry(QtCore.QRect(110, 220, 160, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_animate_lines_form)
        self.label.setGeometry(QtCore.QRect(10, 160, 161, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.outdirname = QtGui.QLineEdit(mmqgis_animate_lines_form)
        self.outdirname.setGeometry(QtCore.QRect(10, 180, 271, 31))
        self.outdirname.setReadOnly(False)
        self.outdirname.setObjectName(_fromUtf8("outdirname"))
        self.browseoutfile = QtGui.QPushButton(mmqgis_animate_lines_form)
        self.browseoutfile.setGeometry(QtCore.QRect(290, 180, 79, 31))
        self.browseoutfile.setObjectName(_fromUtf8("browseoutfile"))
        self.layername = QtGui.QComboBox(mmqgis_animate_lines_form)
        self.layername.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.layername.setObjectName(_fromUtf8("layername"))
        self.label_4 = QtGui.QLabel(mmqgis_animate_lines_form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 108, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.durationframes = QtGui.QLineEdit(mmqgis_animate_lines_form)
        self.durationframes.setGeometry(QtCore.QRect(10, 130, 111, 21))
        self.durationframes.setReadOnly(False)
        self.durationframes.setObjectName(_fromUtf8("durationframes"))
        self.label_7 = QtGui.QLabel(mmqgis_animate_lines_form)
        self.label_7.setGeometry(QtCore.QRect(10, 110, 121, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_6 = QtGui.QLabel(mmqgis_animate_lines_form)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 151, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.timing = QtGui.QComboBox(mmqgis_animate_lines_form)
        self.timing.setGeometry(QtCore.QRect(10, 80, 351, 27))
        self.timing.setObjectName(_fromUtf8("timing"))
        self.timing.addItem(_fromUtf8(""))
        self.timing.addItem(_fromUtf8(""))

        self.retranslateUi(mmqgis_animate_lines_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_animate_lines_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_animate_lines_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_animate_lines_form)
        mmqgis_animate_lines_form.setTabOrder(self.layername, self.timing)
        mmqgis_animate_lines_form.setTabOrder(self.timing, self.durationframes)
        mmqgis_animate_lines_form.setTabOrder(self.durationframes, self.outdirname)
        mmqgis_animate_lines_form.setTabOrder(self.outdirname, self.browseoutfile)
        mmqgis_animate_lines_form.setTabOrder(self.browseoutfile, self.buttonBox)

    def retranslateUi(self, mmqgis_animate_lines_form):
        mmqgis_animate_lines_form.setWindowTitle(_translate("mmqgis_animate_lines_form", "Animate Lines", None))
        self.label.setText(_translate("mmqgis_animate_lines_form", "Image Output Directory", None))
        self.outdirname.setText(_translate("mmqgis_animate_lines_form", "frames", None))
        self.browseoutfile.setText(_translate("mmqgis_animate_lines_form", "Browse...", None))
        self.label_4.setText(_translate("mmqgis_animate_lines_form", "Animation Layer", None))
        self.durationframes.setText(_translate("mmqgis_animate_lines_form", "50", None))
        self.label_7.setText(_translate("mmqgis_animate_lines_form", "Duration (Frames)", None))
        self.label_6.setText(_translate("mmqgis_animate_lines_form", "Timing", None))
        self.timing.setItemText(0, _translate("mmqgis_animate_lines_form", "Different Line Speeds Animated Over Full Duration", None))
        self.timing.setItemText(1, _translate("mmqgis_animate_lines_form", "One Line Speed Determined By Longest Line", None))

