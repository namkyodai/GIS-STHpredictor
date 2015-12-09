#define the markov transition probability
import numpy as np
mtp_cp1 = [[0 for i in range(4)] for j in range(4)] #the transition probabilities for model 4

mtp_cp1[0][0]=0.92
mtp_cp1[0][1]=0.06
mtp_cp1[0][2]=0.01
mtp_cp1[0][3]=1-mtp_cp1[0][0]-mtp_cp1[0][1]-mtp_cp1[0][2]

mtp_cp1[1][0]=0.88
mtp_cp1[1][1]=0.11
mtp_cp1[1][2]=0.00
mtp_cp1[1][3]=1-mtp_cp1[1][0]-mtp_cp1[1][1]-mtp_cp1[1][2]

mtp_cp1[2][0]=0.81
mtp_cp1[2][1]=0.15
mtp_cp1[2][2]=0.00
mtp_cp1[2][3]=1-mtp_cp1[2][0]-mtp_cp1[2][1]-mtp_cp1[2][2]

mtp_cp1[3][0]=0.73
mtp_cp1[3][1]=0.27
mtp_cp1[3][2]=0.00
mtp_cp1[3][3]=1-mtp_cp1[3][0]-mtp_cp1[3][1]-mtp_cp1[3][2]

mtp_cp1=np.array([[mtp_cp1[0][0],mtp_cp1[0][1],mtp_cp1[0][2],mtp_cp1[0][3]],
              [mtp_cp1[1][0],mtp_cp1[1][1],mtp_cp1[1][2],mtp_cp1[1][3]],
              [mtp_cp1[2][0],mtp_cp1[2][1],mtp_cp1[2][2],mtp_cp1[2][3]],
              [mtp_cp1[3][0],mtp_cp1[3][1],mtp_cp1[3][2],mtp_cp1[3][3]]])
