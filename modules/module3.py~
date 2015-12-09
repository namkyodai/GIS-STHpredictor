import os,os.path,shutil
import osgeo.ogr
import osgeo.osr
from osgeo import ogr
import random
from random import randint
import numpy as np


#define the variable of the model
time=100
breakpoint1=5
breakpoint2=10

import mo3function

from mo3function import model3_moderate_HW
from mo3function import model3_light_HW
from mo3function import model3_no_HW
from mo3function import model3_high_HW
from mo3function import model3_high_Tt
from mo3function import model3_moderate_Tt
from mo3function import model3_light_Tt
from mo3function import model3_no_Tt
from mo3function import model3_high_Al
from mo3function import model3_moderate_Al
from mo3function import model3_light_Al
from mo3function import model3_no_Al
from mo3function import model3_total_HW
from mo3function import model3_total_Tt
from mo3function import model3_total_Al
from mo3function import model3_anySTH


import prediction
from prediction import prediction

import mtp3 #the file contain the pre-defined markov transition probability for model 4

def run(parameterContainer):
    # Open the source shapefile.
    shapefile = osgeo.ogr.Open(parameterContainer.targetFileLocation, 1)
    time = parameterContainer.timeStep
    layer = shapefile.GetLayer(0)

    driver = osgeo.ogr.GetDriverByName("ESRI Shapefile")

    #MH I am not sure about the following lines if they are needed since they need to be there before running the model?
    #Also the total prevalences are created randomly further down but they also need to be given beforehand, I guess?
    #define a new field called CATEGORY for user to define
    #fieldDef = osgeo.ogr.FieldDefn("CATEGORY", osgeo.ogr.OFTString)
    #fieldDef.SetWidth(10)
    #targetLayer.CreateField(fieldDef)

    #
    #this is the input of model 3
    #fieldDef = osgeo.ogr.FieldDefn("HW", osgeo.ogr.OFTString) #total prevalence of hookworm in model 3
    #fieldDef.SetWidth(5)
    #targetLayer.CreateField(fieldDef)

    #fieldDef = osgeo.ogr.FieldDefn("TT", osgeo.ogr.OFTString) #total prevalence of hookworm in model 3
    #fieldDef.SetWidth(5)
    #targetLayer.CreateField(fieldDef)

    #fieldDef = osgeo.ogr.FieldDefn("AL", osgeo.ogr.OFTString) #total prevalence of hookworm in model 3
    #fieldDef.SetWidth(5)
    #targetLayer.CreateField(fieldDef)

    words = ['HWNoyear', 'HWLiyear', 'HWModyear', 'HWHiyear', 'HWyear','TTNoyear','TTLiyear','TTMoyear','TTHiyear','TTyear','ALNoyear','ALLiyear','ALMoyear','ALHiyear','ALyear']
    for i in words:
        for t in range(time):
            fieldDef = osgeo.ogr.FieldDefn(i+str(t), osgeo.ogr.OFTReal)
            #fieldDef.SetWidth(5)
            layer.CreateField(fieldDef)


    for i in range(layer.GetFeatureCount()):
        feature=layer.GetFeature(i)
        layer.SetFeature(feature)

        #this generates randome integer value from 0 to 100 for simulation. #MH: Do we need this or should this be given by the user?
        
	#feature.SetField("HW", randint(0,100))
        #feature.SetField("TT", randint(0,100))
        #feature.SetField("AL", randint(0,100))
	#feature.SetField("STH", feature.GetField("STH")*100)

#<<<<<<< HEAD
	feature.SetField("HW", feature.GetField("HW")*1)
	feature.SetField("Tt", feature.GetField("Tt")*1)
	feature.SetField("Al", feature.GetField("Al")*1)
