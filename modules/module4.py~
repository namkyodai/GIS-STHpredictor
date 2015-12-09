import os,os.path,shutil
import osgeo.ogr
import shapely.wkt
import osgeo.osr
from osgeo import ogr
import random
from random import randint
import numpy as np


#define the variable of the model
time=100 #maximum numbers of year for the program to 
breakpoint1=5
breakpoint2=10

import mo4function

from mo4function import model4high
from mo4function import model4moderate
from mo4function import model4light
from mo4function import model4no

import prediction
from prediction import prediction

import mtp4 #the file contain the pre-defined markov transition probability for model 4

def getControlProgram(value):
    if value == "CP1":
        return mtp4.mtp_cp1
    elif value == "CP2":
        return mtp4.mtp_cp2
    elif value == "CP3":
        return mtp4.mtp_cp3
    elif value == "CP4":
        return mtp4.mtp_cp4
    elif value == "CP5":
        return mtp4.mtp_cp5
    elif value == "CP6":
        return mtp4.mtp_cp6
    elif value == "CP7":
        return mtp4.mtp_cp7
    elif value == "CP8":
        return mtp4.mtp_cp8
    elif value == "CP9":
        return mtp4.mtp_cp9
    elif value == "CP10":
        return mtp4.mtp_cp10
    elif value == "No intervention":
        return mtp4.mtp_cpdn

def run(parameterContainer):
    # Open the source shapefile.
    shapefile = osgeo.ogr.Open(parameterContainer.targetFileLocation, 1)
    time = parameterContainer.timeStep
    layer = shapefile.GetLayer(0)
    spatialReference = layer.GetSpatialRef()

    driver = osgeo.ogr.GetDriverByName("ESRI Shapefile")

    controlProgramA = getControlProgram(parameterContainer.categories['A'])
    controlProgramB = getControlProgram(parameterContainer.categories['B'])
    controlProgramC = getControlProgram(parameterContainer.categories['C'])
    controlProgramD = getControlProgram(parameterContainer.categories['D'])
    controlProgramE = getControlProgram(parameterContainer.categories['E'])
    controlProgramF = getControlProgram(parameterContainer.categories['F'])

    print parameterContainer.categories['A']
    print parameterContainer.categories['B']
    print parameterContainer.categories['C']
    print parameterContainer.categories['D']
    print parameterContainer.categories['E']
    print parameterContainer.categories['F']

    print controlProgramA
    print controlProgramB
    print controlProgramC
    print controlProgramD
    print controlProgramE
    print controlProgramF


    words = ['STHyear', 'noyear', 'lightyear', 'moderyear', 'highyear']
    for i in words:
        for t in range(time):
            fieldDef = osgeo.ogr.FieldDefn(i+str(t), osgeo.ogr.OFTReal)
            #fieldDef.SetWidth(5)
            layer.CreateField(fieldDef)


    for i in range(layer.GetFeatureCount()):
        feature=layer.GetFeature(i)
        layer.SetFeature(feature)

        #feature.SetField("STH", randint(0,100))
#<<<<<<< HEAD
	feature.SetField("STH", feature.GetField("STH")*1)
