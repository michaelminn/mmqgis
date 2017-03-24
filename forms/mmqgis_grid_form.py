# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmqgis_grid_form.ui'
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

class Ui_mmqgis_grid_form(object):
    def setupUi(self, mmqgis_grid_form):
        mmqgis_grid_form.setObjectName(_fromUtf8("mmqgis_grid_form"))
        mmqgis_grid_form.setWindowModality(QtCore.Qt.ApplicationModal)
        mmqgis_grid_form.setEnabled(True)
        mmqgis_grid_form.resize(402, 385)
        mmqgis_grid_form.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(mmqgis_grid_form)
        self.buttonBox.setGeometry(QtCore.QRect(130, 350, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(mmqgis_grid_form)
        self.label.setGeometry(QtCore.QRect(10, 290, 108, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(mmqgis_grid_form)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 91, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.xleft = QtGui.QLineEdit(mmqgis_grid_form)
        self.xleft.setGeometry(QtCore.QRect(10, 220, 121, 22))
        self.xleft.setObjectName(_fromUtf8("xleft"))
        self.savename = QtGui.QLineEdit(mmqgis_grid_form)
        self.savename.setGeometry(QtCore.QRect(10, 310, 281, 21))
        self.savename.setReadOnly(False)
        self.savename.setObjectName(_fromUtf8("savename"))
        self.browse = QtGui.QPushButton(mmqgis_grid_form)
        self.browse.setGeometry(QtCore.QRect(310, 310, 79, 26))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.ytop = QtGui.QLineEdit(mmqgis_grid_form)
        self.ytop.setGeometry(QtCore.QRect(140, 180, 121, 22))
        self.ytop.setObjectName(_fromUtf8("ytop"))
        self.xright = QtGui.QLineEdit(mmqgis_grid_form)
        self.xright.setGeometry(QtCore.QRect(270, 220, 121, 22))
        self.xright.setObjectName(_fromUtf8("xright"))
        self.label_6 = QtGui.QLabel(mmqgis_grid_form)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 91, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(mmqgis_grid_form)
        self.label_7.setGeometry(QtCore.QRect(210, 110, 111, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.xspacing = QtGui.QLineEdit(mmqgis_grid_form)
        self.xspacing.setGeometry(QtCore.QRect(10, 80, 121, 22))
        self.xspacing.setObjectName(_fromUtf8("xspacing"))
        self.shapetype = QtGui.QComboBox(mmqgis_grid_form)
        self.shapetype.setGeometry(QtCore.QRect(10, 30, 381, 22))
        self.shapetype.setObjectName(_fromUtf8("shapetype"))
        self.units = QtGui.QComboBox(mmqgis_grid_form)
        self.units.setGeometry(QtCore.QRect(270, 80, 121, 22))
        self.units.setObjectName(_fromUtf8("units"))
        self.label_8 = QtGui.QLabel(mmqgis_grid_form)
        self.label_8.setGeometry(QtCore.QRect(140, 60, 91, 22))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.yspacing = QtGui.QLineEdit(mmqgis_grid_form)
        self.yspacing.setGeometry(QtCore.QRect(140, 80, 121, 22))
        self.yspacing.setObjectName(_fromUtf8("yspacing"))
        self.label_9 = QtGui.QLabel(mmqgis_grid_form)
        self.label_9.setGeometry(QtCore.QRect(270, 60, 91, 22))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.extenttype = QtGui.QComboBox(mmqgis_grid_form)
        self.extenttype.setGeometry(QtCore.QRect(10, 130, 181, 22))
        self.extenttype.setObjectName(_fromUtf8("extenttype"))
        self.ybottom = QtGui.QLineEdit(mmqgis_grid_form)
        self.ybottom.setGeometry(QtCore.QRect(140, 260, 121, 22))
        self.ybottom.setObjectName(_fromUtf8("ybottom"))
        self.label_10 = QtGui.QLabel(mmqgis_grid_form)
        self.label_10.setGeometry(QtCore.QRect(140, 160, 61, 22))
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(mmqgis_grid_form)
        self.label_11.setGeometry(QtCore.QRect(140, 240, 71, 22))
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_3 = QtGui.QLabel(mmqgis_grid_form)
        self.label_3.setGeometry(QtCore.QRect(270, 200, 91, 22))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.layername = QtGui.QComboBox(mmqgis_grid_form)
        self.layername.setGeometry(QtCore.QRect(210, 130, 181, 22))
        self.layername.setObjectName(_fromUtf8("layername"))
        self.typelabel = QtGui.QLabel(mmqgis_grid_form)
        self.typelabel.setGeometry(QtCore.QRect(10, 10, 91, 22))
        self.typelabel.setObjectName(_fromUtf8("typelabel"))
        self.extentlabel = QtGui.QLabel(mmqgis_grid_form)
        self.extentlabel.setGeometry(QtCore.QRect(10, 110, 91, 22))
        self.extentlabel.setObjectName(_fromUtf8("extentlabel"))

        self.retranslateUi(mmqgis_grid_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), mmqgis_grid_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mmqgis_grid_form.reject)
        QtCore.QMetaObject.connectSlotsByName(mmqgis_grid_form)
        mmqgis_grid_form.setTabOrder(self.shapetype, self.xspacing)
        mmqgis_grid_form.setTabOrder(self.xspacing, self.yspacing)
        mmqgis_grid_form.setTabOrder(self.yspacing, self.units)
        mmqgis_grid_form.setTabOrder(self.units, self.extenttype)
        mmqgis_grid_form.setTabOrder(self.extenttype, self.layername)
        mmqgis_grid_form.setTabOrder(self.layername, self.ytop)
        mmqgis_grid_form.setTabOrder(self.ytop, self.xleft)
        mmqgis_grid_form.setTabOrder(self.xleft, self.xright)
        mmqgis_grid_form.setTabOrder(self.xright, self.ybottom)
        mmqgis_grid_form.setTabOrder(self.ybottom, self.savename)
        mmqgis_grid_form.setTabOrder(self.savename, self.browse)
        mmqgis_grid_form.setTabOrder(self.browse, self.buttonBox)

    def retranslateUi(self, mmqgis_grid_form):
        mmqgis_grid_form.setWindowTitle(_translate("mmqgis_grid_form", "Grid", None))
        self.label.setText(_translate("mmqgis_grid_form", "Output Shapefile", None))
        self.label_2.setText(_translate("mmqgis_grid_form", "Left Y", None))
        self.xleft.setText(_translate("mmqgis_grid_form", "10", None))
        self.savename.setText(_translate("mmqgis_grid_form", "grid.shp", None))
        self.browse.setText(_translate("mmqgis_grid_form", "Browse...", None))
        self.ytop.setText(_translate("mmqgis_grid_form", "0", None))
        self.xright.setText(_translate("mmqgis_grid_form", "0", None))
        self.label_6.setText(_translate("mmqgis_grid_form", "X Spacing", None))
        self.label_7.setText(_translate("mmqgis_grid_form", "Layer", None))
        self.xspacing.setText(_translate("mmqgis_grid_form", "100", None))
        self.label_8.setText(_translate("mmqgis_grid_form", "Y Spacing", None))
        self.yspacing.setText(_translate("mmqgis_grid_form", "100", None))
        self.label_9.setText(_translate("mmqgis_grid_form", "Units", None))
        self.ybottom.setText(_translate("mmqgis_grid_form", "0", None))
        self.label_10.setText(_translate("mmqgis_grid_form", "Top Y", None))
        self.label_11.setText(_translate("mmqgis_grid_form", "Bottom Y", None))
        self.label_3.setText(_translate("mmqgis_grid_form", "Right Y", None))
        self.typelabel.setText(_translate("mmqgis_grid_form", "Shape Type", None))
        self.extentlabel.setText(_translate("mmqgis_grid_form", "Extent", None))

