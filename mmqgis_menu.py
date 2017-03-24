# --------------------------------------------------------
#    mmqgis_menu - QGIS plugins menu class
#
#    begin                : August 5, 2009
#    copyright            : (c) 2009 - 2012 by Michael Minn
#    email                : See michaelminn.com
#
#   MMQGIS is free software and is offered without guarantee
#   or warranty. You can redistribute it and/or modify it 
#   under the terms of version 2 of the GNU General Public 
#   License (GPL v2) as published by the Free Software 
#   Foundation (www.gnu.org).
# --------------------------------------------------------

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from mmqgis_dialogs import *

# ---------------------------------------------

class mmqgis_menu:
	def __init__(self, iface):
		self.iface = iface
		self.mmqgis_menu = None

	def mmqgis_add_submenu(self, submenu):
		if self.mmqgis_menu != None:
			self.mmqgis_menu.addMenu(submenu)
		else:
			self.iface.addPluginToMenu("&mmqgis", submenu.menuAction())

	def initGui(self):
		# Uncomment the following two lines to have MMQGIS accessible from a top-level menu
		self.mmqgis_menu = QMenu(QCoreApplication.translate("mmqgis", "MMQGIS"))
		self.iface.mainWindow().menuBar().insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.mmqgis_menu)

		# Animate Submenu
		self.animate_menu = QMenu(QCoreApplication.translate("mmqgis", "&Animate"))
		self.mmqgis_add_submenu(self.animate_menu)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_animate_columns.png")
		self.animate_columns_action = QAction(icon, "Animate Columns", self.iface.mainWindow())
		QObject.connect(self.animate_columns_action, SIGNAL("triggered()"), self.animate_columns)
		self.animate_menu.addAction(self.animate_columns_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_animate_lines.png")
		self.animate_lines_action = QAction(icon, "Animate Lines", self.iface.mainWindow())
		QObject.connect(self.animate_lines_action, SIGNAL("triggered()"), self.animate_lines)
		self.animate_menu.addAction(self.animate_lines_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_animate_rows.png")
		self.animate_rows_action = QAction(icon, "Animate Rows", self.iface.mainWindow())
		QObject.connect(self.animate_rows_action, SIGNAL("triggered()"), self.animate_rows)
		self.animate_menu.addAction(self.animate_rows_action)


		# Combine Submenu
		self.combine_menu = QMenu(QCoreApplication.translate("mmqgis", "&Combine"))
		self.mmqgis_add_submenu(self.combine_menu)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_attribute_join.png")
		self.attribute_join_action = QAction(icon, "Attributes Join from CSV File", self.iface.mainWindow())
		QObject.connect(self.attribute_join_action, SIGNAL("triggered()"), self.attribute_join)
		self.combine_menu.addAction(self.attribute_join_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_merge.png")
		self.merge_action = QAction(icon, "Merge Layers", self.iface.mainWindow())
		QObject.connect(self.merge_action, SIGNAL("triggered()"), self.merge)
		self.combine_menu.addAction(self.merge_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_spatial_join.png")
		self.spatial_join_action = QAction(icon, "Spatial Join", self.iface.mainWindow())
		QObject.connect(self.spatial_join_action, SIGNAL("triggered()"), self.spatial_join)
		self.combine_menu.addAction(self.spatial_join_action)


		# Create Submenu
		self.create_menu = QMenu(QCoreApplication.translate("mmqgis", "&Create"))
		self.mmqgis_add_submenu(self.create_menu)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_buffers.png")
		self.buffers_action = QAction(icon, "Create Buffers", self.iface.mainWindow())
		QObject.connect(self.buffers_action, SIGNAL("triggered()"), self.buffers)
		self.create_menu.addAction(self.buffers_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_grid.png")
		self.grid_action = QAction(icon, "Create Grid Layer", self.iface.mainWindow())
		QObject.connect(self.grid_action, SIGNAL("triggered()"), self.grid)
		self.create_menu.addAction(self.grid_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_hub_distance.png")
		self.hub_distance_action = QAction(icon, "Hub Distance", self.iface.mainWindow())
		QObject.connect(self.hub_distance_action, SIGNAL("triggered()"), self.hub_distance)
		self.create_menu.addAction(self.hub_distance_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_hub_distance.png")
		self.hub_lines_action = QAction(icon, "Hub Lines", self.iface.mainWindow())
		QObject.connect(self.hub_lines_action, SIGNAL("triggered()"), self.hub_lines)
		self.create_menu.addAction(self.hub_lines_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_voronoi.png")
		self.voronoi_action = QAction(icon, "Voronoi Diagram", self.iface.mainWindow())
		QObject.connect(self.voronoi_action, SIGNAL("triggered()"), self.voronoi)
		self.create_menu.addAction(self.voronoi_action)


		# Geocode submenu
		self.geocode_menu = QMenu(QCoreApplication.translate("mmqgis", "&Geocode"))
		self.mmqgis_add_submenu(self.geocode_menu)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_geocode_web_service.png")
		self.geocode_web_service_action = QAction(icon, "Geocode CSV with Google / OpenStreetMap", 
			self.iface.mainWindow())
		QObject.connect(self.geocode_web_service_action, SIGNAL("triggered()"), self.geocode_web_service)
		self.geocode_menu.addAction(self.geocode_web_service_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_geocode_street_layer.png")
		self.geocode_street_layer_action = QAction(icon, "Geocode from Street Layer", self.iface.mainWindow())
		QObject.connect(self.geocode_street_layer_action, SIGNAL("triggered()"), self.geocode_street_layer)
		self.geocode_menu.addAction(self.geocode_street_layer_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_geocode_street_layer.png")
		self.street_address_join_action = QAction(icon, "Street Address Join", self.iface.mainWindow())
		QObject.connect(self.street_address_join_action, SIGNAL("triggered()"), self.street_address_join)
		self.geocode_menu.addAction(self.street_address_join_action)


		# Search / Select Submenu
		self.search_select_menu = QMenu(QCoreApplication.translate("mmqgis", "&Search / Select"))
		self.mmqgis_add_submenu(self.search_select_menu)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_search.png")
		self.search_action = QAction(icon, "Search", self.iface.mainWindow())
		QObject.connect(self.search_action, SIGNAL("triggered()"), self.search)
		self.search_select_menu.addAction(self.search_action)

		# This one button in the plugins toolbar is for the South Derbyshire District Council (7/14/2013)
		# self.iface.addToolBarIcon(self.search_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_select.png")
		self.select_action = QAction(icon, "Select", self.iface.mainWindow())
		QObject.connect(self.select_action, SIGNAL("triggered()"), self.select)
		self.search_select_menu.addAction(self.select_action)


		# Import / Export Submenu
		self.import_export_menu = QMenu(QCoreApplication.translate("mmqgis", "&Import / Export"))
		self.mmqgis_add_submenu(self.import_export_menu)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_attribute_export.png")
		self.attribute_export_action = QAction(icon, "Attributes Export to CSV File", self.iface.mainWindow())
		QObject.connect(self.attribute_export_action, SIGNAL("triggered()"), self.attribute_export)
		self.import_export_menu.addAction(self.attribute_export_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_attribute_export.png")
		self.geometry_export_action = QAction(icon, "Geometry Export to CSV File", self.iface.mainWindow())
		QObject.connect(self.geometry_export_action, SIGNAL("triggered()"), self.geometry_export)
		self.import_export_menu.addAction(self.geometry_export_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_attribute_join.png")
		self.geometry_import_action = QAction(icon, "Geometry Import from CSV File", self.iface.mainWindow())
		QObject.connect(self.geometry_import_action, SIGNAL("triggered()"), self.geometry_import)
		self.import_export_menu.addAction(self.geometry_import_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_geocode_web_service.png")
		self.kml_export_action = QAction(icon, "Google Maps KML Export", self.iface.mainWindow())
		QObject.connect(self.kml_export_action, SIGNAL("triggered()"), self.kml_export)
		self.import_export_menu.addAction(self.kml_export_action)

		# Modify Submenu
		self.modify_menu = QMenu(QCoreApplication.translate("mmqgis", "&Modify"))
		self.mmqgis_add_submenu(self.modify_menu)

		# icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_color_ramp.png")
		# self.color_ramp_action = QAction(icon, "Color Ramp", self.iface.mainWindow())
		# QObject.connect(self.color_ramp_action, SIGNAL("triggered()"), self.color_ramp)
		# self.modify_menu.addAction(self.color_ramp_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_attribute_export.png")
		self.geometry_convert_action = QAction(icon, "Convert Geometry Type", self.iface.mainWindow())
		QObject.connect(self.geometry_convert_action, SIGNAL("triggered()"), self.geometry_convert)
		self.modify_menu.addAction(self.geometry_convert_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_attribute_join.png")
		self.delete_duplicate_action = QAction(icon, "Delete Duplicate Geometries", self.iface.mainWindow())
		QObject.connect(self.delete_duplicate_action, SIGNAL("triggered()"), self.delete_duplicate_geometries)
		self.modify_menu.addAction(self.delete_duplicate_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_float_to_text.png")
		self.float_to_text_action = QAction(icon, "Float to Text", self.iface.mainWindow())
		QObject.connect(self.float_to_text_action, SIGNAL("triggered()"), self.float_to_text)
		self.modify_menu.addAction(self.float_to_text_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_gridify.png")
		self.gridify_action = QAction(icon, "Gridify", self.iface.mainWindow())
		QObject.connect(self.gridify_action, SIGNAL("triggered()"), self.gridify)
		self.modify_menu.addAction(self.gridify_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_sort.png")
		self.sort_action = QAction(icon, "Sort", self.iface.mainWindow())
		QObject.connect(self.sort_action, SIGNAL("triggered()"), self.sort)
		self.modify_menu.addAction(self.sort_action)

		icon = QIcon(os.path.dirname(__file__) + "/icons/mmqgis_text_to_float.png")
		self.text_to_float_action = QAction(icon, "Text to Float", self.iface.mainWindow())
		QObject.connect(self.text_to_float_action, SIGNAL("triggered()"), self.text_to_float)
		self.modify_menu.addAction(self.text_to_float_action)





	def unload(self):
		if self.mmqgis_menu != None:
			self.iface.mainWindow().menuBar().removeAction(self.mmqgis_menu.menuAction())
		else:
			self.iface.removePluginMenu("&mmqgis", self.animate_menu.menuAction())
			self.iface.removePluginMenu("&mmqgis", self.combine_menu.menuAction())
			self.iface.removePluginMenu("&mmqgis", self.create_menu.menuAction())
			self.iface.removePluginMenu("&mmqgis", self.geocode_menu.menuAction())
			self.iface.removePluginMenu("&mmqgis", self.import_export_menu.menuAction())
			self.iface.removePluginMenu("&mmqgis", self.modify_menu.menuAction())

		# This one button in the plugins toolbar is for the South Derbyshire District Council (7/14/2013)
		# self.iface.removeToolBarIcon(self.search_action)

	def street_address_join(self):
		dialog = mmqgis_street_address_join_dialog(self.iface)
		dialog.exec_()

	def animate_columns(self):
		dialog = mmqgis_animate_columns_dialog(self.iface)
		dialog.exec_()

	def animate_lines(self):
		dialog = mmqgis_animate_lines_dialog(self.iface)
		dialog.exec_()

	def animate_rows(self):
		dialog = mmqgis_animate_rows_dialog(self.iface)
		dialog.exec_()

	def attribute_export(self):
		dialog = mmqgis_attribute_export_dialog(self.iface)
		dialog.exec_()

	def attribute_join(self):
		dialog = mmqgis_attribute_join_dialog(self.iface)
		dialog.exec_()

	def buffers(self):
		#try:
		#	self.buffers_dialog
		#except:
		#	self.buffers_dialog = mmqgis_buffers_dialog(self.iface)
		#self.buffers_dialog.exec_()

		dialog = mmqgis_buffers_dialog(self.iface)
		dialog.exec_()

	def color_ramp(self):
		dialog = mmqgis_color_ramp_dialog(self.iface)
		dialog.exec_()

	def delete_duplicate_geometries(self):
		dialog = mmqgis_delete_duplicate_dialog(self.iface)
		dialog.exec_()

	def float_to_text(self):
		dialog = mmqgis_float_to_text_dialog(self.iface)
		dialog.exec_()

	def geocode_web_service(self):
		dialog = mmqgis_geocode_web_service_dialog(self.iface)
		dialog.exec_()

	def geocode_street_layer(self):
		dialog = mmqgis_geocode_street_layer_dialog(self.iface)
		dialog.exec_()

	def geometry_convert(self):
		dialog = mmqgis_geometry_convert_dialog(self.iface)
		dialog.exec_()

	def geometry_export(self):
		dialog = mmqgis_geometry_export_dialog(self.iface)
		dialog.exec_()

	def geometry_import(self):
		dialog = mmqgis_geometry_import_dialog(self.iface)
		dialog.exec_()

	def grid(self):
		dialog = mmqgis_grid_dialog(self.iface)
		dialog.exec_()

	def gridify(self):
		dialog = mmqgis_gridify_dialog(self.iface)
		dialog.exec_()

	def hub_distance(self):
		dialog = mmqgis_hub_distance_dialog(self.iface)
		dialog.exec_()

	def hub_lines(self):
		dialog = mmqgis_hub_lines_dialog(self.iface)
		dialog.exec_()

	def kml_export(self):
		dialog = mmqgis_kml_export_dialog(self.iface)
		dialog.exec_()

	def merge(self):
		dialog = mmqgis_merge_dialog(self.iface)
		dialog.exec_()

	def search(self):
		# Modeless interactive dialog
		# Must be saved in self, otherwise garbage collector destroys dialog
		self.search_dialog = mmqgis_search_dialog(self.iface)
		self.search_dialog.setWindowModality(QtCore.Qt.NonModal) 
		self.search_dialog.show()
		# self.search_dialog.activateWindow()

	def select(self):
		dialog = mmqgis_select_dialog(self.iface)
		dialog.exec_()

	def sort(self):
		dialog = mmqgis_sort_dialog(self.iface)
		dialog.exec_()

	def spatial_join(self):
		dialog = mmqgis_spatial_join_dialog(self.iface)
		dialog.exec_()

	def text_to_float(self):
		dialog = mmqgis_text_to_float_dialog(self.iface)
		dialog.exec_()

	def voronoi(self):
		dialog = mmqgis_voronoi_dialog(self.iface)
		dialog.exec_()

