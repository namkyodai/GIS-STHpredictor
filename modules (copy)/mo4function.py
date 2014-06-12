#define the high intensity prevalence
def model4high(x):
    y = 0.001*x**2 - 0.0278*x #high intensity
    return y;

#define the high moderate prevalence
def model4moderate(x):
    y = 0.0094*x**2 - 0.2688*x
    return y;

#define the light intensity prevalence
def model4light(x):
    y=x-model4moderate(x)-model4high(x)
    return y;

def model4no(x):
    y=100-model4moderate(x)-model4high(x)-model4light(x)
    return y;



