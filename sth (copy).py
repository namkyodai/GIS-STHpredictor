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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from sthdialog import STHDialog
import os.path

from modules import module3, module4


class ParameterContainer:
    def __init__(self):
        self.targetFileLocation = ""

        self.categories = {'A': 10, 'B': 10, 'C': 10, 'D': 10, 'E': 10, 'F': 10}

        self.timeStep = 10

    pass



class STH:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'sth_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = STHDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/sth/icon.png"),
            u"STH", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&STH", self.action)
        
        self.dlg.pushButtonInput.clicked.connect(self.selectInputFile)
        self.dlg.pushButtonOutput.clicked.connect(self.selectOutputFile)
        

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&STH", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        qDebug("result: " + str(result))
        # See if OK was pressed
        if result == 1:

            # Output of selected data START
            qDebug("Input file is located at: "+self.dlg.lineEditInput.displayText())
            qDebug("Output file is located att: "+self.dlg.lineEditOutput.displayText())
            
            
            qDebug("Category A is: "+self.dlg.comboBoxA.currentText())
            qDebug("Category B is: "+self.dlg.comboBoxB.currentText())
            qDebug("Category C is: "+self.dlg.comboBoxC.currentText())
            qDebug("Category D is: "+self.dlg.comboBoxD.currentText())
            qDebug("Category E is: "+self.dlg.comboBoxE.currentText())
            qDebug("Category F is: "+self.dlg.comboBoxF.currentText())
            
            qDebug("Chosen time step is: "+str(self.dlg.spinBoxTimeStep.value()))
            # Output of selected data STOP

            # Optional: Check for consistency (e.g. for valid file names)
            # ...
            # ...
            #if os.path.exists("module3"):
            #shutil.rmtree("module3")
            #os.mkdir("module3")

            # Copy QgsFile

            inputFileLocation = self.dlg.lineEditInput.displayText()
            outputFileLocation = self.dlg.lineEditOutput.displayText()


            inputLayer = QgsVectorLayer(inputFileLocation, "input_layer", "ogr")
            error = QgsVectorFileWriter.writeAsVectorFormat(inputLayer, outputFileLocation, "CP1250", None, "ESRI Shapefile")


            # Construct parameter container
            parameterContainer = ParameterContainer()

            parameterContainer.targetFileLocation = outputFileLocation

            parameterContainer.timeStep = self.dlg.spinBoxTimeStep.value()

            parameterContainer.categories['A'] = self.dlg.comboBoxA.currentText()
            parameterContainer.categories['B'] = self.dlg.comboBoxB.currentText()
            parameterContainer.categories['C'] = self.dlg.comboBoxC.currentText()
            parameterContainer.categories['D'] = self.dlg.comboBoxD.currentText()
            parameterContainer.categories['E'] = self.dlg.comboBoxE.currentText()
            parameterContainer.categories['F'] = self.dlg.comboBoxF.currentText()


            # Run model
            if (self.dlg.comboBoxModel.currentText() == "Model 3"):
                qDebug("Model 3 was chosen")
                module3.run(parameterContainer)

            elif (self.dlg.comboBoxModel.currentText() == "Model 4"):
                qDebug("Model 4 was chosen")
                module4.run(parameterContainer)

                pass

            outputLayer = QgsVectorLayer(outputFileLocation, "output_layer", "ogr")
            QgsMapLayerRegistry.instance().addMapLayer(outputLayer)

    def selectInputFile(self):
        fileName = QFileDialog.getOpenFileName(self.dlg, "Load Shapefile", ".", "Shapefile (*.shp)");
        self.dlg.lineEditInput.setText(fileName)
        pass

    def selectOutputFile(self):
        fileName = QFileDialog.getOpenFileName(self.dlg, "Write Shapefile", ".", "Shapefile (*.shp)");
        self.dlg.lineEditOutput.setText(fileName)
        pass