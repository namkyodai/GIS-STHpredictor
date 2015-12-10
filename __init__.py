# -*- coding: utf-8 -*-
"""
/***************************************************************************
 STH
                                 A QGIS plugin
 STH
                             -------------------
        begin                : 2014-05-07
        copyright            : (C) 2014 by STH
        email                : STH@STH.STH
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load STH class from file STH
    from sth import STH
    return STH(iface)
