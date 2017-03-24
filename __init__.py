# -*- coding: utf-8 -*-
# --------------------------------------------------------
#    __init__ - MMQGIS init file
#
#    begin                : August 5, 2009
#    copyright            : (c) 2009-2013 by Michael Minn
#    email                : See www.michaelminn.com
#
#   MMQGIS is free software and is offered without guarantee
#   or warranty. You can redistribute it and/or modify it 
#   under the terms of version 2 of the GNU General Public 
#   License (GPL v2) as published by the Free Software 
#   Foundation (www.gnu.org).
# --------------------------------------------------------

def classFactory(iface):
	from mmqgis_menu import mmqgis_menu
	return mmqgis_menu(iface)
