# --------------------------------------------------------
#    mmqgis_dialogs - Dialog classes for mmqgis
#
#    begin                : 10 May 2010
#    copyright            : (c) 2009 - 2015 by Michael Minn
#    email                : See michaelminn.com
#
#   MMQGIS is free software and is offered without guarantee
#   or warranty. You can redistribute it and/or modify it 
#   under the terms of version 2 of the GNU General Public 
#   License (GPL v2) as published by the Free Software 
#   Foundation (www.gnu.org).
# --------------------------------------------------------

import csv
import math
import os.path
import operator

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from mmqgis_library import *

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/forms")

# --------------------------------------------------------
#    mmqgis_street_address_join - Join attributes from a CSV
#	file to a shapefile based on a fuzzy address match
# --------------------------------------------------------

from mmqgis_street_address_join_form import *

class mmqgis_street_address_join_dialog(QDialog, Ui_mmqgis_street_address_join_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browse_infile, SIGNAL("clicked()"), self.browse_infiles)
		QObject.connect(self.browse_outfile, SIGNAL("clicked()"), self.browse_outfiles)
		QObject.connect(self.browse_notfound, SIGNAL("clicked()"), self.browse_notfoundfiles)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.shapelayer, True)

		QObject.connect(self.shapelayer, SIGNAL("currentIndexChanged(QString)"), self.set_shapeaddress)
		self.set_shapeaddress()

		self.outfilename.setText(mmqgis_temp_file_name(".shp"))
		self.notfoundfilename.setText(os.getcwd() + "/notfound.csv")

        def browse_infiles(self):
		newname = QFileDialog.getOpenFileName(None, "Input CSV File", 
			self.infilename.displayText(), "CSV File (*.csv *.txt)")

                if newname:
			header = mmqgis_read_csv_header(self.iface, newname)
			if not header:
				return

			self.csvaddress.clear()
			for field in header:
				self.csvaddress.addItem(field)

			self.infilename.setText(newname)

        def browse_outfiles(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.outfilename.displayText(), "Shapefile (*.shp)")

                if newname != None:
                	self.outfilename.setText(newname)

        def browse_notfoundfiles(self):
		newname = QFileDialog.getSaveFileName(None, "Output Unjoined CSV File", 
			self.notfoundfilename.displayText(), "CSV File (*.csv *.txt)")
                if newname != None:
                	self.notfoundfilename.setText(newname)

	def set_shapeaddress(self):
		self.shapeaddress.clear()
		layer = mmqgis_find_layer(self.shapelayer.currentText())
		if (layer == None):
			return
		for field in layer.fields().toList():
			self.shapeaddress.addItem(field.name())

	def run(self):
		shapelayer = unicode(self.shapelayer.currentText())
		shapeaddress = unicode(self.shapeaddress.currentText())

		csvname = unicode(self.infilename.displayText())
		csvaddress = unicode(self.csvaddress.currentText())

		outfilename = unicode(self.outfilename.displayText())
		notfoundname = unicode(self.notfoundfilename.displayText()).strip()

		message = mmqgis_street_address_join(self.iface, shapelayer, shapeaddress, \
			csvname, csvaddress, outfilename, notfoundname, 1)

		if message != None:
			QMessageBox.critical(self.iface.mainWindow(), "Address Join", message)

# --------------------------------------------------------
#    mmqgis_animate_columns - Create animations by
#		interpolating offsets from attributes
# --------------------------------------------------------

from mmqgis_animate_columns_form import *

