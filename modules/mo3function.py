#define the high intensity prevalence

#for hookworm
def model3_high_HW(x):
    y = 0.001*x**2 - 0.0196*x #high intensity
    return y;

#define the high moderate prevalence
def model3_moderate_HW(x):
    y = 0.0016*x**2 - 0.0121*x
    return y;

#define the light intensity prevalence
def model3_light_HW(x):
    y=x-model3_high_HW(x)-model3_moderate_HW(x)
    return y;

def model3_no_HW(x):
    y=100-model3_high_HW(x)-model3_moderate_HW(x)-model3_light_HW(x)
    return y;

def model3_total_HW(x):
    y=model3_high_HW(x)+model3_moderate_HW(x)+model3_light_HW(x)
    return y;	
	

#for T.trichiura
def model3_high_Tt(x):
    y = 0.0001*x**2 + 0.0001*x #high intensity
    return y;

#define the high moderate prevalence
def model3_moderate_Tt(x):
    y = 0.0042*x**2 + 0.015*x
    return y;

#define the light intensity prevalence
def model3_light_Tt(x):
    y=x-model3_high_Tt(x)-model3_moderate_Tt(x)
    return y;

def model3_no_Tt(x):
    y=100-model3_high_Tt(x)-model3_moderate_Tt(x)-model3_light_Tt(x)
    return y;
	
def model3_total_Tt(x):
    y=model3_high_Tt(x)+model3_moderate_Tt(x)+model3_light_Tt(x)
    return y;	
	
#for A.lumbricoin
def model3_high_Al(x):
    y = 0.0007*x**2 + 0.0037*x #high intensity
    return y;

#define the high moderate prevalence
def model3_moderate_Al(x):
    y = 0.0025*x**2 + 0.2044*x
    return y;

#define the light intensity prevalence
def model3_light_Al(x):
    y=x-model3_high_Al(x)-model3_moderate_Al(x)
    return y;

def model3_no_Al(x):
    y=100-model3_high_Al(x)-model3_moderate_Al(x)-model3_light_Al(x)
    return y;

def model3_total_Al(x):
    y=model3_high_Tt(x)+model3_moderate_Tt(x)+model3_light_Tt(x)
    return y;
	
def model3_anySTH(x1,x2,x3):
    y=(((x1/100+x2/100+x3/100)-(x1/100*x2/100+x2/100*x3/100+x1/100*x3/100)+x1*x2*x3/100/100/100)/1.06)*100
    return y;
	

