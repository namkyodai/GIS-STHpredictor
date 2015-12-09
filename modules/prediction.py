import numpy as np

def prediction(time,cs,mtp1,mtp2,mtp3,breakpoint1,breakpoint2):
  prevalence = np.zeros(time*len(cs))
  prevalence = np.resize(prevalence,(time,len(cs)))
  prevalence[0] = cs
  
  for t in range(1,time):
    if t<breakpoint1:
        P = prevalence[t-1]
        prevalence[t] = P.dot(mtp1)
    elif t<breakpoint2:
        P = prevalence[t-1]
        prevalence[t] = P.dot(mtp2)
    else:
        P = prevalence[t-1]
        prevalence[t] = P.dot(mtp3)
  return prevalence