#=======
#	feature.SetField("STH", feature.GetField("STH")*100)
#>>>>>>> 533be90ebbafee6ae561cd32f60004fe6367577f
        #now estimate the intensity at t=0

        if feature.GetField("CATEGORY") == "A":
	    

            for t in range(time):
                if t==0:
                    STH=feature.GetField("STH")
                    cs1=model4no(STH)
                    cs2=model4light(STH)
                    cs3=model4moderate(STH)
                    cs4=model4high(STH)
                    feature.SetField("noyear"+str(t), cs1)
                    feature.SetField("lightyear"+str(t), cs2)
                    feature.SetField("moderyear"+str(t), cs3)
                    feature.SetField("highyear"+str(t), cs4)
                    feature.SetField("STHyear"+str(t), cs2+cs3+cs4)
                    cs=np.array([cs1,cs2,cs3,cs4])


                    #end of the loop with t

            value=prediction(time,cs,controlProgramA,controlProgramA,controlProgramA,breakpoint1,breakpoint2)
            #value=prediction(time,cs,mtp4.mtp_cp1,mtp4.mtp_cp1,mtp4.mtp_cp1,breakpoint1,breakpoint2)


            for t in (range(time)):
                if t > 0:

                    cs1=value[t][0]
                    cs2=value[t][1]
                    cs3=value[t][2]
                    cs4=value[t][3]

                    feature.SetField("noyear"+str(t), cs1)
                    feature.SetField("lightyear"+str(t), cs2)
                    feature.SetField("moderyear"+str(t), cs3)
                    feature.SetField("highyear"+str(t), cs4)
                    feature.SetField("STHyear"+str(t), cs2+cs3+cs4)



        elif feature.GetField("CATEGORY") == "B":


            for t in range(time):
                if t==0:
                    STH=feature.GetField("STH")
                    cs1=model4no(float(STH))
                    cs2=model4light(float(STH))
                    cs3=model4moderate(float(STH))
                    cs4=model4high(float(STH))
                    feature.SetField("noyear"+str(t), cs1)
                    feature.SetField("lightyear"+str(t), cs2)
                    feature.SetField("moderyear"+str(t), cs3)
                    feature.SetField("highyear"+str(t), cs4)
                    feature.SetField("STHyear"+str(t), cs2+cs3+cs4)
                    cs=np.array([cs1,cs2,cs3,cs4])


                    #end of the loop with t

            value=prediction(time,cs,controlProgramB,controlProgramB,controlProgramB,breakpoint1,breakpoint2)
            #value=prediction(time,cs,mtp4.mtp_cp1,mtp4.mtp_cp1,mtp4.mtp_cp1,breakpoint1,breakpoint2)


            for t in (range(time)):
                if t > 0:

                    cs1=value[t][0]
                    cs2=value[t][1]
                    cs3=value[t][2]
                    cs4=value[t][3]

                    feature.SetField("noyear"+str(t), cs1)
                    feature.SetField("lightyear"+str(t), cs2)
                    feature.SetField("moderyear"+str(t), cs3)
                    feature.SetField("highyear"+str(t), cs4)
                    feature.SetField("STHyear"+str(t), cs2+cs3+cs4)



        elif feature.GetField("CATEGORY") == "C":


            for t in range(time):
                if t==0:
                    STH=feature.GetField("STH")
                    cs1=model4no(float(STH))
                    cs2=model4light(float(STH))
                    cs3=model4moderate(float(STH))
                    cs4=model4high(float(STH))
                    feature.SetField("noyear"+str(t), cs1)
                    feature.SetField("lightyear"+str(t), cs2)
                    feature.SetField("moderyear"+str(t), cs3)
                    feature.SetField("highyear"+str(t), cs4)
                    feature.SetField("STHyear"+str(t), cs2+cs3+cs4)
                    cs=np.array([cs1,cs2,cs3,cs4])


                    #end of the loop with t

            value=prediction(time,cs,controlProgramC,controlProgramC,controlProgramC,breakpoint1,breakpoint2)
            #value=prediction(time,cs,mtp4.mtp_cp1,mtp4.mtp_cp1,mtp4.mtp_cp1,breakpoint1,breakpoint2)


            for t in (range(time)):
                if t > 0:

                    cs1=value[t][0]
                    cs2=value[t][1]
                    cs3=value[t][2]
                    cs4=value[t][3]

                    feature.SetField("noyear"+str(t), cs1)
                    feature.SetField("lightyear"+str(t), cs2)
                    feature.SetField("moderyear"+str(t), cs3)
                    feature.SetField("highyear"+str(t), cs4)
                    feature.SetField("STHyear"+str(t), cs2+cs3+cs4)



        elif feature.GetField("CATEGORY") == "D":

            for t in range(time):
                if t==0:
                    STH=feature.GetField("STH")
                    cs1=model4no(float(STH))
                    cs2=model4light(float(STH))
                    cs3=model4moderate(float(STH))
                    cs4=model4high(float(STH))
                    feature.SetField("noyear"+str(t), cs1)
                    feature.SetField("lightyear"+str(t), cs2)
                    feature.SetField("moderyear"+str(t), cs3)
                    feature.SetField("highyear"+str(t), cs4)
                    feature.SetField("STHyear"+str(t), cs2+cs3+cs4)
                    cs=np.array([cs1,cs2,cs3,cs4])


                    #end of the loop with t

            value=prediction(time,cs,controlProgramD,controlProgramD,controlProgramD,breakpoint1,breakpoint2)
            #value=prediction(time,cs,mtp4.mtp_cp1,mtp4.mtp_cp1,mtp4.mtp_cp1,breakpoint1,breakpoint2)


            for t in (range(time)):
                if t > 0:

                    cs1=value[t][0]
                    cs2=value[t][1]
                    cs3=value[t][2]
                    cs4=value[t][3]

                    feature.SetField("noyear"+str(t), cs1)
                    feature.SetField("lightyear"+str(t), cs2)
                    feature.SetField("moderyear"+str(t), cs3)
                    feature.SetField("highyear"+str(t), cs4)
                    feature.SetField("STHyear"+str(t), cs2+cs3+cs4)



        elif feature.GetField("CATEGORY") == "E":


            for t in range(time):
                if t==0:
                    STH=feature.GetField("STH")
                    cs1=model4no(float(STH))
                    cs2=model4light(float(STH))
                    cs3=model4moderate(float(STH))
                    cs4=model4high(float(STH))
                    feature.SetField("noyear"+str(t), cs1)
                    feature.SetField("lightyear"+str(t), cs2)
                    feature.SetField("moderyear"+str(t), cs3)
                    feature.SetField("highyear"+str(t), cs4)
                    feature.SetField("STHyear"+str(t), cs2+cs3+cs4)
                    cs=np.array([cs1,cs2,cs3,cs4])


                    #end of the loop with t

            value=prediction(time,cs,controlProgramE,controlProgramE,controlProgramE,breakpoint1,breakpoint2)
            #value=prediction(time,cs,mtp4.mtp_cp1,mtp4.mtp_cp1,mtp4.mtp_cp1,breakpoint1,breakpoint2)


            for t in (range(time)):
                if t > 0:

                    cs1=value[t][0]
                    cs2=value[t][1]
                    cs3=value[t][2]
                    cs4=value[t][3]

                    feature.SetField("noyear"+str(t), cs1)
                    feature.SetField("lightyear"+str(t), cs2)
                    feature.SetField("moderyear"+str(t), cs3)
                    feature.SetField("highyear"+str(t), cs4)
                    feature.SetField("STHyear"+str(t), cs2+cs3+cs4)




        elif feature.GetField("CATEGORY") == "F":

            for t in range(time):
                if t==0:
                    STH=feature.GetField("STH")
                    cs1=model4no(float(STH))
                    cs2=model4light(float(STH))
                    cs3=model4moderate(float(STH))
                    cs4=model4high(float(STH))
                    feature.SetField("noyear"+str(t), cs1)
                    feature.SetField("lightyear"+str(t), cs2)
                    feature.SetField("moderyear"+str(t), cs3)
                    feature.SetField("highyear"+str(t), cs4)
                    feature.SetField("STHyear"+str(t), cs2+cs3+cs4)
                    cs=np.array([cs1,cs2,cs3,cs4])


                    #end of the loop with t

            value=prediction(time,cs,controlProgramF,controlProgramF,controlProgramF,breakpoint1,breakpoint2)
            #value=prediction(time,cs,mtp4.mtp_cp1,mtp4.mtp_cp1,mtp4.mtp_cp1,breakpoint1,breakpoint2)


            for t in (range(time)):
                if t > 0:

                    cs1=value[t][0]
                    cs2=value[t][1]
                    cs3=value[t][2]
                    cs4=value[t][3]

                    feature.SetField("noyear"+str(t), cs1)
                    feature.SetField("lightyear"+str(t), cs2)
                    feature.SetField("moderyear"+str(t), cs3)
                    feature.SetField("highyear"+str(t), cs4)
                    feature.SetField("STHyear"+str(t), cs2+cs3+cs4)

        layer.SetFeature(feature)
        feature.Destroy()
    # All done.
    shapefile.Destroy()
