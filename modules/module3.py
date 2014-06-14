import os,os.path,shutil
import osgeo.ogr
import osgeo.osr
from osgeo import ogr
import random
from random import randint
import numpy as np


#define the variable of the model
time=10
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
    #fieldDef = osgeo.ogr.FieldDefn("HW_3", osgeo.ogr.OFTString) #total prevalence of hookworm in model 3
    #fieldDef.SetWidth(5)
    #targetLayer.CreateField(fieldDef)

    #fieldDef = osgeo.ogr.FieldDefn("Tt_3", osgeo.ogr.OFTString) #total prevalence of hookworm in model 3
    #fieldDef.SetWidth(5)
    #targetLayer.CreateField(fieldDef)

    #fieldDef = osgeo.ogr.FieldDefn("Al_3", osgeo.ogr.OFTString) #total prevalence of hookworm in model 3
    #fieldDef.SetWidth(5)
    #targetLayer.CreateField(fieldDef)


    for t in range(time):
        #define the field for Hookworm
        fieldDef = osgeo.ogr.FieldDefn("H_n_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        fieldDef = osgeo.ogr.FieldDefn("H_l_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        fieldDef = osgeo.ogr.FieldDefn("H_m_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        fieldDef = osgeo.ogr.FieldDefn("H_h_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        fieldDef = osgeo.ogr.FieldDefn("HW_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        #define the field for T.trichiura
        fieldDef = osgeo.ogr.FieldDefn("T_n_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        fieldDef = osgeo.ogr.FieldDefn("T_l_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        fieldDef = osgeo.ogr.FieldDefn("T_m_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        fieldDef = osgeo.ogr.FieldDefn("T_h_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        fieldDef = osgeo.ogr.FieldDefn("Tt_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        #define the field for A.lumbricoides
        fieldDef = osgeo.ogr.FieldDefn("A_n_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        fieldDef = osgeo.ogr.FieldDefn("A_l_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        fieldDef = osgeo.ogr.FieldDefn("A_m_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        fieldDef = osgeo.ogr.FieldDefn("A_h_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        fieldDef = osgeo.ogr.FieldDefn("Al_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)
        #for anySTH
        fieldDef = osgeo.ogr.FieldDefn("STH_3_"+str(t), osgeo.ogr.OFTReal)
        fieldDef.SetWidth(5)
        layer.CreateField(fieldDef)




    for i in range(layer.GetFeatureCount()):
        feature=layer.GetFeature(i)
        layer.SetFeature(feature)

        #this generates randome integer value from 0 to 100 for simulation. #MH: Do we need this or should this be given by the user?
        feature.SetField("HW_3", randint(0,100))
        feature.SetField("Tt_3", randint(0,100))
        feature.SetField("Al_3", randint(0,100))

        #now estimate the intensity at t=0
        if feature.GetField("CATEGORY") == "A":
            for t in range(time):
                if t==0:
                    HW_3=feature.GetField("HW_3")
                    Tt_3=feature.GetField("Tt_3")
                    Al_3=feature.GetField("Al_3")
                    #define condition state for Hookworm
                    cs1_HW=model3_no_HW(float(HW_3))
                    cs2_HW=model3_light_HW(float(HW_3))
                    cs3_HW=model3_moderate_HW(float(HW_3))
                    cs4_HW=model3_high_HW(float(HW_3))
                    #define condition state for T.trichiura
                    cs1_Tt=model3_no_Tt(float(Tt_3))
                    cs2_Tt=model3_light_Tt(float(Tt_3))
                    cs3_Tt=model3_moderate_Tt(float(Tt_3))
                    cs4_Tt=model3_high_Tt(float(Tt_3))
                    #define condition state for A.Alumbricoin
                    cs1_Al=model3_no_Al(float(Al_3))
                    cs2_Al=model3_light_Al(float(Al_3))
                    cs3_Al=model3_moderate_Al(float(Al_3))
                    cs4_Al=model3_high_Al(float(Al_3))
                    #for anySTH
                    anySTH=model3_anySTH(float(HW_3),float(Tt_3),float(Al_3))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("H_n_3_"+str(t), cs1_HW)
                    feature.SetField("H_l_3_"+str(t), cs2_HW)
                    feature.SetField("H_m_3_"+str(t), cs3_HW)
                    feature.SetField("H_h_3_"+str(t), cs4_HW)
                    feature.SetField("HW_3_"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    cs_HW=np.array([cs1_HW,cs2_HW,cs3_HW,cs4_HW])
                    #for T.trichiura
                    feature.SetField("T_n_3_"+str(t), cs1_Tt)
                    feature.SetField("T_l_3_"+str(t), cs2_Tt)
                    feature.SetField("T_m_3_"+str(t), cs3_Tt)
                    feature.SetField("T_h_3_"+str(t), cs4_Tt)
                    feature.SetField("Tt_3_"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    cs_Tt=np.array([cs1_Tt,cs2_Tt,cs3_Tt,cs4_Tt])
                    feature.SetField("A_n_3_"+str(t), cs1_Al)
                    feature.SetField("A_l_3_"+str(t), cs2_Al)
                    feature.SetField("A_m_3_"+str(t), cs3_Al)
                    feature.SetField("A_h_3_"+str(t), cs4_Al)
                    feature.SetField("Al_3_"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STH_3_"+str(t), anySTH)
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
                    feature.SetField("H_n_3_"+str(t), cs1_HW)
                    feature.SetField("H_l_3_"+str(t), cs2_HW)
                    feature.SetField("H_m_3_"+str(t), cs3_HW)
                    feature.SetField("H_h_3_"+str(t), cs4_HW)
                    feature.SetField("HW_3_"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    #for T.trichiura
                    feature.SetField("T_n_3_"+str(t), cs1_Tt)
                    feature.SetField("T_l_3_"+str(t), cs2_Tt)
                    feature.SetField("T_m_3_"+str(t), cs3_Tt)
                    feature.SetField("T_h_3_"+str(t), cs4_Tt)
                    feature.SetField("Tt_3_"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    feature.SetField("A_n_3_"+str(t), cs1_Al)
                    feature.SetField("A_l_3_"+str(t), cs2_Al)
                    feature.SetField("A_m_3_"+str(t), cs3_Al)
                    feature.SetField("A_h_3_"+str(t), cs4_Al)
                    feature.SetField("Al_3_"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STH_3_"+str(t), anySTH)


        elif feature.GetField("CATEGORY") == "B":
            for t in range(time):
                if t==0:
                    HW_3=feature.GetField("HW_3")
                    Tt_3=feature.GetField("Tt_3")
                    Al_3=feature.GetField("Al_3")
                    #define condition state for Hookworm
                    cs1_HW=model3_no_HW(float(HW_3))
                    cs2_HW=model3_light_HW(float(HW_3))
                    cs3_HW=model3_moderate_HW(float(HW_3))
                    cs4_HW=model3_high_HW(float(HW_3))
                    #define condition state for T.trichiura
                    cs1_Tt=model3_no_Tt(float(Tt_3))
                    cs2_Tt=model3_light_Tt(float(Tt_3))
                    cs3_Tt=model3_moderate_Tt(float(Tt_3))
                    cs4_Tt=model3_high_Tt(float(Tt_3))
                    #define condition state for A.Alumbricoin
                    cs1_Al=model3_no_Al(float(Al_3))
                    cs2_Al=model3_light_Al(float(Al_3))
                    cs3_Al=model3_moderate_Al(float(Al_3))
                    cs4_Al=model3_high_Al(float(Al_3))
                    #for anySTH
                    anySTH=model3_anySTH(float(HW_3),float(Tt_3),float(Al_3))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("H_n_3_"+str(t), cs1_HW)
                    feature.SetField("H_l_3_"+str(t), cs2_HW)
                    feature.SetField("H_m_3_"+str(t), cs3_HW)
                    feature.SetField("H_h_3_"+str(t), cs4_HW)
                    feature.SetField("HW_3_"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    cs_HW=np.array([cs1_HW,cs2_HW,cs3_HW,cs4_HW])
                    #for T.trichiura
                    feature.SetField("T_n_3_"+str(t), cs1_Tt)
                    feature.SetField("T_l_3_"+str(t), cs2_Tt)
                    feature.SetField("T_m_3_"+str(t), cs3_Tt)
                    feature.SetField("T_h_3_"+str(t), cs4_Tt)
                    feature.SetField("Tt_3_"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    cs_Tt=np.array([cs1_Tt,cs2_Tt,cs3_Tt,cs4_Tt])
                    feature.SetField("A_n_3_"+str(t), cs1_Al)
                    feature.SetField("A_l_3_"+str(t), cs2_Al)
                    feature.SetField("A_m_3_"+str(t), cs3_Al)
                    feature.SetField("A_h_3_"+str(t), cs4_Al)
                    feature.SetField("Al_3_"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STH_3_"+str(t), anySTH)
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
                    feature.SetField("H_n_3_"+str(t), cs1_HW)
                    feature.SetField("H_l_3_"+str(t), cs2_HW)
                    feature.SetField("H_m_3_"+str(t), cs3_HW)
                    feature.SetField("H_h_3_"+str(t), cs4_HW)
                    feature.SetField("HW_3_"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    #for T.trichiura
                    feature.SetField("T_n_3_"+str(t), cs1_Tt)
                    feature.SetField("T_l_3_"+str(t), cs2_Tt)
                    feature.SetField("T_m_3_"+str(t), cs3_Tt)
                    feature.SetField("T_h_3_"+str(t), cs4_Tt)
                    feature.SetField("Tt_3_"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    feature.SetField("A_n_3_"+str(t), cs1_Al)
                    feature.SetField("A_l_3_"+str(t), cs2_Al)
                    feature.SetField("A_m_3_"+str(t), cs3_Al)
                    feature.SetField("A_h_3_"+str(t), cs4_Al)
                    feature.SetField("Al_3_"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STH_3_"+str(t), anySTH)




        elif feature.GetField("CATEGORY") == "C":
            for t in range(time):
                if t==0:
                    HW_3=feature.GetField("HW_3")
                    Tt_3=feature.GetField("Tt_3")
                    Al_3=feature.GetField("Al_3")
                    #define condition state for Hookworm
                    cs1_HW=model3_no_HW(float(HW_3))
                    cs2_HW=model3_light_HW(float(HW_3))
                    cs3_HW=model3_moderate_HW(float(HW_3))
                    cs4_HW=model3_high_HW(float(HW_3))
                    #define condition state for T.trichiura
                    cs1_Tt=model3_no_Tt(float(Tt_3))
                    cs2_Tt=model3_light_Tt(float(Tt_3))
                    cs3_Tt=model3_moderate_Tt(float(Tt_3))
                    cs4_Tt=model3_high_Tt(float(Tt_3))
                    #define condition state for A.Alumbricoin
                    cs1_Al=model3_no_Al(float(Al_3))
                    cs2_Al=model3_light_Al(float(Al_3))
                    cs3_Al=model3_moderate_Al(float(Al_3))
                    cs4_Al=model3_high_Al(float(Al_3))
                    #for anySTH
                    anySTH=model3_anySTH(float(HW_3),float(Tt_3),float(Al_3))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("H_n_3_"+str(t), cs1_HW)
                    feature.SetField("H_l_3_"+str(t), cs2_HW)
                    feature.SetField("H_m_3_"+str(t), cs3_HW)
                    feature.SetField("H_h_3_"+str(t), cs4_HW)
                    feature.SetField("HW_3_"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    cs_HW=np.array([cs1_HW,cs2_HW,cs3_HW,cs4_HW])
                    #for T.trichiura
                    feature.SetField("T_n_3_"+str(t), cs1_Tt)
                    feature.SetField("T_l_3_"+str(t), cs2_Tt)
                    feature.SetField("T_m_3_"+str(t), cs3_Tt)
                    feature.SetField("T_h_3_"+str(t), cs4_Tt)
                    feature.SetField("Tt_3_"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    cs_Tt=np.array([cs1_Tt,cs2_Tt,cs3_Tt,cs4_Tt])
                    feature.SetField("A_n_3_"+str(t), cs1_Al)
                    feature.SetField("A_l_3_"+str(t), cs2_Al)
                    feature.SetField("A_m_3_"+str(t), cs3_Al)
                    feature.SetField("A_h_3_"+str(t), cs4_Al)
                    feature.SetField("Al_3_"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STH_3_"+str(t), anySTH)
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
                    feature.SetField("H_n_3_"+str(t), cs1_HW)
                    feature.SetField("H_l_3_"+str(t), cs2_HW)
                    feature.SetField("H_m_3_"+str(t), cs3_HW)
                    feature.SetField("H_h_3_"+str(t), cs4_HW)
                    feature.SetField("HW_3_"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    #for T.trichiura
                    feature.SetField("T_n_3_"+str(t), cs1_Tt)
                    feature.SetField("T_l_3_"+str(t), cs2_Tt)
                    feature.SetField("T_m_3_"+str(t), cs3_Tt)
                    feature.SetField("T_h_3_"+str(t), cs4_Tt)
                    feature.SetField("Tt_3_"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    feature.SetField("A_n_3_"+str(t), cs1_Al)
                    feature.SetField("A_l_3_"+str(t), cs2_Al)
                    feature.SetField("A_m_3_"+str(t), cs3_Al)
                    feature.SetField("A_h_3_"+str(t), cs4_Al)
                    feature.SetField("Al_3_"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STH_3_"+str(t), anySTH)


        elif feature.GetField("CATEGORY") == "D":
            for t in range(time):
                if t==0:
                    HW_3=feature.GetField("HW_3")
                    Tt_3=feature.GetField("Tt_3")
                    Al_3=feature.GetField("Al_3")
                    #define condition state for Hookworm
                    cs1_HW=model3_no_HW(float(HW_3))
                    cs2_HW=model3_light_HW(float(HW_3))
                    cs3_HW=model3_moderate_HW(float(HW_3))
                    cs4_HW=model3_high_HW(float(HW_3))
                    #define condition state for T.trichiura
                    cs1_Tt=model3_no_Tt(float(Tt_3))
                    cs2_Tt=model3_light_Tt(float(Tt_3))
                    cs3_Tt=model3_moderate_Tt(float(Tt_3))
                    cs4_Tt=model3_high_Tt(float(Tt_3))
                    #define condition state for A.Alumbricoin
                    cs1_Al=model3_no_Al(float(Al_3))
                    cs2_Al=model3_light_Al(float(Al_3))
                    cs3_Al=model3_moderate_Al(float(Al_3))
                    cs4_Al=model3_high_Al(float(Al_3))
                    #for anySTH
                    anySTH=model3_anySTH(float(HW_3),float(Tt_3),float(Al_3))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("H_n_3_"+str(t), cs1_HW)
                    feature.SetField("H_l_3_"+str(t), cs2_HW)
                    feature.SetField("H_m_3_"+str(t), cs3_HW)
                    feature.SetField("H_h_3_"+str(t), cs4_HW)
                    feature.SetField("HW_3_"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    cs_HW=np.array([cs1_HW,cs2_HW,cs3_HW,cs4_HW])
                    #for T.trichiura
                    feature.SetField("T_n_3_"+str(t), cs1_Tt)
                    feature.SetField("T_l_3_"+str(t), cs2_Tt)
                    feature.SetField("T_m_3_"+str(t), cs3_Tt)
                    feature.SetField("T_h_3_"+str(t), cs4_Tt)
                    feature.SetField("Tt_3_"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    cs_Tt=np.array([cs1_Tt,cs2_Tt,cs3_Tt,cs4_Tt])
                    feature.SetField("A_n_3_"+str(t), cs1_Al)
                    feature.SetField("A_l_3_"+str(t), cs2_Al)
                    feature.SetField("A_m_3_"+str(t), cs3_Al)
                    feature.SetField("A_h_3_"+str(t), cs4_Al)
                    feature.SetField("Al_3_"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STH_3_"+str(t), anySTH)
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
                    feature.SetField("H_n_3_"+str(t), cs1_HW)
                    feature.SetField("H_l_3_"+str(t), cs2_HW)
                    feature.SetField("H_m_3_"+str(t), cs3_HW)
                    feature.SetField("H_h_3_"+str(t), cs4_HW)
                    feature.SetField("HW_3_"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    #for T.trichiura
                    feature.SetField("T_n_3_"+str(t), cs1_Tt)
                    feature.SetField("T_l_3_"+str(t), cs2_Tt)
                    feature.SetField("T_m_3_"+str(t), cs3_Tt)
                    feature.SetField("T_h_3_"+str(t), cs4_Tt)
                    feature.SetField("Tt_3_"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    feature.SetField("A_n_3_"+str(t), cs1_Al)
                    feature.SetField("A_l_3_"+str(t), cs2_Al)
                    feature.SetField("A_m_3_"+str(t), cs3_Al)
                    feature.SetField("A_h_3_"+str(t), cs4_Al)
                    feature.SetField("Al_3_"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STH_3_"+str(t), anySTH)


        elif feature.GetField("CATEGORY") == "E":
            for t in range(time):
                if t==0:
                    HW_3=feature.GetField("HW_3")
                    Tt_3=feature.GetField("Tt_3")
                    Al_3=feature.GetField("Al_3")
                    #define condition state for Hookworm
                    cs1_HW=model3_no_HW(float(HW_3))
                    cs2_HW=model3_light_HW(float(HW_3))
                    cs3_HW=model3_moderate_HW(float(HW_3))
                    cs4_HW=model3_high_HW(float(HW_3))
                    #define condition state for T.trichiura
                    cs1_Tt=model3_no_Tt(float(Tt_3))
                    cs2_Tt=model3_light_Tt(float(Tt_3))
                    cs3_Tt=model3_moderate_Tt(float(Tt_3))
                    cs4_Tt=model3_high_Tt(float(Tt_3))
                    #define condition state for A.Alumbricoin
                    cs1_Al=model3_no_Al(float(Al_3))
                    cs2_Al=model3_light_Al(float(Al_3))
                    cs3_Al=model3_moderate_Al(float(Al_3))
                    cs4_Al=model3_high_Al(float(Al_3))
                    #for anySTH
                    anySTH=model3_anySTH(float(HW_3),float(Tt_3),float(Al_3))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("H_n_3_"+str(t), cs1_HW)
                    feature.SetField("H_l_3_"+str(t), cs2_HW)
                    feature.SetField("H_m_3_"+str(t), cs3_HW)
                    feature.SetField("H_h_3_"+str(t), cs4_HW)
                    feature.SetField("HW_3_"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    cs_HW=np.array([cs1_HW,cs2_HW,cs3_HW,cs4_HW])
                    #for T.trichiura
                    feature.SetField("T_n_3_"+str(t), cs1_Tt)
                    feature.SetField("T_l_3_"+str(t), cs2_Tt)
                    feature.SetField("T_m_3_"+str(t), cs3_Tt)
                    feature.SetField("T_h_3_"+str(t), cs4_Tt)
                    feature.SetField("Tt_3_"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    cs_Tt=np.array([cs1_Tt,cs2_Tt,cs3_Tt,cs4_Tt])
                    feature.SetField("A_n_3_"+str(t), cs1_Al)
                    feature.SetField("A_l_3_"+str(t), cs2_Al)
                    feature.SetField("A_m_3_"+str(t), cs3_Al)
                    feature.SetField("A_h_3_"+str(t), cs4_Al)
                    feature.SetField("Al_3_"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STH_3_"+str(t), anySTH)
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
                    feature.SetField("H_n_3_"+str(t), cs1_HW)
                    feature.SetField("H_l_3_"+str(t), cs2_HW)
                    feature.SetField("H_m_3_"+str(t), cs3_HW)
                    feature.SetField("H_h_3_"+str(t), cs4_HW)
                    feature.SetField("HW_3_"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    #for T.trichiura
                    feature.SetField("T_n_3_"+str(t), cs1_Tt)
                    feature.SetField("T_l_3_"+str(t), cs2_Tt)
                    feature.SetField("T_m_3_"+str(t), cs3_Tt)
                    feature.SetField("T_h_3_"+str(t), cs4_Tt)
                    feature.SetField("Tt_3_"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    feature.SetField("A_n_3_"+str(t), cs1_Al)
                    feature.SetField("A_l_3_"+str(t), cs2_Al)
                    feature.SetField("A_m_3_"+str(t), cs3_Al)
                    feature.SetField("A_h_3_"+str(t), cs4_Al)
                    feature.SetField("Al_3_"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STH_3_"+str(t), anySTH)



        elif feature.GetField("CATEGORY") == "F":
            for t in range(time):
                if t==0:
                    HW_3=feature.GetField("HW_3")
                    Tt_3=feature.GetField("Tt_3")
                    Al_3=feature.GetField("Al_3")
                    #define condition state for Hookworm
                    cs1_HW=model3_no_HW(float(HW_3))
                    cs2_HW=model3_light_HW(float(HW_3))
                    cs3_HW=model3_moderate_HW(float(HW_3))
                    cs4_HW=model3_high_HW(float(HW_3))
                    #define condition state for T.trichiura
                    cs1_Tt=model3_no_Tt(float(Tt_3))
                    cs2_Tt=model3_light_Tt(float(Tt_3))
                    cs3_Tt=model3_moderate_Tt(float(Tt_3))
                    cs4_Tt=model3_high_Tt(float(Tt_3))
                    #define condition state for A.Alumbricoin
                    cs1_Al=model3_no_Al(float(Al_3))
                    cs2_Al=model3_light_Al(float(Al_3))
                    cs3_Al=model3_moderate_Al(float(Al_3))
                    cs4_Al=model3_high_Al(float(Al_3))
                    #for anySTH
                    anySTH=model3_anySTH(float(HW_3),float(Tt_3),float(Al_3))
                    #assign value of cs to each field in the shapefile
                    #for hookworm
                    feature.SetField("H_n_3_"+str(t), cs1_HW)
                    feature.SetField("H_l_3_"+str(t), cs2_HW)
                    feature.SetField("H_m_3_"+str(t), cs3_HW)
                    feature.SetField("H_h_3_"+str(t), cs4_HW)
                    feature.SetField("HW_3_"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    cs_HW=np.array([cs1_HW,cs2_HW,cs3_HW,cs4_HW])
                    #for T.trichiura
                    feature.SetField("T_n_3_"+str(t), cs1_Tt)
                    feature.SetField("T_l_3_"+str(t), cs2_Tt)
                    feature.SetField("T_m_3_"+str(t), cs3_Tt)
                    feature.SetField("T_h_3_"+str(t), cs4_Tt)
                    feature.SetField("Tt_3_"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    cs_Tt=np.array([cs1_Tt,cs2_Tt,cs3_Tt,cs4_Tt])
                    feature.SetField("A_n_3_"+str(t), cs1_Al)
                    feature.SetField("A_l_3_"+str(t), cs2_Al)
                    feature.SetField("A_m_3_"+str(t), cs3_Al)
                    feature.SetField("A_h_3_"+str(t), cs4_Al)
                    feature.SetField("Al_3_"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STH_3_"+str(t), anySTH)
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
                    feature.SetField("H_n_3_"+str(t), cs1_HW)
                    feature.SetField("H_l_3_"+str(t), cs2_HW)
                    feature.SetField("H_m_3_"+str(t), cs3_HW)
                    feature.SetField("H_h_3_"+str(t), cs4_HW)
                    feature.SetField("HW_3_"+str(t), cs2_HW+cs3_HW+cs4_HW)
                    #for T.trichiura
                    feature.SetField("T_n_3_"+str(t), cs1_Tt)
                    feature.SetField("T_l_3_"+str(t), cs2_Tt)
                    feature.SetField("T_m_3_"+str(t), cs3_Tt)
                    feature.SetField("T_h_3_"+str(t), cs4_Tt)
                    feature.SetField("Tt_3_"+str(t), cs2_Tt+cs3_Tt+cs4_Tt)
                    feature.SetField("A_n_3_"+str(t), cs1_Al)
                    feature.SetField("A_l_3_"+str(t), cs2_Al)
                    feature.SetField("A_m_3_"+str(t), cs3_Al)
                    feature.SetField("A_h_3_"+str(t), cs4_Al)
                    feature.SetField("Al_3_"+str(t), cs2_Al+cs3_Al+cs4_Al)
                    #for anySTH
                    feature.SetField("STH_3_"+str(t), anySTH)

        layer.SetFeature(feature)
        feature.Destroy()
    # All done.
    shapefile.Destroy()
    #import mtp4