#=======
#	feature.SetField("HW", feature.GetField("HW")*100)
#	feature.SetField("TT", feature.GetField("TT")*100)
#	feature.SetField("AL", feature.GetField("AL")*100)
#>>>>>>> 533be90ebbafee6ae561cd32f60004fe6367577f


        #now estimate the intensity at t=0
        if feature.GetField("CATEGORY") == "A":
            for t in range(time):
                if t==0:
                    HW=feature.GetField("HW")
                    TT=feature.GetField("TT")
                    AL=feature.GetField("AL")
                    #define condition state for Hookworm
                    cs1_HW=model3_no_HW(float(HW))
                    cs2_HW=model3_light_HW(float(HW))
                    cs3_HW=model3_moderate_HW(float(HW))
                    cs4_HW=model3_high_HW(float(HW))
                    #define condition state for T.trichiura
                    cs1_Tt=model3_no_Tt(float(TT))
                    cs2_Tt=model3_light_Tt(float(TT))
                    cs3_Tt=model3_moderate_Tt(float(TT))
                    cs4_Tt=model3_high_Tt(float(TT))
                    #define condition state for A.Alumbricoin
                    cs1_Al=model3_no_Al(float(AL))
                    cs2_Al=model3_light_Al(float(AL))
                    cs3_Al=model3_moderate_Al(float(AL))
                    cs4_Al=model3_high_Al(float(AL))
                    #for anySTH
                    anySTH=model3_anySTH(float(HW),float(TT),float(AL))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("HWNoyear"+str(t), cs1_HW)
                    feature.SetField("HWLiyear"+str(t), cs2_HW)
                    feature.SetField("HWModyear"+str(t), cs3_HW)
                    feature.SetField("HWHiyear"+str(t), cs4_HW)
                    feature.SetField("HWyear"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    cs_HW=np.array([cs1_HW,cs2_HW,cs3_HW,cs4_HW])
                    #for T.trichiura
                    feature.SetField("TTNoyear"+str(t), cs1_Tt)
                    feature.SetField("TTLiyear"+str(t), cs2_Tt)
                    feature.SetField("TTMoyear"+str(t), cs3_Tt)
                    feature.SetField("TTHiyear"+str(t), cs4_Tt)
                    feature.SetField("TTyear"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    cs_Tt=np.array([cs1_Tt,cs2_Tt,cs3_Tt,cs4_Tt])
                    feature.SetField("ALNoyear"+str(t), cs1_Al)
                    feature.SetField("ALLiyear"+str(t), cs2_Al)
                    feature.SetField("ALMoyear"+str(t), cs3_Al)
                    feature.SetField("ALHiyear"+str(t), cs4_Al)
                    feature.SetField("ALyear"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STHyear"+str(t), anySTH)
                    #define conditionstate for compute with numpy package
                    cs_Al=np.array([cs1_Al,cs2_Al,cs3_Al,cs4_Al])
                    #end of the loop with t


            value_HW=prediction(time,cs_HW,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)
            value_Tt=prediction(time,cs_Tt,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)
            value_Al=prediction(time,cs_Al,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)


            for t in (range(time)):
                if t > 0:
                    cs1_HW=value_HW[t][0]
                    cs2_HW=value_HW[t][1]
                    cs3_HW=value_HW[t][2]
                    cs4_HW=value_HW[t][3]
                    cs1_Tt=value_Tt[t][0]
                    cs2_Tt=value_Tt[t][1]
                    cs3_Tt=value_Tt[t][2]
                    cs4_Tt=value_Tt[t][3]
                    cs1_Al=value_Al[t][0]
                    cs2_Al=value_Al[t][1]
                    cs3_Al=value_Al[t][2]
                    cs4_Al=value_Al[t][3]
                    #for anySTH
                    anySTH=model3_anySTH((cs2_HW+cs3_HW+cs4_HW),(cs2_Tt+cs3_Tt+cs4_Tt),(cs2_Al+cs3_Al+cs4_Al))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("HWNoyear"+str(t), cs1_HW)
                    feature.SetField("HWLiyear"+str(t), cs2_HW)
                    feature.SetField("HWModyear"+str(t), cs3_HW)
                    feature.SetField("HWHiyear"+str(t), cs4_HW)
                    feature.SetField("HWyear"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    #for T.trichiura
                    feature.SetField("TTNoyear"+str(t), cs1_Tt)
                    feature.SetField("TTLiyear"+str(t), cs2_Tt)
                    feature.SetField("TTMoyear"+str(t), cs3_Tt)
                    feature.SetField("TTHiyear"+str(t), cs4_Tt)
                    feature.SetField("TTyear"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    feature.SetField("ALNoyear"+str(t), cs1_Al)
                    feature.SetField("ALLiyear"+str(t), cs2_Al)
                    feature.SetField("ALMoyear"+str(t), cs3_Al)
                    feature.SetField("ALHiyear"+str(t), cs4_Al)
                    feature.SetField("ALyear"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STHyear"+str(t), anySTH)


        elif feature.GetField("CATEGORY") == "B":
            for t in range(time):
                if t==0:
                    HW=feature.GetField("HW")
                    TT=feature.GetField("TT")
                    AL=feature.GetField("AL")
                    #define condition state for Hookworm
                    cs1_HW=model3_no_HW(float(HW))
                    cs2_HW=model3_light_HW(float(HW))
                    cs3_HW=model3_moderate_HW(float(HW))
                    cs4_HW=model3_high_HW(float(HW))
                    #define condition state for T.trichiura
                    cs1_Tt=model3_no_Tt(float(TT))
                    cs2_Tt=model3_light_Tt(float(TT))
                    cs3_Tt=model3_moderate_Tt(float(TT))
                    cs4_Tt=model3_high_Tt(float(TT))
                    #define condition state for A.Alumbricoin
                    cs1_Al=model3_no_Al(float(AL))
                    cs2_Al=model3_light_Al(float(AL))
                    cs3_Al=model3_moderate_Al(float(AL))
                    cs4_Al=model3_high_Al(float(AL))
                    #for anySTH
                    anySTH=model3_anySTH(float(HW),float(TT),float(AL))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("HWNoyear"+str(t), cs1_HW)
                    feature.SetField("HWLiyear"+str(t), cs2_HW)
                    feature.SetField("HWModyear"+str(t), cs3_HW)
                    feature.SetField("HWHiyear"+str(t), cs4_HW)
                    feature.SetField("HWyear"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    cs_HW=np.array([cs1_HW,cs2_HW,cs3_HW,cs4_HW])
                    #for T.trichiura
                    feature.SetField("TTNoyear"+str(t), cs1_Tt)
                    feature.SetField("TTLiyear"+str(t), cs2_Tt)
                    feature.SetField("TTMoyear"+str(t), cs3_Tt)
                    feature.SetField("TTHiyear"+str(t), cs4_Tt)
                    feature.SetField("TTyear"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    cs_Tt=np.array([cs1_Tt,cs2_Tt,cs3_Tt,cs4_Tt])
                    feature.SetField("ALNoyear"+str(t), cs1_Al)
                    feature.SetField("ALLiyear"+str(t), cs2_Al)
                    feature.SetField("ALMoyear"+str(t), cs3_Al)
                    feature.SetField("ALHiyear"+str(t), cs4_Al)
                    feature.SetField("ALyear"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STHyear"+str(t), anySTH)
                    #define conditionstate for compute with numpy package
                    cs_Al=np.array([cs1_Al,cs2_Al,cs3_Al,cs4_Al])
                    #end of the loop with t


            value_HW=prediction(time,cs_HW,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)
            value_Tt=prediction(time,cs_Tt,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)
            value_Al=prediction(time,cs_Al,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)


            for t in (range(time)):
                if t > 0:
                    cs1_HW=value_HW[t][0]
                    cs2_HW=value_HW[t][1]
                    cs3_HW=value_HW[t][2]
                    cs4_HW=value_HW[t][3]
                    cs1_Tt=value_Tt[t][0]
                    cs2_Tt=value_Tt[t][1]
                    cs3_Tt=value_Tt[t][2]
                    cs4_Tt=value_Tt[t][3]
                    cs1_Al=value_Al[t][0]
                    cs2_Al=value_Al[t][1]
                    cs3_Al=value_Al[t][2]
                    cs4_Al=value_Al[t][3]
                    #for anySTH
                    anySTH=model3_anySTH((cs2_HW+cs3_HW+cs4_HW),(cs2_Tt+cs3_Tt+cs4_Tt),(cs2_Al+cs3_Al+cs4_Al))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("HWNoyear"+str(t), cs1_HW)
                    feature.SetField("HWLiyear"+str(t), cs2_HW)
                    feature.SetField("HWModyear"+str(t), cs3_HW)
                    feature.SetField("HWHiyear"+str(t), cs4_HW)
                    feature.SetField("HWyear"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    #for T.trichiura
                    feature.SetField("TTNoyear"+str(t), cs1_Tt)
                    feature.SetField("TTLiyear"+str(t), cs2_Tt)
                    feature.SetField("TTMoyear"+str(t), cs3_Tt)
                    feature.SetField("TTHiyear"+str(t), cs4_Tt)
                    feature.SetField("TTyear"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    feature.SetField("ALNoyear"+str(t), cs1_Al)
                    feature.SetField("ALLiyear"+str(t), cs2_Al)
                    feature.SetField("ALMoyear"+str(t), cs3_Al)
                    feature.SetField("ALHiyear"+str(t), cs4_Al)
                    feature.SetField("ALyear"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STHyear"+str(t), anySTH)




        elif feature.GetField("CATEGORY") == "C":
            for t in range(time):
                if t==0:
                    HW=feature.GetField("HW")
                    TT=feature.GetField("TT")
                    AL=feature.GetField("AL")
                    #define condition state for Hookworm
                    cs1_HW=model3_no_HW(float(HW))
                    cs2_HW=model3_light_HW(float(HW))
                    cs3_HW=model3_moderate_HW(float(HW))
                    cs4_HW=model3_high_HW(float(HW))
                    #define condition state for T.trichiura
                    cs1_Tt=model3_no_Tt(float(TT))
                    cs2_Tt=model3_light_Tt(float(TT))
                    cs3_Tt=model3_moderate_Tt(float(TT))
                    cs4_Tt=model3_high_Tt(float(TT))
                    #define condition state for A.Alumbricoin
                    cs1_Al=model3_no_Al(float(AL))
                    cs2_Al=model3_light_Al(float(AL))
                    cs3_Al=model3_moderate_Al(float(AL))
                    cs4_Al=model3_high_Al(float(AL))
                    #for anySTH
                    anySTH=model3_anySTH(float(HW),float(TT),float(AL))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("HWNoyear"+str(t), cs1_HW)
                    feature.SetField("HWLiyear"+str(t), cs2_HW)
                    feature.SetField("HWModyear"+str(t), cs3_HW)
                    feature.SetField("HWHiyear"+str(t), cs4_HW)
                    feature.SetField("HWyear"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    cs_HW=np.array([cs1_HW,cs2_HW,cs3_HW,cs4_HW])
                    #for T.trichiura
                    feature.SetField("TTNoyear"+str(t), cs1_Tt)
                    feature.SetField("TTLiyear"+str(t), cs2_Tt)
                    feature.SetField("TTMoyear"+str(t), cs3_Tt)
                    feature.SetField("TTHiyear"+str(t), cs4_Tt)
                    feature.SetField("TTyear"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    cs_Tt=np.array([cs1_Tt,cs2_Tt,cs3_Tt,cs4_Tt])
                    feature.SetField("ALNoyear"+str(t), cs1_Al)
                    feature.SetField("ALLiyear"+str(t), cs2_Al)
                    feature.SetField("ALMoyear"+str(t), cs3_Al)
                    feature.SetField("ALHiyear"+str(t), cs4_Al)
                    feature.SetField("ALyear"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STHyear"+str(t), anySTH)
                    #define conditionstate for compute with numpy package
                    cs_Al=np.array([cs1_Al,cs2_Al,cs3_Al,cs4_Al])
                    #end of the loop with t


            value_HW=prediction(time,cs_HW,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)
            value_Tt=prediction(time,cs_Tt,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)
            value_Al=prediction(time,cs_Al,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)


            for t in (range(time)):
                if t > 0:
                    cs1_HW=value_HW[t][0]
                    cs2_HW=value_HW[t][1]
                    cs3_HW=value_HW[t][2]
                    cs4_HW=value_HW[t][3]
                    cs1_Tt=value_Tt[t][0]
                    cs2_Tt=value_Tt[t][1]
                    cs3_Tt=value_Tt[t][2]
                    cs4_Tt=value_Tt[t][3]
                    cs1_Al=value_Al[t][0]
                    cs2_Al=value_Al[t][1]
                    cs3_Al=value_Al[t][2]
                    cs4_Al=value_Al[t][3]
                    #for anySTH
                    anySTH=model3_anySTH((cs2_HW+cs3_HW+cs4_HW),(cs2_Tt+cs3_Tt+cs4_Tt),(cs2_Al+cs3_Al+cs4_Al))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("HWNoyear"+str(t), cs1_HW)
                    feature.SetField("HWLiyear"+str(t), cs2_HW)
                    feature.SetField("HWModyear"+str(t), cs3_HW)
                    feature.SetField("HWHiyear"+str(t), cs4_HW)
                    feature.SetField("HWyear"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    #for T.trichiura
                    feature.SetField("TTNoyear"+str(t), cs1_Tt)
                    feature.SetField("TTLiyear"+str(t), cs2_Tt)
                    feature.SetField("TTMoyear"+str(t), cs3_Tt)
                    feature.SetField("TTHiyear"+str(t), cs4_Tt)
                    feature.SetField("TTyear"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    feature.SetField("ALNoyear"+str(t), cs1_Al)
                    feature.SetField("ALLiyear"+str(t), cs2_Al)
                    feature.SetField("ALMoyear"+str(t), cs3_Al)
                    feature.SetField("ALHiyear"+str(t), cs4_Al)
                    feature.SetField("ALyear"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STHyear"+str(t), anySTH)


        elif feature.GetField("CATEGORY") == "D":
            for t in range(time):
                if t==0:
                    HW=feature.GetField("HW")
                    TT=feature.GetField("TT")
                    AL=feature.GetField("AL")
                    #define condition state for Hookworm
                    cs1_HW=model3_no_HW(float(HW))
                    cs2_HW=model3_light_HW(float(HW))
                    cs3_HW=model3_moderate_HW(float(HW))
                    cs4_HW=model3_high_HW(float(HW))
                    #define condition state for T.trichiura
                    cs1_Tt=model3_no_Tt(float(TT))
                    cs2_Tt=model3_light_Tt(float(TT))
                    cs3_Tt=model3_moderate_Tt(float(TT))
                    cs4_Tt=model3_high_Tt(float(TT))
                    #define condition state for A.Alumbricoin
                    cs1_Al=model3_no_Al(float(AL))
                    cs2_Al=model3_light_Al(float(AL))
                    cs3_Al=model3_moderate_Al(float(AL))
                    cs4_Al=model3_high_Al(float(AL))
                    #for anySTH
                    anySTH=model3_anySTH(float(HW),float(TT),float(AL))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("HWNoyear"+str(t), cs1_HW)
                    feature.SetField("HWLiyear"+str(t), cs2_HW)
                    feature.SetField("HWModyear"+str(t), cs3_HW)
                    feature.SetField("HWHiyear"+str(t), cs4_HW)
                    feature.SetField("HWyear"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    cs_HW=np.array([cs1_HW,cs2_HW,cs3_HW,cs4_HW])
                    #for T.trichiura
                    feature.SetField("TTNoyear"+str(t), cs1_Tt)
                    feature.SetField("TTLiyear"+str(t), cs2_Tt)
                    feature.SetField("TTMoyear"+str(t), cs3_Tt)
                    feature.SetField("TTHiyear"+str(t), cs4_Tt)
                    feature.SetField("TTyear"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    cs_Tt=np.array([cs1_Tt,cs2_Tt,cs3_Tt,cs4_Tt])
                    feature.SetField("ALNoyear"+str(t), cs1_Al)
                    feature.SetField("ALLiyear"+str(t), cs2_Al)
                    feature.SetField("ALMoyear"+str(t), cs3_Al)
                    feature.SetField("ALHiyear"+str(t), cs4_Al)
                    feature.SetField("ALyear"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STHyear"+str(t), anySTH)
                    #define conditionstate for compute with numpy package
                    cs_Al=np.array([cs1_Al,cs2_Al,cs3_Al,cs4_Al])
                    #end of the loop with t


            value_HW=prediction(time,cs_HW,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)
            value_Tt=prediction(time,cs_Tt,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)
            value_Al=prediction(time,cs_Al,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)


            for t in (range(time)):
                if t > 0:
                    cs1_HW=value_HW[t][0]
                    cs2_HW=value_HW[t][1]
                    cs3_HW=value_HW[t][2]
                    cs4_HW=value_HW[t][3]
                    cs1_Tt=value_Tt[t][0]
                    cs2_Tt=value_Tt[t][1]
                    cs3_Tt=value_Tt[t][2]
                    cs4_Tt=value_Tt[t][3]
                    cs1_Al=value_Al[t][0]
                    cs2_Al=value_Al[t][1]
                    cs3_Al=value_Al[t][2]
                    cs4_Al=value_Al[t][3]
                    #for anySTH
                    anySTH=model3_anySTH((cs2_HW+cs3_HW+cs4_HW),(cs2_Tt+cs3_Tt+cs4_Tt),(cs2_Al+cs3_Al+cs4_Al))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("HWNoyear"+str(t), cs1_HW)
                    feature.SetField("HWLiyear"+str(t), cs2_HW)
                    feature.SetField("HWModyear"+str(t), cs3_HW)
                    feature.SetField("HWHiyear"+str(t), cs4_HW)
                    feature.SetField("HWyear"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    #for T.trichiura
                    feature.SetField("TTNoyear"+str(t), cs1_Tt)
                    feature.SetField("TTLiyear"+str(t), cs2_Tt)
                    feature.SetField("TTMoyear"+str(t), cs3_Tt)
                    feature.SetField("TTHiyear"+str(t), cs4_Tt)
                    feature.SetField("TTyear"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    feature.SetField("ALNoyear"+str(t), cs1_Al)
                    feature.SetField("ALLiyear"+str(t), cs2_Al)
                    feature.SetField("ALMoyear"+str(t), cs3_Al)
                    feature.SetField("ALHiyear"+str(t), cs4_Al)
                    feature.SetField("ALyear"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STHyear"+str(t), anySTH)


        elif feature.GetField("CATEGORY") == "E":
            for t in range(time):
                if t==0:
                    HW=feature.GetField("HW")
                    TT=feature.GetField("TT")
                    AL=feature.GetField("AL")
                    #define condition state for Hookworm
                    cs1_HW=model3_no_HW(float(HW))
                    cs2_HW=model3_light_HW(float(HW))
                    cs3_HW=model3_moderate_HW(float(HW))
                    cs4_HW=model3_high_HW(float(HW))
                    #define condition state for T.trichiura
                    cs1_Tt=model3_no_Tt(float(TT))
                    cs2_Tt=model3_light_Tt(float(TT))
                    cs3_Tt=model3_moderate_Tt(float(TT))
                    cs4_Tt=model3_high_Tt(float(TT))
                    #define condition state for A.Alumbricoin
                    cs1_Al=model3_no_Al(float(AL))
                    cs2_Al=model3_light_Al(float(AL))
                    cs3_Al=model3_moderate_Al(float(AL))
                    cs4_Al=model3_high_Al(float(AL))
                    #for anySTH
                    anySTH=model3_anySTH(float(HW),float(TT),float(AL))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("HWNoyear"+str(t), cs1_HW)
                    feature.SetField("HWLiyear"+str(t), cs2_HW)
                    feature.SetField("HWModyear"+str(t), cs3_HW)
                    feature.SetField("HWHiyear"+str(t), cs4_HW)
                    feature.SetField("HWyear"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    cs_HW=np.array([cs1_HW,cs2_HW,cs3_HW,cs4_HW])
                    #for T.trichiura
                    feature.SetField("TTNoyear"+str(t), cs1_Tt)
                    feature.SetField("TTLiyear"+str(t), cs2_Tt)
                    feature.SetField("TTMoyear"+str(t), cs3_Tt)
                    feature.SetField("TTHiyear"+str(t), cs4_Tt)
                    feature.SetField("TTyear"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    cs_Tt=np.array([cs1_Tt,cs2_Tt,cs3_Tt,cs4_Tt])
                    feature.SetField("ALNoyear"+str(t), cs1_Al)
                    feature.SetField("ALLiyear"+str(t), cs2_Al)
                    feature.SetField("ALMoyear"+str(t), cs3_Al)
                    feature.SetField("ALHiyear"+str(t), cs4_Al)
                    feature.SetField("ALyear"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STHyear"+str(t), anySTH)
                    #define conditionstate for compute with numpy package
                    cs_Al=np.array([cs1_Al,cs2_Al,cs3_Al,cs4_Al])
                    #end of the loop with t


            value_HW=prediction(time,cs_HW,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)
            value_Tt=prediction(time,cs_Tt,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)
            value_Al=prediction(time,cs_Al,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)


            for t in (range(time)):
                if t > 0:
                    cs1_HW=value_HW[t][0]
                    cs2_HW=value_HW[t][1]
                    cs3_HW=value_HW[t][2]
                    cs4_HW=value_HW[t][3]
                    cs1_Tt=value_Tt[t][0]
                    cs2_Tt=value_Tt[t][1]
                    cs3_Tt=value_Tt[t][2]
                    cs4_Tt=value_Tt[t][3]
                    cs1_Al=value_Al[t][0]
                    cs2_Al=value_Al[t][1]
                    cs3_Al=value_Al[t][2]
                    cs4_Al=value_Al[t][3]
                    #for anySTH
                    anySTH=model3_anySTH((cs2_HW+cs3_HW+cs4_HW),(cs2_Tt+cs3_Tt+cs4_Tt),(cs2_Al+cs3_Al+cs4_Al))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("HWNoyear"+str(t), cs1_HW)
                    feature.SetField("HWLiyear"+str(t), cs2_HW)
                    feature.SetField("HWModyear"+str(t), cs3_HW)
                    feature.SetField("HWHiyear"+str(t), cs4_HW)
                    feature.SetField("HWyear"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    #for T.trichiura
                    feature.SetField("TTNoyear"+str(t), cs1_Tt)
                    feature.SetField("TTLiyear"+str(t), cs2_Tt)
                    feature.SetField("TTMoyear"+str(t), cs3_Tt)
                    feature.SetField("TTHiyear"+str(t), cs4_Tt)
                    feature.SetField("TTyear"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    feature.SetField("ALNoyear"+str(t), cs1_Al)
                    feature.SetField("ALLiyear"+str(t), cs2_Al)
                    feature.SetField("ALMoyear"+str(t), cs3_Al)
                    feature.SetField("ALHiyear"+str(t), cs4_Al)
                    feature.SetField("ALyear"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STHyear"+str(t), anySTH)



        elif feature.GetField("CATEGORY") == "F":
            for t in range(time):
                if t==0:
                    HW=feature.GetField("HW")
                    TT=feature.GetField("TT")
                    AL=feature.GetField("AL")
                    #define condition state for Hookworm
                    cs1_HW=model3_no_HW(float(HW))
                    cs2_HW=model3_light_HW(float(HW))
                    cs3_HW=model3_moderate_HW(float(HW))
                    cs4_HW=model3_high_HW(float(HW))
                    #define condition state for T.trichiura
                    cs1_Tt=model3_no_Tt(float(TT))
                    cs2_Tt=model3_light_Tt(float(TT))
                    cs3_Tt=model3_moderate_Tt(float(TT))
                    cs4_Tt=model3_high_Tt(float(TT))
                    #define condition state for A.Alumbricoin
                    cs1_Al=model3_no_Al(float(AL))
                    cs2_Al=model3_light_Al(float(AL))
                    cs3_Al=model3_moderate_Al(float(AL))
                    cs4_Al=model3_high_Al(float(AL))
                    #for anySTH
                    anySTH=model3_anySTH(float(HW),float(TT),float(AL))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("HWNoyear"+str(t), cs1_HW)
                    feature.SetField("HWLiyear"+str(t), cs2_HW)
                    feature.SetField("HWModyear"+str(t), cs3_HW)
                    feature.SetField("HWHiyear"+str(t), cs4_HW)
                    feature.SetField("HWyear"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    cs_HW=np.array([cs1_HW,cs2_HW,cs3_HW,cs4_HW])
                    #for T.trichiura
                    feature.SetField("TTNoyear"+str(t), cs1_Tt)
                    feature.SetField("TTLiyear"+str(t), cs2_Tt)
                    feature.SetField("TTMoyear"+str(t), cs3_Tt)
                    feature.SetField("TTHiyear"+str(t), cs4_Tt)
                    feature.SetField("TTyear"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    cs_Tt=np.array([cs1_Tt,cs2_Tt,cs3_Tt,cs4_Tt])
                    feature.SetField("ALNoyear"+str(t), cs1_Al)
                    feature.SetField("ALLiyear"+str(t), cs2_Al)
                    feature.SetField("ALMoyear"+str(t), cs3_Al)
                    feature.SetField("ALHiyear"+str(t), cs4_Al)
                    feature.SetField("ALyear"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STHyear"+str(t), anySTH)
                    #define conditionstate for compute with numpy package
                    cs_Al=np.array([cs1_Al,cs2_Al,cs3_Al,cs4_Al])
                    #end of the loop with t


            value_HW=prediction(time,cs_HW,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)
            value_Tt=prediction(time,cs_Tt,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)
            value_Al=prediction(time,cs_Al,mtp3.mtp_cp1,mtp3.mtp_cp1,mtp3.mtp_cp1,breakpoint1,breakpoint2)


            for t in (range(time)):
                if t > 0:
                    cs1_HW=value_HW[t][0]
                    cs2_HW=value_HW[t][1]
                    cs3_HW=value_HW[t][2]
                    cs4_HW=value_HW[t][3]
                    cs1_Tt=value_Tt[t][0]
                    cs2_Tt=value_Tt[t][1]
                    cs3_Tt=value_Tt[t][2]
                    cs4_Tt=value_Tt[t][3]
                    cs1_Al=value_Al[t][0]
                    cs2_Al=value_Al[t][1]
                    cs3_Al=value_Al[t][2]
                    cs4_Al=value_Al[t][3]
                    #for anySTH
                    anySTH=model3_anySTH((cs2_HW+cs3_HW+cs4_HW),(cs2_Tt+cs3_Tt+cs4_Tt),(cs2_Al+cs3_Al+cs4_Al))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("HWNoyear"+str(t), cs1_HW)
                    feature.SetField("HWLiyear"+str(t), cs2_HW)
                    feature.SetField("HWModyear"+str(t), cs3_HW)
                    feature.SetField("HWHiyear"+str(t), cs4_HW)
                    feature.SetField("HWyear"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    #for T.trichiura
                    feature.SetField("TTNoyear"+str(t), cs1_Tt)
                    feature.SetField("TTLiyear"+str(t), cs2_Tt)
                    feature.SetField("TTMoyear"+str(t), cs3_Tt)
                    feature.SetField("TTHiyear"+str(t), cs4_Tt)
                    feature.SetField("TTyear"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    feature.SetField("ALNoyear"+str(t), cs1_Al)
                    feature.SetField("ALLiyear"+str(t), cs2_Al)
                    feature.SetField("ALMoyear"+str(t), cs3_Al)
                    feature.SetField("ALHiyear"+str(t), cs4_Al)
                    feature.SetField("ALyear"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STHyear"+str(t), anySTH)

        layer.SetFeature(feature)
        feature.Destroy()
    # All done.
    shapefile.Destroy()
    #import mtp4