class mmqgis_animate_columns_dialog(QDialog, Ui_mmqgis_animate_columns_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)

		QObject.connect(self.browseoutfile, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		for layer in iface.mapCanvas().layers():
			self.layername.addItem(layer.name())

		QObject.connect(self.layername, SIGNAL("currentIndexChanged(QString)"), self.set_column_options)

		self.set_column_options()
		self.outdirname.setText(os.getcwd() + "/frames")

	def set_column_options(self):
		self.latoffsetcol.clear()
		self.longoffsetcol.clear()

		if self.layername.currentIndex() >= 0:
			#print str(self.layername.currentIndex())
			layer = self.iface.mapCanvas().layer(self.layername.currentIndex())
			if layer.type() == QgsMapLayer.VectorLayer:
				for field in layer.fields().toList():
					#print "fields: " + str(index) + str(field.type())
					if (field.type() in [QVariant.Double, QVariant.Int, QVariant.UInt, \
							QVariant.LongLong, QVariant.ULongLong]):
						self.latoffsetcol.addItem(field.name())
						self.longoffsetcol.addItem(field.name())
						#if ("lat" in field.name().toLower()) and ("off" in field.name().toLower()):
						#	self.latoffsetcol.setCurrentIndex(self.latoffsetcol.count() - 1)
						#if ("lon" in field.name().toLower()) and ("off" in field.name().toLower()):
						#	self.longoffsetcol.setCurrentIndex(self.longoffsetcol.count() - 1)
						if ("lat" in field.name().lower()) and ("off" in field.name().lower()):
							self.latoffsetcol.setCurrentIndex(self.latoffsetcol.count() - 1)
						if ("lon" in field.name().lower()) and ("off" in field.name().lower()):
							self.longoffsetcol.setCurrentIndex(self.longoffsetcol.count() - 1)
						

        def browse_outfile(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Frames Directory",
			self.outdirname.displayText())

		if newname != None:
                	self.outdirname.setText(newname)

	def run(self):
		layer = unicode(self.layername.currentText())
		latcol = unicode(self.latoffsetcol.currentText())
		longcol = unicode(self.longoffsetcol.currentText())
		outdir = unicode(self.outdirname.displayText())
		frame_count = int(self.durationframes.displayText())

		message = mmqgis_animate_columns(self.iface, layer, longcol, latcol, outdir, frame_count)
		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Animate Columns", message)

# --------------------------------------------------------
#    mmqgis_animate_lines - Create animations by
#		interpolating offsets from attributes
# --------------------------------------------------------

from mmqgis_animate_lines_form import *

class mmqgis_animate_lines_dialog(QDialog, Ui_mmqgis_animate_lines_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)

		QObject.connect(self.browseoutfile, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		for name, layer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
			if (layer.type() == QgsMapLayer.VectorLayer) and \
			   (layer.wkbType() in [QGis.WKBLineString, QGis.WKBLineString25D, \
			    QGis.WKBMultiLineString, QGis.WKBMultiLineString25D]):
				self.layername.addItem(layer.name())

		self.outdirname.setText(os.getcwd() + "/frames")

        def browse_outfile(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Frames Directory",
			self.outdirname.displayText())

		if newname != None:
                	self.outdirname.setText(newname)

	def run(self):
		layer = unicode(self.layername.currentText())		
		fixed_speed = unicode(self.timing.currentText()) == "One Line Speed Determined By Longest Line"
		frame_count = int(self.durationframes.displayText())
		outdir = unicode(self.outdirname.displayText())

		message = mmqgis_animate_lines(self.iface, layer, fixed_speed, frame_count, outdir)
		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Animate Columns", message)

# --------------------------------------------------------
#    mmqgis_animate_rows - Create animations by
#		displaying successive rows
# --------------------------------------------------------

from mmqgis_animate_rows_form import *

class mmqgis_animate_rows_dialog(QDialog, Ui_mmqgis_animate_rows_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)

		QObject.connect(self.browseoutfile, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		for name, layer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
			if layer.type() == QgsMapLayer.VectorLayer:
				self.layernames.addItem(layer.name())

		self.outdirname.setText(os.getcwd() + "/frames")

        def browse_outfile(self):
		newname = QFileDialog.getExistingDirectory(None, "Output Frames Directory",
			self.outdirname.displayText())

		if newname != None:
                	self.outdirname.setText(newname)

	def run(self):
		layers = []
		for x in range(0, self.layernames.count()):
			if self.layernames.item(x).isSelected():
				layers.append(self.layernames.item(x).text())

		# cumulative = self.cumulative.isChecked()
		outdir = unicode(self.outdirname.displayText())

		message = mmqgis_animate_rows(self.iface, layers, outdir)
		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Animate Rows", message)



# ----------------------------------------------------------
#    mmqgis_attribute_export - Export attributes to CSV file
# ----------------------------------------------------------

from mmqgis_attribute_export_form import *

class mmqgis_attribute_export_dialog(QDialog, Ui_mmqgis_attribute_export_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browseoutfile, SIGNAL("clicked()"), self.browse_outfiles)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.sourcelayer, True)

		QObject.connect(self.sourcelayer, SIGNAL("currentIndexChanged(QString)"), self.set_attributes)
		self.set_attributes()

		self.outfilename.setText(mmqgis_temp_file_name(".csv"))

        def browse_outfiles(self):
		newname = QFileDialog.getSaveFileName(None, "Output CSV File", 
			self.outfilename.displayText(), "CSV File (*.csv *.txt)")
                if newname != None:
                	self.outfilename.setText(newname)

	def set_attributes(self):
		self.attributes.clear()
		layer = mmqgis_find_layer(self.sourcelayer.currentText())
		if (layer == None):
			return

		for field in layer.fields():
			self.attributes.addItem(field.name())

		#print self.locale().name()
		# print QSettings().allKeys()

		#print "Configured locale", QSettings().value("locale/userLocale")
		#print "Self Qt locale", unicode(self.locale().countryToString(self.locale().country()))
		#print "Self Qt decimal point: ", unicode(self.locale().decimalPoint())
		
		# Decimal mark is dependent on locale (comma instead of decimal point in Europe)
		# This doesn't use local override in settings (although it should)
		# Idiot check to make sure it's either a period or comma

		# QGIS configured country codes (locale/userLocale) are not
		# usable with python locale, so just use QLocale from user interface

		if (self.locale().decimalPoint() == '.'):
			self.decimalmark.setCurrentIndex(self.decimalmark.findText("(period)"))
			self.delimiter.setCurrentIndex(self.delimiter.findText("(comma)"))

		else:
			self.decimalmark.setCurrentIndex(self.decimalmark.findText("(comma)"))
			self.delimiter.setCurrentIndex(self.delimiter.findText("(semicolon)"))


		#if (layername[0] != '/') and (layername[0] != '\\'):
		#	self.outfilename.setText(os.getcwd() + "/" + layername + ".csv")
		#else:
		#	self.outfilename.setText(layername + ".csv")

	def run(self):
		layername = unicode(self.sourcelayer.currentText())
		outfilename = unicode(self.outfilename.displayText())

		delimiter = ","
		if unicode(self.delimiter.currentText()) == "(bar)":
			delimiter = "|"
		elif unicode(self.delimiter.currentText()) == "(space)":
			delimiter = " "
		elif unicode(self.delimiter.currentText()) == "(semicolon)":
			delimiter = ";"

		lineterminator = "\r\n"
		if unicode(self.lineterminator.currentText()) == "LF":
			lineterminator = "\n"

		decimal_mark = '.'
		if unicode(self.decimalmark.currentText()) == "(comma)":
			decimal_mark = ','

		# Compile a list and header of selected attributes
		attribute_names = []
		for x in range(0, self.attributes.count()):
			list_item = self.attributes.item(x)
			if list_item.isSelected():
				attribute_names.append(unicode(list_item.text()))

		#if len(attribute_names) <= 0:
		#	QMessageBox.critical(self.iface.mainWindow(), "Attribute Export", "No attributes selected")
		#	return

		message = mmqgis_attribute_export(self.iface, outfilename, layername, \
			attribute_names, delimiter, lineterminator, decimal_mark)

		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Attribute Export", message)

# --------------------------------------------------------
#    mmqgis_attribute_join - Join attributes from a CSV
#                            file to a shapefile
# --------------------------------------------------------

from mmqgis_attribute_join_form import *

class mmqgis_attribute_join_dialog(QDialog, Ui_mmqgis_attribute_join_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browse_infile, SIGNAL("clicked()"), self.browse_infiles)
		QObject.connect(self.browse_outfile, SIGNAL("clicked()"), self.browse_outfiles)
		QObject.connect(self.browse_notfound, SIGNAL("clicked()"), self.browse_notfoundfiles)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.joinlayer, True)

		QObject.connect(self.joinlayer, SIGNAL("currentIndexChanged(QString)"), self.set_join_attributes)
		self.set_join_attributes()

		self.outfilename.setText(mmqgis_temp_file_name(".shp"))
		self.notfoundfilename.setText(os.getcwd() + "/notfound.csv")

        def browse_infiles(self):
		newname = QFileDialog.getOpenFileName(None, "Input CSV File", 
			self.infilename.displayText(), "CSV File (*.csv *.txt)")

                if newname:
			header = mmqgis_read_csv_header(self.iface, newname)
			if not header:
				return

			self.csvfilefield.clear()
			for field in header:
				self.csvfilefield.addItem(field)

			self.infilename.setText(newname)

        def browse_outfiles(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.outfilename.displayText(), "Shapefile (*.shp)")

                if newname != None:
                	self.outfilename.setText(newname)

        def browse_notfoundfiles(self):
		newname = QFileDialog.getSaveFileName(None, "Output Unjoined CSV File", 
			self.notfoundfilename.displayText(), "CSV File (*.csv *.txt)")
                if newname != None:
                	self.notfoundfilename.setText(newname)

	def set_join_attributes(self):
		self.joinlayerattribute.clear()
		layer = mmqgis_find_layer(self.joinlayer.currentText())
		if (layer == None):
			return
		for field in layer.fields().toList():
			self.joinlayerattribute.addItem(field.name())

	def run(self):
		layername = unicode(self.joinlayer.currentText())
		joinfield = unicode(self.csvfilefield.currentText())
		joinattribute = unicode(self.joinlayerattribute.currentText())
		infilename = unicode(self.infilename.displayText())
		outfilename = unicode(self.outfilename.displayText())
		notfoundname = unicode(self.notfoundfilename.displayText()).strip()

		message = mmqgis_attribute_join(self.iface, layername, infilename, joinfield, \
			joinattribute, outfilename, notfoundname, 1)
		if message != None:
			QMessageBox.critical(self.iface.mainWindow(), "Attribute Join", message)

# ---------------------------------------------------------
#    mmqgis_buffers - Create buffer polygons
# ---------------------------------------------------------

from mmqgis_buffers_form import *

# These globals are a kludge to give search term persistence.
# This should probably be implemented in Qt with a static
# dialog and multiple exec(), but that is undocumented behavior
# that might break on Windoze.

mmqgis_buffers_radius = 0.5
mmqgis_buffers_rotation = 0
mmqgis_buffers_edgecount = 4 # rough circle
mmqgis_buffers_radiusunit = 1 # miles

class mmqgis_buffers_dialog(QDialog, Ui_mmqgis_buffers_form):
	def __init__(self, iface):
		global mmqgis_buffers_edges
		global mmqgis_buffers_radius
		global mmqgis_buffers_rotation
		global mmqgis_buffers_radiusunit

		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)

		self.radiusunit.addItems(["Feet", "Miles", "Meters", "Kilometers"])
		self.edgecount.addItems(["3 (Triangle)", "4 (Square)", "5 (Pentagon)", \
				"6 (Hexagon)", "32 (Rough Circle)", "64 (Smooth Circle)"])

		self.radius.setText(unicode(mmqgis_buffers_radius))
		self.rotation.setText(unicode(mmqgis_buffers_rotation))
		self.edgecount.setCurrentIndex(mmqgis_buffers_edgecount)
		self.radiusunit.setCurrentIndex(mmqgis_buffers_radiusunit)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.sourcelayer, True)

		QObject.connect(self.browse, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)
		QObject.connect(self.sourcelayer, SIGNAL("currentIndexChanged(QString)"), self.layer_changed)
		QObject.connect(self.edgeattribute, SIGNAL("currentIndexChanged(QString)"), self.edgeattribute_changed)
		QObject.connect(self.radiusattribute, SIGNAL("currentIndexChanged(QString)"), self.radiusattribute_changed)
		QObject.connect(self.rotationattribute, SIGNAL("currentIndexChanged(QString)"), self.rotationattribute_changed)

		self.layer_changed()

		self.filename.setText(mmqgis_temp_file_name(".shp"))


	def edgeattribute_changed(self):
		self.edgecount.setEnabled(self.edgeattribute.currentText() == "(fixed)")


	def radiusattribute_changed(self):
		self.radius.setEnabled(self.radiusattribute.currentText() == "(fixed)")


	def rotationattribute_changed(self):
		self.rotation.setEnabled(self.rotationattribute.currentText() == "(fixed)")


	def layer_changed(self):
		self.edgeattribute.clear()
		self.radiusattribute.clear()
		self.rotationattribute.clear()

		self.radiusattribute.addItem("(fixed)")
		self.rotationattribute.addItem("(fixed)")

		self.radiusattribute.setCurrentIndex(0)
		self.rotationattribute.setCurrentIndex(0)

		self.radius.setEnabled(True)

		layer = mmqgis_find_layer(unicode(self.sourcelayer.currentText()))
		if (layer == None):
			return

		for field in layer.fields().toList():
			if (field.type() in [QVariant.Double, QVariant.Int, QVariant.UInt, \
					QVariant.LongLong, QVariant.ULongLong]):
				self.radiusattribute.addItem(field.name())
				self.rotationattribute.addItem(field.name())


		if (layer.wkbType() in [QGis.WKBPoint, QGis.WKBPoint25D, QGis.WKBMultiPoint, QGis.WKBMultiPoint25D]):
			self.rotation.setEnabled(True)
			self.edgecount.setEnabled(True)
			self.rotationattribute.setEnabled(True)

			self.edgeattribute.addItem("(fixed)")

			for field in layer.fields().toList():
				if (field.type() in [QVariant.Double, QVariant.Int, QVariant.UInt, \
						QVariant.LongLong, QVariant.ULongLong]):
					self.edgeattribute.addItem(field.name())


		elif (layer.wkbType() in [QGis.WKBLineString, QGis.WKBLineString25D, \
		      QGis.WKBMultiLineString, QGis.WKBMultiLineString25D]):

			self.rotation.setEnabled(False)
			self.edgecount.setEnabled(False)
			self.rotationattribute.setEnabled(False)

			self.edgeattribute.addItems(["Rounded", "Flat End", "North Side", \
				"East Side", "South Side", "West Side"])

		else:
			self.rotation.setEnabled(False)
			self.edgecount.setEnabled(False)
			self.rotationattribute.setEnabled(False)

			self.edgeattribute.addItems(["Rounded"])

		self.edgeattribute.setCurrentIndex(0)


        def browse_outfile(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.filename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.filename.setText(newname)

	def run(self):
		global mmqgis_buffers_radius
		global mmqgis_buffers_rotation
		global mmqgis_buffers_edgecount
		global mmqgis_buffers_radiusunit

		# Radius
		radius_attribute = self.radiusattribute.currentText()
		if (radius_attribute == "(fixed)"):
			radius_attribute = None

		try:
			mmqgis_buffers_radius = float(self.radius.displayText())
		except:
			QMessageBox.critical(self.iface.mainWindow(), "Create Buffers", 
				"Invalid radius number format: " + unicode(self.radius.displayText()))
			return None

		mmqgis_buffers_radiusunit = self.radiusunit.currentIndex()
		radius_unit = unicode(self.radiusunit.currentText())

		# Shape / Edges
		edge_attribute = self.edgeattribute.currentText()
		if (edge_attribute == "(fixed)"):
			edge_attribute = None

		edge_count = int(self.edgecount.currentText()[0:2])
		mmqgis_buffers_edgecount = self.edgecount.currentIndex()

		# Rotation
		rotation_attribute = self.rotationattribute.currentText()
		if (rotation_attribute == "(fixed)"):
			rotation_attribute = None

		try:
			mmqgis_buffers_rotation = float(self.rotation.displayText())
		except:
			QMessageBox.critical(self.iface.mainWindow(), "Create Buffers", 
				"Invalid rotation number format: " + unicode(self.rotation.displayText()))
			return None

		layername = unicode(self.sourcelayer.currentText())

		selectedonly = self.selectedonly.isChecked()

		savename = unicode(self.filename.displayText()).strip()

		message = mmqgis_buffers(self.iface, layername, radius_attribute, mmqgis_buffers_radius, radius_unit, \
			edge_attribute, edge_count, rotation_attribute, mmqgis_buffers_rotation, \
			savename, selectedonly, True)

		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Create Buffers", message)





# --------------------------------------------------------
#    mmqgis_delete_duplicate_geometries - Save to shaperile
#			while removing duplicate shapes
# --------------------------------------------------------

from mmqgis_delete_duplicate_form import *

class mmqgis_delete_duplicate_dialog(QDialog, Ui_mmqgis_delete_duplicate_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browse, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.sourcelayer, True)

		self.filename.setText(mmqgis_temp_file_name(".shp"))

        def browse_outfile(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.filename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.filename.setText(newname)

	def run(self):
		savename = unicode(self.filename.displayText()).strip()
		layername = unicode(self.sourcelayer.currentText())

		message = mmqgis_delete_duplicate_geometries(self.iface, layername, savename, 1)
		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Delete Duplicate Geometries", message)

# ---------------------------------------------------------
#    mmqgis_float_to_text - Change text fields to numbers
# ---------------------------------------------------------

from mmqgis_float_to_text_form import *

class mmqgis_float_to_text_dialog(QDialog, Ui_mmqgis_float_to_text_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browse, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.sourcelayer, True)

		QObject.connect(self.sourcelayer, SIGNAL("currentIndexChanged(QString)"), self.set_fieldnames)

		self.set_fieldnames()

		self.filename.setText(mmqgis_temp_file_name(".shp"))

        def browse_outfile(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.filename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.filename.setText(newname)

	def set_fieldnames(self):
		self.fieldnames.clear()
		layer = mmqgis_find_layer(self.sourcelayer.currentText())
		if (layer == None):
			return

		for field in layer.fields().toList():
			if (field.type() in [QVariant.Double, QVariant.Int, QVariant.UInt, \
						QVariant.LongLong, QVariant.ULongLong]):
				self.fieldnames.addItem(field.name())
				self.fieldnames.item(self.fieldnames.count() - 1).setSelected(1)

	def run(self):
		layername = unicode(self.sourcelayer.currentText())
		savename = unicode(self.filename.displayText()).strip()

		if unicode(self.separator.currentText()) == "Comma":
			separator = ','
		elif unicode(self.separator.currentText()) == "Space":
			separator = ' '
		else:
			separator = None

		decimals = self.decimals.currentIndex()
		prefix = unicode(self.prefix.text())
		suffix = unicode(self.suffix.text())

		attributes = []
		for x in range(0, self.fieldnames.count()):
			if self.fieldnames.item(x).isSelected():
				attributes.append(self.fieldnames.item(x).text())

		message = mmqgis_float_to_text(self.iface, layername, attributes, separator, 
			decimals, prefix, suffix, savename, 1)
		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Float to Text", message)


# --------------------------------------------------------
#    mmqgis_geometry_convert - Convert geometries to
#		simpler types
# --------------------------------------------------------

from mmqgis_geometry_convert_form import *

class mmqgis_geometry_convert_dialog(QDialog, Ui_mmqgis_geometry_convert_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browse, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.sourcelayer, True)

		self.mergeattop.addItems(["First", "Sum"])

		QObject.connect(self.sourcelayer, SIGNAL("currentIndexChanged(QString)"), self.set_geometry_types)
		QObject.connect(self.newgeometry, SIGNAL("currentIndexChanged(QString)"), self.set_merge_fields)

		self.set_geometry_types()

		self.filename.setText(mmqgis_temp_file_name(".shp"))

        def browse_outfile(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.filename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.filename.setText(newname)

	def set_geometry_types(self):
		newtypes = []
		layername = self.sourcelayer.currentText()
		for name, layer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
			# print layername + " =? " + layer.name() + ": " + str(layer.dataProvider().geometryType())

			if layer.name() == layername:
				if layer.wkbType() == QGis.WKBPoint:
					self.oldgeometry.setText("Type: Point")
					newtypes = ["Multipoints"]

				elif layer.wkbType() == QGis.WKBPoint25D:
					self.oldgeometry.setText("Type: Point 2.5D")
					newtypes = ["Points", "Multipoints"]

				elif layer.wkbType() == QGis.WKBLineString:
					self.oldgeometry.setText("Type: Lines")
					# Multi-linestring layers have a geometry type of WKBLineString,
					# so a linestring option must be provided and no
					# multilinestring option is possible
					newtypes = ["Line Centers", "Centroids", "Nodes", "Lines", "Multilines"]

				elif layer.wkbType() == QGis.WKBLineString25D:
					self.oldgeometry.setText("Type: Linestring 2.5D")
					newtypes = ["Line Centers", "Centroids", "Nodes", "Lines", "Multilines"]

				elif layer.wkbType() == QGis.WKBPolygon:
					self.oldgeometry.setText("Type: Polygon")
					newtypes = ["Centroids", "Nodes", "Lines", "Multilines", \
						"Polygons", "Multipolygons"] 

				elif layer.wkbType() == QGis.WKBPolygon25D:
					self.oldgeometry.setText("Type: Polygon 2.5D")
					newtypes = ["Centroids", "Nodes", "Lines", "Multilines", \
						"Polygons", "Multipolygons"]

				elif layer.wkbType() == QGis.WKBMultiPoint:
					self.oldgeometry.setText("Type: Multipoint")
					newtypes = ["Points", "Centroids"]

				elif layer.wkbType() == QGis.WKBMultiPoint25D:
					self.oldgeometry.setText("Type: Multipoint 2.5D")
					newtypes = ["Points", "Centroids"]

				elif layer.wkbType() == QGis.WKBMultiLineString:
					self.oldgeometry.setText("Type: Multilines")
					newtypes = ["Line Centers", "Centroids", "Nodes", "Lines"]

				elif layer.wkbType() == QGis.WKBMultiLineString25D:
					self.oldgeometry.setText("Type: Multilines 2.5D")
					newtypes = ["Line Centers", "Centroids", "Nodes", "Lines", "Multilines"]

				elif layer.wkbType() == QGis.WKBMultiPolygon:
					self.oldgeometry.setText("Type: Multipolygons")
					newtypes = ["Centroids", "Nodes", "Lines", "Multilines", "Polygons"] 

				elif layer.wkbType() == QGis.WKBMultiPolygon25D:
					self.oldgeometry.setText("Type: Multipolygons 2.5D")
					newtypes = ["Centroids", "Nodes", "Lines", "Multilines", "Polygons", "Multipolygons"]

		self.newgeometry.clear()
		self.newgeometry.addItems(newtypes)
		self.set_merge_fields()

	def set_merge_fields(self):
		self.mergefield.clear()
		layer = mmqgis_find_layer(self.sourcelayer.currentText())
		if (layer == None):
			return

		oldgeometry = layer.wkbType()
		newgeometry = self.newgeometry.currentText()

		if ((oldgeometry == QGis.WKBPoint) and (newgeometry == "Multipoints")) or \
		   ((oldgeometry == QGis.WKBPoint25D) and (newgeometry == "Multipoints")) or \
		   ((oldgeometry == QGis.WKBLineString) and (newgeometry == "Multilines")) or \
		   ((oldgeometry == QGis.WKBLineString25D) and (newgeometry == "Multilines")) or \
		   ((oldgeometry == QGis.WKBPolygon) and (newgeometry == "Multipolygons")) or \
		   ((oldgeometry == QGis.WKBPolygon25D) and (newgeometry == "Multipolygons")):
			self.mergefield.clear()
			for field in layer.fields().toList():
				self.mergefield.addItem(field.name())
			self.mergefield.setEnabled(True)
			self.mergeattop.setEnabled(True)

		else:
			self.mergefield.clear()
			self.mergefield.setEnabled(False)
			self.mergeattop.setEnabled(False)
		
	def run(self):
		savename = unicode(self.filename.displayText()).strip()
		layername = unicode(self.sourcelayer.currentText())
		newtype = unicode(self.newgeometry.currentText())

		if self.mergefield.isEnabled():
			mergefield = unicode(self.mergefield.currentText())
			mergeattop = unicode(self.mergeattop.currentText())
			message = mmqgis_geometry_to_multipart(self.iface, layername, mergefield, mergeattop, savename, 1)

		else:
			message = mmqgis_geometry_convert(self.iface, layername, newtype, savename, 1)

		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Label", message)


# --------------------------------------------------------
#    mmqgis_geometry_export - Import geometries from a
#			CSV files of nodes and attributes
#			into a shapefile
# --------------------------------------------------------

from mmqgis_geometry_export_form import *

class mmqgis_geometry_export_dialog(QDialog, Ui_mmqgis_geometry_export_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.nodebrowse, SIGNAL("clicked()"), self.browse_nodes)
		QObject.connect(self.attbrowse, SIGNAL("clicked()"), self.browse_attributes)
		QObject.connect(self.sourcelayer, SIGNAL("currentIndexChanged(QString)"), self.check_layer_type)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.sourcelayer, True)

		self.attfilename.setText(os.getcwd() + "/temp-attributes.csv")
		self.nodefilename.setText(os.getcwd() + "/temp-nodes.csv")

        def browse_nodes(self):
		newname = QFileDialog.getSaveFileName(None, "Output Nodes CSV File", 
			self.nodefilename.displayText(), "CSV File (*.csv *.txt)")

		if newname != None:
                	self.nodefilename.setText(newname)

        def browse_attributes(self):
		newname = QFileDialog.getSaveFileName(None, "Output Nodes CSV File", 
			self.attfilename.displayText(), "CSV File (*.csv *.txt)")

		if newname != None:
                	self.attfilename.setText(newname)

	def check_layer_type(self):
		layer = mmqgis_find_layer(self.sourcelayer.currentText())
		if (layer != None) and (layer.type() == QgsMapLayer.VectorLayer):
			if (layer.geometryType() == QGis.Point):
				self.attbrowse.setEnabled(False)
				self.attfilename.setEnabled(False)
			else:
				self.attbrowse.setEnabled(True)
				self.attfilename.setEnabled(True)

	def run(self):
		delimiter = ","
		if unicode(self.delimiter.currentText()) == "(bar)":
			delimiter = "|"
		elif unicode(self.delimiter.currentText()) == "(space)":
			delimiter = " "

		lineterminator = "\r\n"
		if unicode(self.lineterminator.currentText()) == "LF":
			lineterminator = "\n"

		sourcelayer = self.sourcelayer.currentText()
		nodefilename = self.nodefilename.displayText()
		attributefilename = self.attfilename.displayText()

		message = mmqgis_geometry_export_to_csv(self.iface, sourcelayer, nodefilename, 
			attributefilename, delimiter, lineterminator)
		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Geometry Export", message)


# --------------------------------------------------------
#    mmqgis_geometry_import - Import geometries from a
#			CSV files of nodes and attributes
#			into a shapefile
# --------------------------------------------------------

from mmqgis_geometry_import_form import *

class mmqgis_geometry_import_dialog(QDialog, Ui_mmqgis_geometry_import_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.nodebrowse, SIGNAL("clicked()"), self.browse_nodes)
		QObject.connect(self.outfilebrowse, SIGNAL("clicked()"), self.browse_shapefile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		self.geometrytype.addItem("Point")
		self.geometrytype.addItem("Polyline")
		self.geometrytype.addItem("Polygon")

		self.outfilename.setText(mmqgis_temp_file_name(".shp"))

	def browse_nodes(self):
		newname = QFileDialog.getOpenFileName(None, "Input Nodes CSV File", 
			self.nodefilename.displayText(), "CSV File (*.csv *.txt)")

                if not newname:
			return

		header = mmqgis_read_csv_header(self.iface, newname)
		if not header:
			return

		self.longcol.clear()
		self.latcol.clear()
		self.shapeidcol.clear()
		for field in header:
			self.longcol.addItem(field)
			self.latcol.addItem(field)
			self.shapeidcol.addItem(field)

		for x in range(0, len(header)):
			if (header[x].lower() == "shapeid") or (header[x].lower() == 'shape_id'):
				self.shapeidcol.setCurrentIndex(x)
				break

		for x in range(0, len(header)):
			if (header[x].find("x") >= 0) or (header[x].find("X") >= 0) or (header[x].lower().find('lon') >= 0):
				self.longcol.setCurrentIndex(x)
				break

		for x in range(0, len(header)):
			if (header[x].find("y") >= 0) or (header[x].find("Y") >= 0) or (header[x].lower().find('lat') >= 0):
				self.latcol.setCurrentIndex(x)
				break


		#for x in range(self.shapeidcol.count()):
		#	if (unicode(self.shapeidcol.itemText(x)).lower() == "shapeid") or \
		#	   (unicode(self.shapeidcol.itemText(x)).lower() == "shape_id"):
		#		self.shapeidcol.setCurrentIndex(x)

		#for x in range(self.longcol.count()):
		#	if (unicode(self.longcol.itemText(x)).lower() == "x") or \
		#	   (unicode(self.longcol.itemText(x)).lower()[0:3] == "lon"):
		#		self.longcol.setCurrentIndex(x)

		#for x in range(self.latcol.count()):
		#	if (unicode(self.latcol.itemText(x)).lower() == "x") or \
		#	   (unicode(self.latcol.itemText(x)).lower()[0:3] == "lon"):
		#		self.latcol.setCurrentIndex(x)

		self.nodefilename.setText(newname)
		shapename = str(newname) # make copy or replace alters original
		shapename = shapename.replace(".csv", ".shp")
		shapename = shapename.replace(".CSV", ".shp")
		shapename = shapename.replace(".txt", ".shp")
		shapename = shapename.replace(".TXT", ".shp")
		if shapename == newname:
			shapename = unicode(shapename) + ".shp"
		self.outfilename.setText(shapename)


        def browse_shapefile(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.outfilename.displayText(), "Shapefile (*.shp)")

                if newname != None:
                	self.outfilename.setText(newname)

	def run(self):
		message = mmqgis_geometry_import_from_csv(self.iface, unicode(self.nodefilename.displayText()), 
			unicode(self.longcol.currentText()), unicode(self.latcol.currentText()),
			unicode(self.shapeidcol.currentText()), unicode(self.geometrytype.currentText()),
			unicode(self.outfilename.displayText()), 1)

		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Geometry Import", message)


# --------------------------------------------------------
#    mmqgis_geocode_web_service - Geocode using 
#	Google Maps or Nominatim
# --------------------------------------------------------

from mmqgis_geocode_web_service_form import *

#pyqt4-dev-tools
#designer

class mmqgis_geocode_web_service_dialog(QDialog, Ui_mmqgis_geocode_web_service_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browse_infile, SIGNAL("clicked()"), self.browse_infile_dialog)
		QObject.connect(self.browse_shapefile, SIGNAL("clicked()"), self.browse_shapefile_dialog)
		QObject.connect(self.browse_notfound, SIGNAL("clicked()"), self.browse_notfound_dialog)
		QObject.connect(self.servicename, SIGNAL("currentIndexChanged(QString)"), self.servicename_changed)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		self.apikey.setText("(none)")
		self.shapefilename.setText(mmqgis_temp_file_name(".shp"))
		self.notfoundfilename.setText(os.getcwd() + "/notfound.csv")

		self.servicename.clear()
		self.servicename.addItems(["Google Maps", "OpenStreetMap / Nominatim"])
		self.servicename.setCurrentIndex(0)

	def servicename_changed(self, service):
		self.apikey.setEnabled(service == "Google Maps")

        def browse_infile_dialog(self):
		newname = QFileDialog.getOpenFileName(None, "Address CSV Input File", 
			self.infilename.displayText(), "CSV File (*.csv *.txt)")

                if newname:

			if len(newname) > 4:
				prefix = newname[:len(newname) - 4]
				self.shapefilename.setText(prefix + ".shp")
			else:
				self.shapefilename.setText(mmqgis_temp_file_name(".shp"))


			combolist = [self.addressfield, self.cityfield, self.statefield, self.countryfield]
			for box in combolist:
				box.clear()
				box.addItem("(none)")
				box.setCurrentIndex(0)
				
			header = mmqgis_read_csv_header(self.iface, newname)
			if header == None:
				return

			for index in range(0, len(header)):
				field = header[index]
				for box in combolist:
					box.addItem(field)

				if field.lower().find("addr") >= 0:
					self.addressfield.setCurrentIndex(index + 1)
				if field.lower().find("street") >= 0:
					self.addressfield.setCurrentIndex(index + 1)
				if field.lower().find("city") >= 0:
					self.cityfield.setCurrentIndex(index + 1)
				if field.lower().find("state") >= 0:
					self.statefield.setCurrentIndex(index + 1)
				if field.lower() == "st":
					self.statefield.setCurrentIndex(index + 1)
				if field.lower().find("province") >= 0:
					self.statefield.setCurrentIndex(index + 1)
				if field.lower().find("country") >= 0:
					self.countryfield.setCurrentIndex(index + 1)

                	self.infilename.setText(newname)

        def browse_notfound_dialog(self):
		newname = QFileDialog.getSaveFileName(None, "Not Found List Output File", 
			self.notfoundfilename.displayText(), "CSV File (*.csv *.txt)")
                if newname != None:
                	self.notfoundfilename.setText(newname)

        def browse_shapefile_dialog(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.shapefilename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.shapefilename.setText(newname)

	def run(self):
		apikey = unicode(self.apikey.displayText()).strip()
		csvname = unicode(self.infilename.displayText()).strip()
		service = unicode(self.servicename.currentText()).strip()
		notfoundfile = self.notfoundfilename.displayText()
		shapefilename = unicode(self.shapefilename.displayText())

		fields = [unicode(self.addressfield.currentText()).strip(),
			  unicode(self.cityfield.currentText()).strip(),
			  unicode(self.statefield.currentText()).strip(),
			  unicode(self.countryfield.currentText()).strip()]
	
		for x in range(0, len(fields)):
			if fields[x] == "(none)":
				fields[x] = ""

		if (apikey == "(none)") or (apikey == ""):
			apikey = None

		# print csvname + "," + "," + shapefilename
		message = mmqgis_geocode_web_service(self.iface, csvname, 
			shapefilename, notfoundfile, fields, service, apikey, 1)

		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Web Service Geocode", message)

# --------------------------------------------------------
#    mmqgis_grid - Grid creation plugin
# --------------------------------------------------------

from mmqgis_grid_form import *

class mmqgis_grid_dialog(QDialog, Ui_mmqgis_grid_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)

		self.extenttype.addItems(["Current Window", "Layer Extent", "Whole World", "Custom Area"])
		self.shapetype.addItems(["Lines", "Rectangles", "Points", "Random Points", "Diamonds", "Hexagons"])

		self.units.addItems(["Degrees", "Layer Units", "Project Units"])
		self.current_crs = None

		self.wgs84 = QgsCoordinateReferenceSystem()
		self.wgs84.createFromProj4("+proj=longlat +datum=WGS84 +no_defs")

		for name, layer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
			self.layername.addItem(layer.name())

		QObject.connect(self.units, SIGNAL("currentIndexChanged(QString)"), self.units_changed)
		QObject.connect(self.xspacing, SIGNAL("textEdited(QString)"), self.xspacing_changed)
		QObject.connect(self.yspacing, SIGNAL("textEdited(QString)"), self.yspacing_changed)
		QObject.connect(self.shapetype, SIGNAL("currentIndexChanged(QString)"), self.shapetype_changed)
		QObject.connect(self.layername, SIGNAL("currentIndexChanged(QString)"), self.layer_changed)
		QObject.connect(self.extenttype, SIGNAL("currentIndexChanged(QString)"), self.extenttype_changed)

		self.units.setCurrentIndex(0);
		self.shapetype.setCurrentIndex(0);
		self.extenttype.setCurrentIndex(0);
		self.extenttype_changed("Current Window")

		self.savename.setText(os.getcwd() + "/grid.shp")
		QObject.connect(self.browse, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)


	def set_extent(self, extent, enable):
		self.ytop.setText(unicode(extent.yMaximum()))
		self.xleft.setText(unicode(extent.xMinimum()))
		self.xright.setText(unicode(extent.xMaximum()))
		self.ybottom.setText(unicode(extent.yMinimum()))

		self.ytop.setEnabled(enable)
		self.xleft.setEnabled(enable)
		self.xright.setEnabled(enable)
		self.ybottom.setEnabled(enable)

		self.set_default_spacing()

	def set_default_spacing(self):
		try:
			width = float(self.xright.displayText()) - float(self.xleft.displayText())
			height = float(self.ytop.displayText()) - float(self.ybottom.displayText())
		except:
			width = 1
			height = 1

		if (width <= 0):
			width = 1
		if (height <= 0):
			height = 1

		x = 10 ** (math.floor(math.log(width, 10)) - 1)
		y = 10 ** (math.floor(math.log(height, 10)) - 1)

		if self.shapetype.currentText() == "Hexagons":
			y = x / 0.866025

		self.xspacing.setText(unicode(x))
		self.yspacing.setText(unicode(y))


	def layer_changed(self, text):
		if (self.extenttype.currentText() == "Layer Extent"):
			self.extenttype_changed(self.extenttype.currentText())
		else:
			self.units_changed(self.units.currentText())


	def extenttype_changed(self, text):
		if (text == "Current Window"):

			self.units.setCurrentIndex(2)
			self.current_crs = self.iface.mapCanvas().mapRenderer().destinationCrs()
			self.set_extent(self.iface.mapCanvas().mapRenderer().extent(), False)
			
		elif (text == "Layer Extent"):

			layer = mmqgis_find_layer(self.layername.currentText())
			if layer == None:
				return

			self.units.setCurrentIndex(1)
			self.current_crs = layer.crs()
			self.set_extent(layer.extent(), False)
			self.layername.setEnabled(True)

 		elif (text == "Custom Area"):

			self.ytop.setEnabled(True)
			self.xleft.setEnabled(True)
			self.xright.setEnabled(True)
			self.ybottom.setEnabled(True)

			if (self.units.currentText() != "Layer Units"):
				self.layername.setEnabled(False)

		else: # "Whole World"

			self.units.setCurrentIndex(0)
			self.current_crs = self.wgs84
			self.set_extent(QgsRectangle(-180, -90, 180, 90), False)

			if (self.units.currentText() != "Layer Units"):
				self.layername.setEnabled(False)


	def shapetype_changed(self, text):
		if unicode(self.shapetype.currentText()) == "Hexagons":
			try:
				yspacing = float(self.yspacing.displayText())
				self.xspacing.setText(unicode(yspacing * 0.866025403784439))
			except:
				self.set_default_spacing()

	def yspacing_changed(self, text):
		# Hexagonal grid must maintain fixed aspect ratio to make sense
		if unicode(self.shapetype.currentText()) == "Hexagons":
			yspacing = float(text)
			self.xspacing.setText(unicode(yspacing * 0.866025403784439))

	def xspacing_changed(self, text):
		if unicode(self.shapetype.currentText()) == "Hexagons":
			xspacing = float(text)
			self.yspacing.setText(unicode(xspacing / 0.866025))

	def units_changed(self, text):

		# Choose the appropriate CRS for the new units

		past_crs = self.current_crs

		if (text == "Layer Units"):
			layer = mmqgis_find_layer(unicode(self.layername.currentText()))
			if (layer == None):
				self.current_crs = self.wgs84
			else:
				self.current_crs = layer.crs()

			self.layername.setEnabled(True)
				
		elif (text == "Project Units"):
			self.current_crs = self.iface.mapCanvas().mapRenderer().destinationCrs()
			self.layername.setEnabled(self.extenttype.currentText() == "Layer Extent")

		else:
			self.current_crs = self.wgs84
			self.layername.setEnabled(self.extenttype.currentText() == "Layer Extent")


		# Initialization = no conversion necessary
		if not past_crs:
			return

		# Convert the extent to the new units

		try:
			extent = QgsGeometry.fromRect(QgsRectangle( \
				float(self.xleft.displayText()), float(self.ybottom.displayText()), \
				float(self.xright.displayText()), float(self.ytop.displayText())))
		except:
			extent = QgsGeometry.fromRect(QgsRectangle(-180, -90, 180, 90))

		extent.transform(QgsCoordinateTransform(past_crs, self.current_crs))

		# Set the extent text boxes and base a new spacing on that

		self.set_extent(extent.boundingBox(), (self.extenttype.currentText() == "Custom Area"))

		self.set_default_spacing()


        def browse_outfile(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.savename.displayText(), "Shapefile (*.shp)")

                if newname != None:
                	self.savename.setText(newname)

	def run(self):
		try:
			xspacing = float(self.xspacing.displayText())
			yspacing = float(self.yspacing.displayText())
			
			ytop = float(self.ytop.displayText())
			xleft = float(self.xleft.displayText())
			xright = float(self.xright.displayText())
			ybottom = float(self.ybottom.displayText())
		except:
			QMessageBox.critical(self.iface.mainWindow(), "Grid", "Invalid dimension parameter")
			return

		units = self.units.currentText()
		savename = unicode(self.savename.displayText()).strip()
		shapetype = self.shapetype.currentText()
		extenttype = self.extenttype.currentText()

		# Hexagons must have a fixed aspect ratio to align
		if (shapetype == "Hexagons"):
			yspacing = xspacing / 0.866025

		# Align extent on even spacing boundaries so numbers look better
		if (extenttype in ["Current Window", "Layer Extent"]):
			xleft = xspacing * floor(xleft / xspacing)
			xright = xspacing * ceil(xright / xspacing)
			ybottom = yspacing * floor(ybottom / yspacing)
			ytop = yspacing * ceil(ytop / yspacing)
			

		layer_name = unicode(self.layername.currentText())
		layer = mmqgis_find_layer(layer_name)

		if (units == "Project Units"):
			crs = self.iface.mapCanvas().mapRenderer().destinationCrs()

		elif (units == "Layer Units"):
			if (layer == None):
				QMessageBox.critical(self.iface.mainWindow(), "Grid", "No Layer Selected")
				return
			crs = layer.crs()

		else:
			crs = self.wgs84

		message = mmqgis_grid(self.iface, shapetype, crs, xspacing, yspacing, \
				xleft, ybottom, xright, ytop, layer_name, savename, True)

		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Grid", message)



# --------------------------------------------------------
#    mmqgis_gridify - Snap shape verticies to grid
# --------------------------------------------------------

from mmqgis_gridify_form import *

class mmqgis_gridify_dialog(QDialog, Ui_mmqgis_gridify_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browse, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.sourcelayer, True)

		QObject.connect(self.sourcelayer, SIGNAL("currentIndexChanged(int)"), self.layer_changed)
		
		self.filename.setText(mmqgis_temp_file_name(".shp"))
		

        def browse_outfile(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.filename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.filename.setText(newname)

	def layer_changed(self):
		layer = mmqgis_find_layer(unicode(self.sourcelayer.currentText()))
		if (layer == None):
			return

		extent = QgsRectangle (-180.0, -90.0, 180.0, 90.0)
		if (layer):
			extent = layer.extent()

		#if (self.iface.mapCanvas() != None) and (self.iface.mapCanvas().mapRenderer() != None):
		#	extent = self.iface.mapCanvas().mapRenderer().extent()
		#elif self.iface.activeLayer():
		#	extent = self.iface.activeLayer().extent()

		self.hspacing.setText(unicode(extent.width() / 200))
		self.vspacing.setText(unicode(extent.height() / 200))

	def run(self):
		layername = unicode(self.sourcelayer.currentText()).strip()
		savename = unicode(self.filename.displayText()).strip()
		try:
			hspacing = float(self.hspacing.displayText())
			vspacing = float(self.vspacing.displayText())
		except:
			QMessageBox.critical(self.iface.mainWindow(), "Gridify", "Invalid spacing parameter")
			return

		message = mmqgis_gridify_layer(self.iface, layername, hspacing, vspacing, savename, 1)
		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Gridify", message)


# --------------------------------------------------------
#    mmqgis_hub_distance - Create shapefile of distances
#			   from points to nearest hub
# --------------------------------------------------------

from mmqgis_hub_distance_form import *

class mmqgis_hub_distance_dialog(QDialog, Ui_mmqgis_hub_distance_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browse, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		#for name, layer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
		#	if layer.type() == QgsMapLayer.VectorLayer:
		#		self.sourcelayerbox.addItem(layer.name())
		#		self.hubslayerbox.addItem(layer.name())

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.sourcelayerbox, False)
		mmqgis_load_combo_box_with_vector_layers(self.iface, self.hubslayerbox, False)

		if self.hubslayerbox.count() > 1:
			self.hubslayerbox.setCurrentIndex(1)

		QObject.connect(self.hubslayerbox, SIGNAL("currentIndexChanged(QString)"), self.set_name_attributes)

		self.set_name_attributes()

		self.outputtype.addItems(["Line to Hub", "Point"])

		self.measurement.addItems(["Layer Units", "Meters", "Feet", "Miles", "Kilometers"])
		# self.measurement.setEnabled(False)
	
		self.filename.setText(mmqgis_temp_file_name(".shp"))

        def browse_outfile(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.filename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.filename.setText(newname)

	def set_name_attributes(self):
		self.nameattributebox.clear()
		layer = mmqgis_find_layer(self.hubslayerbox.currentText())
		if (layer == None):
			return
		for field in layer.fields().toList():
			self.nameattributebox.addItem(field.name())

	def run(self):
		sourcename = unicode(self.sourcelayerbox.currentText())
		destname = unicode(self.hubslayerbox.currentText())
		nameattributename = unicode(self.nameattributebox.currentText())
		units = unicode(self.measurement.currentText())
		addlines = (self.outputtype.currentText() == "Line to Hub")
		savename = unicode(self.filename.displayText()).strip()
		evenly_distributed = self.distribute.isChecked()

		message = mmqgis_hub_distance(self.iface, sourcename, destname, \
			nameattributename, units, addlines, savename, evenly_distributed, 1)

		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Hub Distance", message)


# --------------------------------------------------------
#    mmqgis_hub_lines - Create shapefile of lines from
#			spoke points to matching hubs
# --------------------------------------------------------

from mmqgis_hub_lines_form import *

class mmqgis_hub_lines_dialog(QDialog, Ui_mmqgis_hub_lines_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browse, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		for name, layer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
			if layer.type() == QgsMapLayer.VectorLayer:
				self.hublayer.addItem(layer.name())
				self.spokelayer.addItem(layer.name())

		QObject.connect(self.hublayer, SIGNAL("currentIndexChanged(QString)"), self.set_hub_attributes)
		QObject.connect(self.spokelayer, SIGNAL("currentIndexChanged(QString)"), self.set_spoke_attributes)

		self.set_hub_attributes(self.hublayer.currentText())
		self.set_spoke_attributes(self.spokelayer.currentText())

		self.filename.setText(mmqgis_temp_file_name(".shp"))

        def browse_outfile(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.filename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.filename.setText(newname)

	def set_hub_attributes(self, layername):
		self.hubid.clear()
		layer = mmqgis_find_layer(layername)
		if (layer == None):
			return
		for field in layer.fields().toList():
			self.hubid.addItem(field.name())

	def set_spoke_attributes(self, layername):
		self.spokehubid.clear()
		layer = mmqgis_find_layer(layername)
		if (layer == None):
			return
		for field in layer.fields().toList():
			self.spokehubid.addItem(field.name())

	def run(self):
		hubname = unicode(self.hublayer.currentText())
		hubattr = unicode(self.hubid.currentText())
		spokename = unicode(self.spokelayer.currentText())
		spokeattr = unicode(self.spokehubid.currentText())
		savename = unicode(self.filename.displayText()).strip()
			
		message = mmqgis_hub_lines(self.iface, hubname, hubattr, spokename, spokeattr, savename, 1)
		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Hub Lines", message)


# ----------------------------------------------------------
#    mmqgis_kml_export - Export attributes to KML file
#			 suitable for display in Google Maps
# ----------------------------------------------------------

from mmqgis_kml_export_form import *

# These globals are a kludge to give kml description persistence
# so time spent typing in a complex description is not lost if
# there is an error

mmqgis_kml_export_layername = ""
mmqgis_kml_export_description = ""

class mmqgis_kml_export_dialog(QDialog, Ui_mmqgis_kml_export_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browseoutfile, SIGNAL("clicked()"), self.browse_outfiles)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		global mmqgis_kml_export_layername
		global mmqgis_kml_export_description

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.sourcelayer, mmqgis_kml_export_layername)

		self.separator.addItems([ 'Field Names', 'Paragraphs', 'Commas', 'Custom HTML'])

		QObject.connect(self.sourcelayer, SIGNAL("currentIndexChanged(QString)"), self.change_layer)
		QObject.connect(self.separator, SIGNAL("currentIndexChanged(QString)"), self.change_description)

		if (self.sourcelayer.currentText() == mmqgis_kml_export_layername) and (mmqgis_kml_export_description <> ""):
			self.set_namefield()
			self.separator.setCurrentIndex(3)
			self.description.setPlainText(mmqgis_kml_export_description)
			self.description.setEnabled(True)
		else:
			self.change_layer()

		self.exportdata.setChecked(True)

		self.outfilename.setText(mmqgis_temp_file_name(".kml"))

        def browse_outfiles(self):
		newname = QFileDialog.getSaveFileName(None, "Output KML File", 
			self.outfilename.displayText(), "KML File (*.kml *.xml)")
                if newname != None:
                	self.outfilename.setText(newname)

	def change_layer(self):
		self.set_namefield()
		self.separator.setCurrentIndex(0)
		self.change_description()

	def set_namefield(self):
		layer = mmqgis_find_layer(self.sourcelayer.currentText())
		if layer == None:
			return

		self.namefield.clear()
		for index, field in enumerate(layer.fields()):
			self.namefield.addItem(field.name())

		self.namefield.setCurrentIndex(0)


	def change_description(self):
		layer = mmqgis_find_layer(self.sourcelayer.currentText())
		if layer == None:
			return

		if (self.separator.currentText() == 'Custom HTML'):
			self.description.setEnabled(True)
			return

		description = ""
		self.description.setEnabled(False)
		for index, field in enumerate(layer.fields()):
			if (self.separator.currentText() == 'Commas'):

				if (index == 0):
					description = "<p>"
				else:
					description = description + ', '

				description = description + '{{' + field.name() + '}}'

				if (index == (len(layer.fields()) - 1)):
					description = description + "</p>"


			elif (self.separator.currentText() == 'Paragraphs'):

				description = description + '<p>{{' + field.name() + '}}</p>\n'

			else: # Field Names

				if (index == 0):
					description = "<p>"
				else:
					description = description + '\n<br/>'

				description = description + field.name() + ': {{' + field.name() + '}}'

				if (index == (len(layer.fields()) - 1)):
					description = description + "</p>"

		self.description.setPlainText(description)


	def run(self):
		global mmqgis_kml_export_layername
		global mmqgis_kml_export_description

		mmqgis_kml_export_layername = unicode(self.sourcelayer.currentText())
		mmqgis_kml_export_description = unicode(self.description.toPlainText())

		outfilename = unicode(self.outfilename.displayText())
		namefield = unicode(self.namefield.currentText())
		exportdata = self.exportdata.isChecked()

		message = mmqgis_kml_export(self.iface, mmqgis_kml_export_layername, namefield, 
			mmqgis_kml_export_description, exportdata, outfilename, True)

		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "KML Export", message)

# --------------------------------------------------------
#    mmqgis_merge - Merge layers to single shapefile
# --------------------------------------------------------

from mmqgis_merge_form import *

class mmqgis_merge_dialog(QDialog, Ui_mmqgis_merge_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browseoutfile, SIGNAL("clicked()"), self.browse_outfiles)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.sourcelayers, True)

		# self.sourcelayers.clear()
		# for name, layer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
		#	if layer.type() == QgsMapLayer.VectorLayer:
		#		self.sourcelayers.addItem(layer.name())
		#		self.sourcelayers.item(self.sourcelayers.count() - 1).setSelected(1)

		# Suggested by Daniel Vaz
		self.sourcelayers.setDragDropMode(QAbstractItemView.InternalMove)
		self.outfilename.setText(mmqgis_temp_file_name(".shp"))

        def browse_outfiles(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.outfilename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.outfilename.setText(newname)

	def run(self):
		layernames = []
		for x in range(0, self.sourcelayers.count()):
			if self.sourcelayers.item(x).isSelected():
				layernames.append(unicode(self.sourcelayers.item(x).text()))

		savename = unicode(self.outfilename.displayText()).strip()

		message = mmqgis_merge(self.iface, layernames, savename, 1)
		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Merge", message)





# ----------------------------------------------------------
#    mmqgis_search - Interactive search
# ----------------------------------------------------------

from mmqgis_search_form import *

# These globals are a kludge to give search term persistence.
# This should probably be implemented in Qt with a static
# dialog and multiple exec(), but that is undocumented behavior
# that might break on Windoze.
# Defaults were requested by South Derbyshire District Council (7/14/2013)

mmqgis_search_layername = "SD_LLPG_MI_Live"
mmqgis_search_attribute1 = "SearchAddress"
mmqgis_search_attribute2 = "Postcode"
mmqgis_search_comparison1 = "contains"
mmqgis_search_comparison2 = "contains"
mmqgis_search_value1 = ""
mmqgis_search_value2 = ""

class mmqgis_search_dialog(QDialog, Ui_mmqgis_search_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)

		# print "Setup: " + mmqgis_search_layername

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.searchlayer, mmqgis_search_layername)
		self.searchlayer.addItem("[Google Maps]")
		self.searchlayer.addItem("[Open Street Map]")

		#Change of selection signals: currentTextChanged, currentRowChanged, itemSelectionChanged
		QObject.connect(self.results, SIGNAL("itemSelectionChanged()"), self.select_feature)

		QObject.connect(self.search, SIGNAL("clicked()"), self.perform_search)
		QObject.connect(self.donebutton, SIGNAL("clicked()"), self.finished)
		QObject.connect(self.searchlayer, SIGNAL("currentIndexChanged(QString)"), self.set_search_attributes)
		# QObject.connect(self.exportcsv, SIGNAL("clicked()"), self.export_to_file)

		comparisons = ['contains', 'begins with', '=', '<>', '>', '>=', '<', '<=']
		for x in comparisons:
			self.comparison1.addItem(x)
			self.comparison2.addItem(x)

		self.set_search_attributes()

	def set_search_attributes(self):
		self.results.clear()
		self.attribute1.clear()
		self.attribute2.clear()
		self.attribute2.addItem("(none)")

		# Special case for web address searches
		if (self.searchlayer.currentText() == "[Google Maps]") or \
		   (self.searchlayer.currentText() == "[Open Street Map]"):
			self.comparison1.setCurrentIndex(self.comparison1.findText("="))
			self.comparison2.setEnabled(False)
			self.attribute1.addItem("Address")
			self.attribute1.setEnabled(False)
			self.attribute2.setEnabled(False)
			self.value2.setEnabled(False)
			return

		else:
			self.comparison2.setEnabled(True)
			self.attribute1.setEnabled(True)
			self.attribute2.setEnabled(True)
			self.value2.setEnabled(True)

		layer = mmqgis_find_layer(self.searchlayer.currentText())
		if layer == None:
			return

		if (mmqgis_search_comparison1 > ""):
			self.comparison1.setCurrentIndex(self.comparison1.findText(mmqgis_search_comparison1))

		if (mmqgis_search_comparison2 > ""):
			self.comparison2.setCurrentIndex(self.comparison2.findText(mmqgis_search_comparison2))

		for index, field in enumerate(layer.fields()):
			self.attribute1.addItem(field.name())
			self.attribute2.addItem(field.name())

			if (field.name() == mmqgis_search_attribute1):
				self.attribute1.setCurrentIndex(index)
				self.value1.setText(mmqgis_search_value1)

			elif (field.name() == mmqgis_search_attribute2):
				self.attribute2.setCurrentIndex(index + 1)
				self.value2.setText(mmqgis_search_value2)

	def perform_search(self):
		if (self.searchlayer.currentText() == "[Google Maps]"):
			return self.perform_web_search("google")

		elif (self.searchlayer.currentText() == "[Open Street Map]"):
			return self.perform_web_search("osm")

		# print "perform_search(" + self.searchlayer.currentText() + ")"

		# Build list(s) of attribute names, comparison operators and comparison values
		layername = unicode(self.searchlayer.currentText())
		attributes = [ unicode(self.attribute1.currentText()) ]
		comparisons = [ self.comparison1.currentText() ]
		values = [ unicode(self.value1.displayText()).strip() ]

		if len(values[0]) <= 0:
			QMessageBox.critical(self.iface.mainWindow(), "Search", "No value given for comparison")
			return

		if (unicode(self.attribute1.currentText()) != "(none)") and \
		   (len(unicode(self.value2.displayText()).strip()) > 0):
			attributes.append(unicode(self.attribute2.currentText()))
			comparisons.append(self.comparison2.currentText())
			values.append(unicode(self.value2.displayText()).strip())

		# Perform search
		self.results.clear()
		self.features = mmqgis_search(self.iface, layername, attributes, comparisons, values, 1000)
		if type(self.features) != list:
			QMessageBox.critical(self.iface.mainWindow(), "Search", self.features)
			self.features = None
			return

		# Populate list of found features
		self.results.clear()
		for index, feature in self.features:
			# print str(index) + ") " + unicode(feature)
			self.results.addItem(unicode(feature))

	def perform_web_search(self, service):
		address = unicode(self.value1.displayText()).strip()
		address.replace("  ", " ")
		address.replace(" ", "+")
		# print "perform_web_search(" + address + ")"

		if (service == "google"):
			x, y, addrtype, addrlocat, formatted_addr = mmqgis_geocode_address_google(address)
		else:
			x, y, addrtype, addrlocat, formatted_addr = mmqgis_geocode_address_osm(address)

		self.features = []
		self.results.clear()
		for z in range(0, len(x)):
			self.features.append([[x[z],y[z]], formatted_addr[z]])
			self.results.addItem(unicode(formatted_addr[z]))


	# def export_to_file(self):
	#	newname = QFileDialog.getSaveFileName(None, "Output CSV File", 
	#		mmqgis_temp_file_name(".csv"), "CSV File (*.csv)")
	#
	#	if newname != None:
	#		self.filename.setText(newname)

	def select_feature(self):
		if (len(self.features) <= 0):
			return

		# Results from OSM / Google Maps
		if (type(self.features[0][0]) == list):
			return self.pan_to_xy_locations()

		layer = mmqgis_find_layer(self.searchlayer.currentText())
		if layer == None:
			return

		# Select all features in the layer that are selected in the results box
		layer.removeSelection()
		for index in range(0, self.results.count()):
			if (index < len(self.features)) and self.results.item(index).isSelected():
				# print unicode(index) + ") selected feature " + unicode(self.features[index][0])
				layer.select(self.features[index][0])

		# Nothing selected
		if len(layer.selectedFeatures()) <= 0:
			return 

		# Find the extent of the selected items
		transform = QgsCoordinateTransform(layer.crs(), self.iface.mapCanvas().mapRenderer().destinationCrs())

		centroids = []
		for feature in layer.selectedFeatures():
			centroids.append(transform.transform(feature.geometry().boundingBox().center()))

		# Center the canvas around the centroid of the selected features
		center = QgsGeometry.fromMultiPoint(centroids).boundingBox().center()
		extent = self.iface.mapCanvas().extent()
		extent.set(center.x() - (extent.width() / 2.0), center.y() - (extent.height() / 2.0),
			center.x() + (extent.width() / 2.0), center.y() + (extent.height() / 2.0))
		self.iface.mapCanvas().setExtent(extent)

		layer.triggerRepaint()
		# self.iface.mapCanvas().refresh()
		

	def pan_to_xy_locations(self):
		if (len(self.features) <= 0):
			return

		# Get list of selected points
		points = []
		for index in range(0, self.results.count()):
			if (index < len(self.features)) and self.results.item(index).isSelected():
				points.append(QgsPoint(self.features[index][0][0], self.features[index][0][1]))

		# Nothing selected
		if (len(points) <= 0):
			return

		# Transform to the map's coordinate system
		wgs84 = QgsCoordinateReferenceSystem()
		wgs84.createFromProj4("+proj=longlat +datum=WGS84 +no_defs")
		transform = QgsCoordinateTransform(wgs84,
			self.iface.mapCanvas().mapRenderer().destinationCrs())

		for z in range(0, len(points)):
			points[z] = transform.transform(points[z])

		# Center the canvas around the centroid of the selected features
		center = QgsGeometry.fromMultiPoint(points).boundingBox().center()
		extent = self.iface.mapCanvas().extent()
		extent.set(center.x() - (extent.width() / 2.0), center.y() - (extent.height() / 2.0),
			center.x() + (extent.width() / 2.0), center.y() + (extent.height() / 2.0))
		self.iface.mapCanvas().setExtent(extent)

		# layer.triggerRepaint()
		self.iface.mapCanvas().refresh()

	def finished(self):
		# Save form contents for future searches
		global mmqgis_search_layername
		global mmqgis_search_attribute1
		global mmqgis_search_attribute2
		global mmqgis_search_comparison1
		global mmqgis_search_comparison2
		global mmqgis_search_value1
		global mmqgis_search_value2

		mmqgis_search_layername = self.searchlayer.currentText()
		mmqgis_search_attribute1 = self.attribute1.currentText()
		mmqgis_search_attribute2 = self.attribute2.currentText()
		mmqgis_search_comparison1 = self.comparison1.currentText()
		mmqgis_search_comparison2 = self.comparison2.currentText()
		mmqgis_search_value1 = self.value1.displayText()
		mmqgis_search_value2 = self.value2.displayText()

		# print "Finished " + mmqgis_search_layername

		self.done(1)



# ----------------------------------------------------------
#    mmqgis_select - Select features by attribute
# ----------------------------------------------------------

from mmqgis_select_form import *

class mmqgis_select_dialog(QDialog, Ui_mmqgis_select_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browse, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.sourcelayer, True)

		QObject.connect(self.sourcelayer, SIGNAL("currentIndexChanged(QString)"), self.set_select_attributes)
		self.set_select_attributes()

		comparisons = ['=', '<>', '>', '>=', '<', '<=', 'begins with', 'contains']
		for x in comparisons:
			self.comparison.addItem(x)

		self.filename.setText(mmqgis_temp_file_name(".shp"))

        def browse_outfile(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.filename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.filename.setText(newname)

	def set_select_attributes(self):
		self.selectattribute.clear()
		layername = self.sourcelayer.currentText()
		for name, selectlayer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
			if selectlayer.name() == layername:
				for field in selectlayer.fields().toList():
					self.selectattribute.addItem(field.name())

	def run(self):
		savename = unicode(self.filename.displayText()).strip()
		layername = unicode(self.sourcelayer.currentText())
		comparisonname = self.comparison.currentText()
		comparisonvalue = unicode(self.value.displayText()).strip()
		selectattributename = self.selectattribute.currentText()

		message = mmqgis_select(self.iface, layername, [ selectattributename], \
			[ comparisonname ], [ comparisonvalue ], savename, 1)

		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Select", message)


# --------------------------------------------------------
#    mmqgis_sort - Sort shapefile by attribute
# --------------------------------------------------------

from mmqgis_sort_form import *

class mmqgis_sort_dialog(QDialog, Ui_mmqgis_sort_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browse, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.sourcelayer, True)

		QObject.connect(self.sourcelayer, SIGNAL("currentIndexChanged(QString)"), self.set_sort_attributes)

		self.set_sort_attributes()

		self.filename.setText(mmqgis_temp_file_name(".shp"))

        def browse_outfile(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.filename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.filename.setText(newname)

	def set_sort_attributes(self):
		self.sortattribute.clear()
		layer = mmqgis_find_layer(self.sourcelayer.currentText())
		if (layer == None):
			return
		for field in layer.fields().toList():
			self.sortattribute.addItem(field.name())

	def run(self):
		savename = unicode(self.filename.displayText()).strip()
		layername = unicode(self.sourcelayer.currentText())
		direction = unicode(self.direction.currentText())
		sortattributename = self.sortattribute.currentText()

		message = mmqgis_sort(self.iface, layername, sortattributename, savename, direction, 1)
		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Sort", message)


# ---------------------------------------------------------------
#    mmqgis_geocode_street_layer - Geocode addresses from street 
#					address finder shapefile
# ---------------------------------------------------------------

from mmqgis_geocode_street_layer_form import *

class mmqgis_geocode_street_layer_dialog(QDialog, Ui_mmqgis_geocode_street_layer_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browse_infile, SIGNAL("clicked()"), self.browse_infile_dialog)
		QObject.connect(self.browse_shapefile, SIGNAL("clicked()"), self.browse_shapefile_dialog)
		QObject.connect(self.browse_notfound, SIGNAL("clicked()"), self.browse_notfound_dialog)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.streetlayer, True)

		QObject.connect(self.streetlayer, SIGNAL("currentIndexChanged(int)"), self.set_layer_attributes)

		self.set_layer_attributes(0)

		self.shapefilename.setText(mmqgis_temp_file_name(".shp"))
		self.notfoundfilename.setText(os.getcwd() + "/notfound.csv")

        def browse_infile_dialog(self):
		newname = QFileDialog.getOpenFileName(None, "Address CSV Input File", 
			self.infilename.displayText(), "CSV File (*.csv *.txt)")

                if newname:
			header = mmqgis_read_csv_header(self.iface, newname)
			if not header:
				return

			# Add attributes to street and number
			self.streetnamefield.clear()
			self.numberfield.clear()
			self.zipfield.clear()

			self.zipfield.addItem("(none)")
			for field in header:
				self.streetnamefield.addItem(field)
				self.numberfield.addItem(field)
				self.zipfield.addItem(field)

			self.zipfield.setCurrentIndex(0)
			for x, field in enumerate(header):
				if field.strip().lower().find("street") >= 0:
					self.streetnamefield.setCurrentIndex(x)

				elif field.strip().lower().find("number") >= 0:
					self.numberfield.setCurrentIndex(x)

				elif field.strip().lower().find("zip") >= 0:
					self.zipfield.setCurrentIndex(x + 1)

                	self.infilename.setText(newname)

        def browse_notfound_dialog(self):
		newname = QFileDialog.getSaveFileName(None, "Not Found List Output File", 
			self.notfoundfilename.displayText(), "CSV File (*.csv *.txt)")
                if newname != None:
                	self.notfoundfilename.setText(newname)

        def browse_shapefile_dialog(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.shapefilename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.shapefilename.setText(newname)

	def set_layer_attributes(self, index):
		# index parameter required for currentIndexChanged() signal and is not used
		layername = unicode(self.streetlayer.currentText())
		layer = mmqgis_find_layer(layername)

		if not layer:
			print "Layer not found " + layername
			return

		self.setback.setText("0")

		#if (layer.dataProvider().crs().mapUnits() == QGis.Feet):
                #	self.setback.setText("60")
		#elif (layer.dataProvider().crs().mapUnits() == QGis.Meters):
                #	self.setback.setText("4")
                #else:
		#	self.setback.setText("0")
	
		#elif (layer.dataProvider().crs().mapUnits() == QGis.Degrees):
		#	meters = 4 * cos(layer.extent().center().y() * pi / 180) * 6378137.0
                #	self.setback.setText(unicode(meters))
		#else:
                #	self.setback.setText("4")

		self.streetname.clear()
		self.fromx.clear()
		self.fromy.clear()
		self.tox.clear()
		self.toy.clear()
		self.leftfrom.clear()
		self.leftto.clear()
		self.rightfrom.clear()
		self.rightto.clear()
		self.leftzip.clear()
		self.rightzip.clear()

		# From/To options to use line geometries for X/Y coordinates
		# Assumes order of line vertices in shapefile is consistent

		self.fromx.addItem("(street line start)")
		self.fromx.addItem("(street line end)")
		self.fromy.addItem("(street line start)")
		self.fromy.addItem("(street line end)")
		self.tox.addItem("(street line start)")
		self.tox.addItem("(street line end)")
		self.toy.addItem("(street line start)")
		self.toy.addItem("(street line end)")

		self.fromx.setCurrentIndex(0)
		self.fromy.setCurrentIndex(0)
		self.tox.setCurrentIndex(1)
		self.toy.setCurrentIndex(1)

		self.leftzip.addItem("(none)")
		self.rightzip.addItem("(none)")

		# Add all attributes to lists

		for field in layer.fields().toList():
			self.streetname.addItem(unicode(field.name()))
			self.fromx.addItem(unicode(field.name()))
			self.fromy.addItem(unicode(field.name()))
			self.tox.addItem(unicode(field.name()))
			self.toy.addItem(unicode(field.name()))
			self.leftfrom.addItem(unicode(field.name()))
			self.leftto.addItem(unicode(field.name()))
			self.rightfrom.addItem(unicode(field.name()))
			self.rightto.addItem(unicode(field.name()))
			self.leftzip.addItem(unicode(field.name()))
			self.rightzip.addItem(unicode(field.name()))


		# Select different parameters based on guesses from attribute names

		self.leftzip.setCurrentIndex(0)
		self.rightzip.setCurrentIndex(0)
		for index, field in enumerate(layer.fields()):
			if unicode(field.name()).lower().find("name") >= 0:
				self.streetname.setCurrentIndex(index)

			elif (unicode(field.name().lower()).find("street") >= 0):
				self.streetname.setCurrentIndex(index)

			elif (unicode(field.name().lower()).find("calle") >= 0):
				self.streetname.setCurrentIndex(index)

			elif unicode(field.name()).lower() == "xfrom":
				self.fromx.setCurrentIndex(index + 2)

			elif unicode(field.name()).lower() == "yfrom":
				self.fromy.setCurrentIndex(index + 2)

			elif unicode(field.name()).lower() == "xto":
				self.tox.setCurrentIndex(index + 2)

			elif unicode(field.name()).lower() == "yto":
				self.toy.setCurrentIndex(index + 2)

			elif unicode(field.name()).lower() == "lfromadd":
				self.leftfrom.setCurrentIndex(index)

			elif unicode(field.name()).lower() == "rfromadd":
				self.rightfrom.setCurrentIndex(index)

			elif unicode(field.name()).lower() == "ltoadd":
				self.leftto.setCurrentIndex(index)

			elif unicode(field.name()).lower() == "rtoadd":
				self.rightto.setCurrentIndex(index)

			elif unicode(field.name()).lower() == "zipl":
				self.leftzip.setCurrentIndex(index + 1)

			elif unicode(field.name()).lower() == "zipr":
				self.rightzip.setCurrentIndex(index + 1)

			elif (unicode(field.name().lower()).find("right") >= 0):
				if (unicode(field.name().lower()).find("from") >= 0):
					self.rightfrom.setCurrentIndex(index)

				elif (unicode(field.name().lower()).find("to") >= 0):
					self.rightto.setCurrentIndex(index)

			elif (unicode(field.name().lower()).find("left") >= 0):
				if (unicode(field.name().lower()).find("from") >= 0):
					self.leftfrom.setCurrentIndex(index)

				elif (unicode(field.name().lower()).find("to") >= 0):
					self.leftto.setCurrentIndex(index)
	


	def run(self):
		csvname = unicode(self.infilename.displayText()).strip()
		streetnamefield = unicode(self.streetnamefield.currentText()).strip()
		numberfield = unicode(self.numberfield.currentText()).strip()
		zipfield = unicode(self.zipfield.currentText()).strip()
		if zipfield == "(none)":
			zipfield = None

		layername = unicode(self.streetlayer.currentText())
		streetname = unicode(self.streetname.currentText())
		fromx = unicode(self.fromx.currentText())
		fromy = unicode(self.fromy.currentText())
		tox = unicode(self.tox.currentText())
		toy = unicode(self.toy.currentText())
		leftfrom = unicode(self.leftfrom.currentText())
		rightfrom = unicode(self.rightfrom.currentText())
		leftto = unicode(self.leftto.currentText())
		rightto = unicode(self.rightto.currentText())

		leftzip = unicode(self.leftzip.currentText())
		if leftzip == "(none)":
			leftzip = None
		rightzip = unicode(self.rightzip.currentText())
		if rightzip == "(none)":
			rightzip = None

		setback = float(self.setback.displayText())
		shapefilename = unicode(self.shapefilename.displayText())
		notfoundfile = self.notfoundfilename.displayText()
		# addlayer = self.addtoproject.isChecked()

		message = mmqgis_geocode_street_layer(self.iface, layername, csvname, streetnamefield, 
			numberfield, zipfield, streetname, fromx, fromy, tox, toy, leftfrom, rightfrom, 
			leftto, rightto, leftzip, rightzip, setback, shapefilename, notfoundfile, 1)

		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Geocode", message)

# ----------------------------------------------------------
#    mmqgis_spatial_join - Spatial Join
# ----------------------------------------------------------

from mmqgis_spatial_join_form import *

class mmqgis_spatial_join_dialog(QDialog, Ui_mmqgis_spatial_join_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browseoutfile, SIGNAL("clicked()"), self.browse_outfiles)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.targetlayer, True)

		self.fieldop.addItems(["First", "Sum", "Average", "Proportional Sum"])
		QObject.connect(self.targetlayer, SIGNAL("currentIndexChanged(QString)"), self.set_join_layers)
		QObject.connect(self.joinlayer, SIGNAL("currentIndexChanged(QString)"), self.set_spatial_operations)
		self.set_join_layers()

		self.outfilename.setText(mmqgis_temp_file_name(".shp"))

        def browse_outfiles(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.outfilename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.outfilename.setText(newname)

	def set_join_layers(self):
		self.joinlayer.clear()
		target_layer = mmqgis_find_layer(self.targetlayer.currentText())
		if (target_layer == None):
			return

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.joinlayer, True)

		# Remove target layer so no accidental join to itself
		index = 0
		while (index < self.joinlayer.count()):
			if (self.joinlayer.itemText(index) == target_layer.name()):
				self.joinlayer.removeItem(index)
			else:
				index = index + 1

		self.joinlayer.setCurrentIndex(0)
		self.set_spatial_operations()

	def set_spatial_operations(self):
		target = mmqgis_find_layer(self.targetlayer.currentText())
		if (target == None):
			return

		join = mmqgis_find_layer(self.joinlayer.currentText())
		if (join == None):
			return

		self.spatialop.clear()

		if not join:
			return

		# Rasters don't have fields()
		if (not hasattr(target, "fields")) or (not hasattr(join, "fields")):
			return

		self.fieldnames.clear()
		for field in target.fields().toList():
			self.fieldnames.addItem(field.name())
			self.fieldnames.item(self.fieldnames.count() - 1).setSelected(1)

		for field in join.fields().toList():
			self.fieldnames.addItem(field.name())
			self.fieldnames.item(self.fieldnames.count() - 1).setSelected(1)

		if (target.wkbType() in [QGis.WKBPoint, QGis.WKBPoint25D]):
			if (join.wkbType() in [QGis.WKBPolygon, QGis.WKBPolygon25D, 
			    QGis.WKBMultiPolygon, QGis.WKBMultiPolygon25D]):
				self.spatialop.addItems(["Within"])

		elif (target.wkbType() in [QGis.WKBMultiPoint, QGis.WKBMultiPoint25D, \
		      QGis.WKBLineString, QGis.WKBLineString25D, QGis.WKBMultiLineString, QGis.WKBMultiLineString25D]):
			if (join.wkbType() in [QGis.WKBPolygon, QGis.WKBPolygon25D,
			    QGis.WKBMultiPolygon, QGis.WKBMultiPolygon25D]):
				self.spatialop.addItems(["Intersects", "Within"])

		else: # Polygon
			if (join.wkbType() in [QGis.WKBPoint, QGis.WKBPoint25D]):
				self.spatialop.addItems(["Contains"])

			elif (join.wkbType() in [QGis.WKBMultiPoint, QGis.WKBMultiPoint25D,
			      QGis.WKBLineString, QGis.WKBLineString25D, QGis.WKBMultiLineString]):
				self.spatialop.addItems(["Intersects", "Contains"])

			else: # Polygon
				self.spatialop.addItems(["Intersects", "Within", "Contains"])


	def run(self):
		target = unicode(self.targetlayer.currentText())
		spatialop = unicode(self.spatialop.currentText())
		join = unicode(self.joinlayer.currentText())
		fieldop = unicode(self.fieldop.currentText())
		outfilename = unicode(self.outfilename.displayText())

		fields = []
		for x in range(0, self.fieldnames.count()):
			if self.fieldnames.item(x).isSelected():
				fields.append(self.fieldnames.item(x).text())

		message = mmqgis_spatial_join(self.iface, target, spatialop, join, fields, fieldop, outfilename, True)

		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Spatial Join", message)

# ---------------------------------------------------------
#    mmqgis_text_to_float - Change text fields to numbers
# ---------------------------------------------------------

from mmqgis_text_to_float_form import *

class mmqgis_text_to_float_dialog(QDialog, Ui_mmqgis_text_to_float_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browse, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.sourcelayer, True)

		QObject.connect(self.sourcelayer, SIGNAL("currentIndexChanged(QString)"), self.set_fieldnames)

		self.set_fieldnames()

		self.filename.setText(mmqgis_temp_file_name(".shp"))

        def browse_outfile(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.filename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.filename.setText(newname)

	def set_fieldnames(self):
		self.fieldnames.clear()
		layer = mmqgis_find_layer(self.sourcelayer.currentText())
		if (layer == None):
			return

		for index, field in enumerate(layer.fields()):
			self.fieldnames.addItem(field.name())

			if (field.type() == QVariant.String):
				self.fieldnames.item(index).setSelected(1)

	def run(self):
		layername = unicode(self.sourcelayer.currentText())
		savename = unicode(self.filename.displayText()).strip()
		# addlayer = self.addtoproject.isChecked()

		attributes = []
		for x in range(0, self.fieldnames.count()):
			if self.fieldnames.item(x).isSelected():
				attributes.append(self.fieldnames.item(x).text())

		message = mmqgis_text_to_float(self.iface, layername, attributes, savename, 1)
		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Text to Float", message)


# --------------------------------------------------------
#    mmqgis_voronoi - Voronoi diagram creation
# --------------------------------------------------------

from mmqgis_voronoi_form import *

class mmqgis_voronoi_dialog(QDialog, Ui_mmqgis_voronoi_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		QObject.connect(self.browse, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		mmqgis_load_combo_box_with_vector_layers(self.iface, self.sourcelayer, True)

		self.filename.setText(mmqgis_temp_file_name(".shp"))

        def browse_outfile(self):
		newname = QFileDialog.getSaveFileName(None, "Output Shapefile", 
			self.filename.displayText(), "Shapefile (*.shp)")
                if newname != None:
                	self.filename.setText(newname)

	def run(self):
		savename = unicode(self.filename.displayText()).strip()
		layer = unicode(self.sourcelayer.currentText())

		message = mmqgis_voronoi_diagram(self.iface, layer, savename, 1)
		if message <> None:
			QMessageBox.critical(self.iface.mainWindow(), "Voronoi", message)


# --------------------------------------------------------
#    Utility Functions
# --------------------------------------------------------

def mmqgis_read_csv_header(qgis, filename):
	try:
		infile = open(filename, 'r')
	except Exception as e:
		QMessageBox.information(qgis.mainWindow(), 
			"Input CSV File", "Failure opening " + filename + ": " + unicode(e))
		return None

	try:
		dialect = csv.Sniffer().sniff(infile.read(4096))
	except:
		QMessageBox.information(qgis.mainWindow(), "Input CSV File", 
			"Bad CSV file - verify that your delimiters are consistent");
		return None

	infile.seek(0)
	reader = csv.reader(infile, dialect)
		
	# Decode from UTF-8 characters because csv.reader can only handle 8-bit characters
	try:
		header = reader.next()
		header = [unicode(field, "utf-8") for field in header]
	except:
		QMessageBox.information(qgis.mainWindow(), "Input CSV File", 
			"Invalid character in file - verify your file uses UTF-8 character encoding");
		return None

	del reader
	del infile

	if len(header) <= 0:
		QMessageBox.information(qgis.mainWindow(), "Input CSV File", 
			filename + " does not appear to be a CSV file")
		return None

	return header

def mmqgis_load_combo_box_with_vector_layers(qgis, combo_box, set_selected):

	combo_box.clear()

	for legend in QgsProject.instance().layerTreeRoot().findLayers():
		layer = QgsMapLayerRegistry.instance().mapLayer(legend.layerId())
		if layer.type() == QgsMapLayer.VectorLayer:
			combo_box.addItem(layer.name())

	#for name, layer in QgsMapLayerRegistry.instance().mapLayers().iteritems():
	#	if layer.type() == QgsMapLayer.VectorLayer:
	#		combo_box.addItem(layer.name())

	# Parameter can be boolean "True" to use current selection in layer pane
	# or can be a str/unicode name

	if (type(set_selected) != bool):
		combo_index = combo_box.findText(set_selected)
		if combo_index >= 0:
			combo_box.setCurrentIndex(combo_index)
			return;

	for index, layer in enumerate(qgis.legendInterface().selectedLayers()):
		combo_index = combo_box.findText(layer.name())
		if combo_index >= 0:
			combo_box.setCurrentIndex(combo_index)
			break;

	

def mmqgis_temp_file_name(suffix):
	preferred = os.getcwd() + "/temp" + suffix
	if not os.path.isfile(preferred):
		return preferred

	for x in range(2, 10):
		name = os.getcwd() + "/temp" + unicode(x) + suffix
		if not os.path.isfile(name):
			return name

	return preferred


