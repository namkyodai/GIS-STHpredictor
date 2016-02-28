# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GIS-STH-Predictor
 This program was designed and coded by Nam Lethanh, with supports of a Phd Student Magnus Heitzler @ ETHZ, Zürich
                                 A QGIS plugin
 STH predictor
                              -------------------
        begin                : 2014-05-07
        end		     : January, 2016
        copyright            : (C) 2016 by Nam Lethanh
        email                : namkyodai@gmail.com
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

from osgeo import ogr

from modules import module3, module4


class ParameterContainer:
    def __init__(self):
        self.targetFileLocation = ""
        self.categories = {'A': 11, 'B': 11, 'C': 11, 'D': 11, 'E': 11, 'F': 11}

        self.timeStep = 11

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
        
        #self.sideLabel = QLabel()
        #self.sideLabel.setTextFormat(Qt.RichText)
        #self.sideLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)

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
        self.dlg.pushButtonOutput.clicked.connect(self.selectOutputFolder)
        
        self.dlg.comboBoxModel.currentIndexChanged[str].connect(self.modelComboBoxChanged)
        
        #self.dlg.setSideWidget(QWidget())
        #hbox = QHBoxLayout()
        #hbox.addWidget(self.sideLabel)
        #self.dlg.sideWidget().setLayout(hbox)
        #self.sideLabel.setFixedWidth(100)
        #self.sideLabel.setWordWrap(True)
        #self.sideLabel.setText("Help:<br>")

        

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
            qDebug("Input file is located at: "  + self.dlg.lineEditInputFileName.displayText())
            qDebug("Output file is located at: " + self.dlg.lineEditOutputFolder.displayText() + "/" + self.dlg.lineEditOutputFileName.displayText())
            
            
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

            inputFileLocation = self.dlg.lineEditInputFileName.displayText()
            outputFileLocation = self.dlg.lineEditOutputFolder.displayText() + "/" + self.dlg.lineEditOutputFileName.displayText()
            if (outputFileLocation.endswith(".shp") == False):
	        outputFileLocation = outputFileLocation + ".shp"


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
            if (self.dlg.comboBoxModel.currentText() == "STH prevalance"):
                qDebug("Model 3 was chosen")
                module3.run(parameterContainer)

            elif (self.dlg.comboBoxModel.currentText() == "Total prevalance"):
                qDebug("Model 4 was chosen")
                module4.run(parameterContainer)

                pass

            outputLayer = QgsVectorLayer(outputFileLocation, "output_layer", "ogr")
            QgsMapLayerRegistry.instance().addMapLayer(outputLayer)

    def selectInputFile(self):
        fileName = QFileDialog.getOpenFileName(self.dlg, "Load Shapefile", ".", "Shapefile (*.shp)");

	self.checkShapefileConsistency(fileName, self.dlg.comboBoxModel.currentText())
	
        
        self.dlg.lineEditInputFileName.setText(fileName)
        pass

    def selectOutputFolder(self):
        folderName = QFileDialog.getExistingDirectory(self.dlg, "Select Output Folder");
        self.dlg.lineEditOutputFolder.setText(folderName)
        pass
      
      
    def checkShapefileConsistency(self, fileName, modelName):
        # ------------------------- #
        # validate input file START #
        # ------------------------- #      
        
        shapefile = ogr.Open(fileName, 0)
        
        # check if file is valid

        if shapefile is None:
           QMessageBox.warning(None, "Shapefile load error.", "Please select a valid Shapefile.")
           
        pureFileName = os.path.splitext(os.path.basename(fileName))[0]

        lyr = shapefile.GetLayer(0)
        lyrDef = lyr.GetLayerDefn()
        
        
        categoryFound = False
        categoryIsString = False
        for i in range(lyrDef.GetFieldCount()):
	  if (lyrDef.GetFieldDefn(i).GetName() == "CATEGORY"):
	    found = True
	    if (lyrDef.GetFieldDefn(i).GetType() == ogr.OFTString):
	      categoryIsString = True
	
	lyr.ResetReading()
        
        # check if CATEGORY is present
        if (found == False):
           QMessageBox.warning(None, "Shapefile load error.", "The shapefile does not have a field named CATEGORY.")
        
        # check if CATEGORY is of type string
        if (categoryIsString == False):
           QMessageBox.warning(None, "Shapefile load error.", "The shapefile has a field named CATEGORY but it is not of type Text.")
        
        
        possiblyProblematicFeatures = []
        # check if there are any missing or invalid entries in CATEGORY
        for i in range(lyr.GetFeatureCount()):
           feature=lyr.GetFeature(i)
           featureCategory = feature.GetField("CATEGORY")
           
           
           if (featureCategory not in ["A", "B", "C", "D", "E", "F"]):
              possiblyProblematicFeatures.append(feature.GetFID())

	lyr.ResetReading()
        
        # invalid features
        if (len(possiblyProblematicFeatures)>0):
           QMessageBox.warning(None, "Shapefile load warning.", "The shapefile has a field named CATEGORY but the following features have an invalid CATEGORY field. Feature IDs are: " + ",".join(possiblyProblematicFeatures))
        
        numericFields = []
        numericFieldsPresent = []
        if (modelName == "Model 4"):
	    numericFields = ["STH"]
	    numericFieldsPresent = [False]
	
        if (modelName == "Model 3"):
	    numericFields = ["HW_3", "Tt_3", "Al_3"]
	    numericFieldsPresent = [False, False, False]
        
        # check if mandatory numeric fields exist
        for i in range(lyrDef.GetFieldCount()):
	  if (lyrDef.GetFieldDefn(i).GetName() in numericFields):
	    numericFieldsPresent[numericFields.index(lyrDef.GetFieldDefn(i).GetName())] = True
        
        missingNumericFields = []
        for index in range(0, len(numericFieldsPresent)):
	  if (numericFieldsPresent[index] == False):
	    missingNumericFields.append(numericFields[index])
        
        if (len(missingNumericFields)>0):
           QMessageBox.warning(None, "Shapefile load error.", "Check that all mandatory numeric fields are present. Missing field names are: " + ",".join(missingNumericFields))
        
        # check if mandatory numeric fields are numeric
        problematicFields = []
        
        for i in range(lyrDef.GetFieldCount()):
	  if (lyrDef.GetFieldDefn(i).GetName() in numericFields):
	    if (lyrDef.GetFieldDefn(i).GetType() != ogr.OFTInteger and lyrDef.GetFieldDefn(i).GetType() != ogr.OFTReal):
	      problematicFields.append(lyrDef.GetFieldDefn(i).GetName())
        
        if (len(problematicFields)>0):
           QMessageBox.warning(None, "Shapefile load warning.", "Check the numeric fields in your shapefile. Some of them are not numeric. Field names are: " + ",".join(problematicFields))


        # check for validity in numeric fields
        wrongValueFeatures = []
        for numericFieldName in numericFields:
	   lyr.ResetReading()
           for i in range(lyr.GetFeatureCount()):
              feature=lyr.GetFeature(i)
              featureValue = feature.GetField(numericFieldName)
              if (featureValue < 0 or featureValue > 1):
                 wrongValueFeatures.append(feature.GetFID())
        
        if (len(wrongValueFeatures)>0):
	  QMessageBox.warning(None, "Shapefile load warning.", "Check the numeric fields in your shapefile. Some features have values outside the range [0, 1].")
          #QMessageBox.warning(None, "Shapefile load warning.", "Please check the numeric fields in your shapefile. Some features have values outside the range [0, 100]. Feature IDs are: " + ",".join(possiblyProblematicFeatures))

	
        # ------------------------- #
        # validate input file STOP  #
        # ------------------------- # 
        
    def modelComboBoxChanged(self, modelName):
        if self.dlg.lineEditInputFileName.displayText() == "":
	  return
	
	print modelName
	
	self.checkShapefileConsistency(self.dlg.lineEditInputFileName.displayText(), modelName)
        
