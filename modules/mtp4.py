#define the markov transition probability
import numpy as np
mtp_cp1 = [[0 for i in range(4)] for j in range(4)] #the transition probabilities for model 4

mtp_cp1[0][0]=0.91
mtp_cp1[0][1]=0.07
mtp_cp1[0][2]=0.01
mtp_cp1[0][3]=1-mtp_cp1[0][0]-mtp_cp1[0][1]-mtp_cp1[0][2]

mtp_cp1[1][0]=0.85
mtp_cp1[1][1]=0.13
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


mtp_cp2 = [[0 for i in range(4)] for j in range(4)] #the transition probabilities for model 4

mtp_cp2[0][0]=0.92
mtp_cp2[0][1]=0.06
mtp_cp2[0][2]=0.01
mtp_cp2[0][3]=1-mtp_cp2[0][0]-mtp_cp2[0][1]-mtp_cp2[0][2]

mtp_cp2[1][0]=0.88
mtp_cp2[1][1]=0.11
mtp_cp2[1][2]=0.00
mtp_cp2[1][3]=1-mtp_cp2[1][0]-mtp_cp2[1][1]-mtp_cp2[1][2]

mtp_cp2[2][0]=0.81
mtp_cp2[2][1]=0.15
mtp_cp2[2][2]=0.00
mtp_cp2[2][3]=1-mtp_cp2[2][0]-mtp_cp2[2][1]-mtp_cp2[2][2]

mtp_cp2[3][0]=0.73
mtp_cp2[3][1]=0.27
mtp_cp2[3][2]=0.00
mtp_cp2[3][3]=1-mtp_cp2[3][0]-mtp_cp2[3][1]-mtp_cp2[3][2]

mtp_cp2=np.array([[mtp_cp2[0][0],mtp_cp2[0][1],mtp_cp2[0][2],mtp_cp2[0][3]],
              [mtp_cp2[1][0],mtp_cp2[1][1],mtp_cp2[1][2],mtp_cp2[1][3]],
              [mtp_cp2[2][0],mtp_cp2[2][1],mtp_cp2[2][2],mtp_cp2[2][3]],
              [mtp_cp2[3][0],mtp_cp2[3][1],mtp_cp2[3][2],mtp_cp2[3][3]]])

			  
			  
mtp_cp3 = [[0 for i in range(4)] for j in range(4)] #the transition probabilities for model 4

mtp_cp3[0][0]=0.92
mtp_cp3[0][1]=0.06
mtp_cp3[0][2]=0.01
mtp_cp3[0][3]=1-mtp_cp3[0][0]-mtp_cp3[0][1]-mtp_cp3[0][2]

mtp_cp3[1][0]=0.88
mtp_cp3[1][1]=0.11
mtp_cp3[1][2]=0.00
mtp_cp3[1][3]=1-mtp_cp3[1][0]-mtp_cp3[1][1]-mtp_cp3[1][2]

mtp_cp3[2][0]=0.81
mtp_cp3[2][1]=0.15
mtp_cp3[2][2]=0.00
mtp_cp3[2][3]=1-mtp_cp3[2][0]-mtp_cp3[2][1]-mtp_cp3[2][2]

mtp_cp3[3][0]=0.73
mtp_cp3[3][1]=0.27
mtp_cp3[3][2]=0.00
mtp_cp3[3][3]=1-mtp_cp3[3][0]-mtp_cp3[3][1]-mtp_cp3[3][2]

mtp_cp3=np.array([[mtp_cp3[0][0],mtp_cp3[0][1],mtp_cp3[0][2],mtp_cp3[0][3]],
              [mtp_cp3[1][0],mtp_cp3[1][1],mtp_cp3[1][2],mtp_cp3[1][3]],
              [mtp_cp3[2][0],mtp_cp3[2][1],mtp_cp3[2][2],mtp_cp3[2][3]],
              [mtp_cp3[3][0],mtp_cp3[3][1],mtp_cp3[3][2],mtp_cp3[3][3]]])

			  
mtp_cp4 = [[0 for i in range(4)] for j in range(4)] #the transition probabilities for model 4

mtp_cp4[0][0]=0.92
mtp_cp4[0][1]=0.06
mtp_cp4[0][2]=0.01
mtp_cp4[0][3]=1-mtp_cp4[0][0]-mtp_cp4[0][1]-mtp_cp4[0][2]

mtp_cp4[1][0]=0.88
mtp_cp4[1][1]=0.11
mtp_cp4[1][2]=0.00
mtp_cp4[1][3]=1-mtp_cp4[1][0]-mtp_cp4[1][1]-mtp_cp4[1][2]

mtp_cp4[2][0]=0.81
mtp_cp4[2][1]=0.15
mtp_cp4[2][2]=0.00
mtp_cp4[2][3]=1-mtp_cp4[2][0]-mtp_cp4[2][1]-mtp_cp4[2][2]

mtp_cp4[3][0]=0.73
mtp_cp4[3][1]=0.27
mtp_cp4[3][2]=0.00
mtp_cp4[3][3]=1-mtp_cp4[3][0]-mtp_cp4[3][1]-mtp_cp4[3][2]

mtp_cp4=np.array([[mtp_cp4[0][0],mtp_cp4[0][1],mtp_cp4[0][2],mtp_cp4[0][3]],
              [mtp_cp4[1][0],mtp_cp4[1][1],mtp_cp4[1][2],mtp_cp4[1][3]],
              [mtp_cp4[2][0],mtp_cp4[2][1],mtp_cp4[2][2],mtp_cp4[2][3]],
              [mtp_cp4[3][0],mtp_cp4[3][1],mtp_cp4[3][2],mtp_cp4[3][3]]])
			  
mtp_cp5 = [[0 for i in range(4)] for j in range(4)] #the transition probabilities for model 4

mtp_cp5[0][0]=0.92
mtp_cp5[0][1]=0.06
mtp_cp5[0][2]=0.01
mtp_cp5[0][3]=1-mtp_cp5[0][0]-mtp_cp5[0][1]-mtp_cp5[0][2]

mtp_cp5[1][0]=0.88
mtp_cp5[1][1]=0.11
mtp_cp5[1][2]=0.00
mtp_cp5[1][3]=1-mtp_cp5[1][0]-mtp_cp5[1][1]-mtp_cp5[1][2]

mtp_cp5[2][0]=0.81
mtp_cp5[2][1]=0.15
mtp_cp5[2][2]=0.00
mtp_cp5[2][3]=1-mtp_cp5[2][0]-mtp_cp5[2][1]-mtp_cp5[2][2]

mtp_cp5[3][0]=0.73
mtp_cp5[3][1]=0.27
mtp_cp5[3][2]=0.00
mtp_cp5[3][3]=1-mtp_cp5[3][0]-mtp_cp5[3][1]-mtp_cp5[3][2]

mtp_cp5=np.array([[mtp_cp5[0][0],mtp_cp5[0][1],mtp_cp5[0][2],mtp_cp5[0][3]],
              [mtp_cp5[1][0],mtp_cp5[1][1],mtp_cp5[1][2],mtp_cp5[1][3]],
              [mtp_cp5[2][0],mtp_cp5[2][1],mtp_cp5[2][2],mtp_cp5[2][3]],
              [mtp_cp5[3][0],mtp_cp5[3][1],mtp_cp5[3][2],mtp_cp5[3][3]]])
			  
			  
mtp_cp6 = [[0 for i in range(4)] for j in range(4)] #the transition probabilities for model 4

mtp_cp6[0][0]=0.92
mtp_cp6[0][1]=0.06
mtp_cp6[0][2]=0.01
mtp_cp6[0][3]=1-mtp_cp6[0][0]-mtp_cp6[0][1]-mtp_cp6[0][2]

mtp_cp6[1][0]=0.88
mtp_cp6[1][1]=0.11
mtp_cp6[1][2]=0.00
mtp_cp6[1][3]=1-mtp_cp6[1][0]-mtp_cp6[1][1]-mtp_cp6[1][2]

mtp_cp6[2][0]=0.81
mtp_cp6[2][1]=0.15
mtp_cp6[2][2]=0.00
mtp_cp6[2][3]=1-mtp_cp6[2][0]-mtp_cp6[2][1]-mtp_cp6[2][2]

mtp_cp6[3][0]=0.73
mtp_cp6[3][1]=0.27
mtp_cp6[3][2]=0.00
mtp_cp6[3][3]=1-mtp_cp6[3][0]-mtp_cp6[3][1]-mtp_cp6[3][2]

mtp_cp6=np.array([[mtp_cp6[0][0],mtp_cp6[0][1],mtp_cp6[0][2],mtp_cp6[0][3]],
              [mtp_cp6[1][0],mtp_cp6[1][1],mtp_cp6[1][2],mtp_cp6[1][3]],
              [mtp_cp6[2][0],mtp_cp6[2][1],mtp_cp6[2][2],mtp_cp6[2][3]],
              [mtp_cp6[3][0],mtp_cp6[3][1],mtp_cp6[3][2],mtp_cp6[3][3]]])
			  
mtp_cp7 = [[0 for i in range(4)] for j in range(4)] #the transition probabilities for model 4

mtp_cp7[0][0]=0.92
mtp_cp7[0][1]=0.06
mtp_cp7[0][2]=0.01
mtp_cp7[0][3]=1-mtp_cp7[0][0]-mtp_cp7[0][1]-mtp_cp7[0][2]

mtp_cp7[1][0]=0.88
mtp_cp7[1][1]=0.11
mtp_cp7[1][2]=0.00
mtp_cp7[1][3]=1-mtp_cp7[1][0]-mtp_cp7[1][1]-mtp_cp7[1][2]

mtp_cp7[2][0]=0.81
mtp_cp7[2][1]=0.15
mtp_cp7[2][2]=0.00
mtp_cp7[2][3]=1-mtp_cp7[2][0]-mtp_cp7[2][1]-mtp_cp7[2][2]

mtp_cp7[3][0]=0.73
mtp_cp7[3][1]=0.27
mtp_cp7[3][2]=0.00
mtp_cp7[3][3]=1-mtp_cp7[3][0]-mtp_cp7[3][1]-mtp_cp7[3][2]

mtp_cp7=np.array([[mtp_cp7[0][0],mtp_cp7[0][1],mtp_cp7[0][2],mtp_cp7[0][3]],
              [mtp_cp7[1][0],mtp_cp7[1][1],mtp_cp7[1][2],mtp_cp7[1][3]],
              [mtp_cp7[2][0],mtp_cp7[2][1],mtp_cp7[2][2],mtp_cp7[2][3]],
              [mtp_cp7[3][0],mtp_cp7[3][1],mtp_cp7[3][2],mtp_cp7[3][3]]])
			  
mtp_cp8 = [[0 for i in range(4)] for j in range(4)] #the transition probabilities for model 4

mtp_cp8[0][0]=0.92
mtp_cp8[0][1]=0.06
mtp_cp8[0][2]=0.01
mtp_cp8[0][3]=1-mtp_cp8[0][0]-mtp_cp8[0][1]-mtp_cp8[0][2]

mtp_cp8[1][0]=0.88
mtp_cp8[1][1]=0.11
mtp_cp8[1][2]=0.00
mtp_cp8[1][3]=1-mtp_cp8[1][0]-mtp_cp8[1][1]-mtp_cp8[1][2]

mtp_cp8[2][0]=0.81
mtp_cp8[2][1]=0.15
mtp_cp8[2][2]=0.00
mtp_cp8[2][3]=1-mtp_cp8[2][0]-mtp_cp8[2][1]-mtp_cp8[2][2]

mtp_cp8[3][0]=0.73
mtp_cp8[3][1]=0.27
mtp_cp8[3][2]=0.00
mtp_cp8[3][3]=1-mtp_cp8[3][0]-mtp_cp8[3][1]-mtp_cp8[3][2]

mtp_cp8=np.array([[mtp_cp8[0][0],mtp_cp8[0][1],mtp_cp8[0][2],mtp_cp8[0][3]],
              [mtp_cp8[1][0],mtp_cp8[1][1],mtp_cp8[1][2],mtp_cp8[1][3]],
              [mtp_cp8[2][0],mtp_cp8[2][1],mtp_cp8[2][2],mtp_cp8[2][3]],
              [mtp_cp8[3][0],mtp_cp8[3][1],mtp_cp8[3][2],mtp_cp8[3][3]]])
			  
mtp_cp9 = [[0 for i in range(4)] for j in range(4)] #the transition probabilities for model 4

mtp_cp9[0][0]=0.92
mtp_cp9[0][1]=0.06
mtp_cp9[0][2]=0.01
mtp_cp9[0][3]=1-mtp_cp9[0][0]-mtp_cp9[0][1]-mtp_cp9[0][2]

mtp_cp9[1][0]=0.88
mtp_cp9[1][1]=0.11
mtp_cp9[1][2]=0.00
mtp_cp9[1][3]=1-mtp_cp9[1][0]-mtp_cp9[1][1]-mtp_cp9[1][2]

mtp_cp9[2][0]=0.81
mtp_cp9[2][1]=0.15
mtp_cp9[2][2]=0.00
mtp_cp9[2][3]=1-mtp_cp9[2][0]-mtp_cp9[2][1]-mtp_cp9[2][2]

mtp_cp9[3][0]=0.73
mtp_cp9[3][1]=0.27
mtp_cp9[3][2]=0.00
mtp_cp9[3][3]=1-mtp_cp9[3][0]-mtp_cp9[3][1]-mtp_cp9[3][2]

mtp_cp9=np.array([[mtp_cp9[0][0],mtp_cp9[0][1],mtp_cp9[0][2],mtp_cp9[0][3]],
              [mtp_cp9[1][0],mtp_cp9[1][1],mtp_cp9[1][2],mtp_cp9[1][3]],
              [mtp_cp9[2][0],mtp_cp9[2][1],mtp_cp9[2][2],mtp_cp9[2][3]],
              [mtp_cp9[3][0],mtp_cp9[3][1],mtp_cp9[3][2],mtp_cp9[3][3]]])
			  
mtp_cp10 = [[0 for i in range(4)] for j in range(4)] #the transition probabilities for model 4

mtp_cp10[0][0]=0.92
mtp_cp10[0][1]=0.06
mtp_cp10[0][2]=0.01
mtp_cp10[0][3]=1-mtp_cp10[0][0]-mtp_cp10[0][1]-mtp_cp10[0][2]

mtp_cp10[1][0]=0.88
mtp_cp10[1][1]=0.11
mtp_cp10[1][2]=0.00
mtp_cp10[1][3]=1-mtp_cp10[1][0]-mtp_cp10[1][1]-mtp_cp10[1][2]

mtp_cp10[2][0]=0.81
mtp_cp10[2][1]=0.15
mtp_cp10[2][2]=0.00
mtp_cp10[2][3]=1-mtp_cp10[2][0]-mtp_cp10[2][1]-mtp_cp10[2][2]

mtp_cp10[3][0]=0.73
mtp_cp10[3][1]=0.27
mtp_cp10[3][2]=0.00
mtp_cp10[3][3]=1-mtp_cp10[3][0]-mtp_cp10[3][1]-mtp_cp10[3][2]

mtp_cp10=np.array([[mtp_cp10[0][0],mtp_cp10[0][1],mtp_cp10[0][2],mtp_cp10[0][3]],
              [mtp_cp10[1][0],mtp_cp10[1][1],mtp_cp10[1][2],mtp_cp10[1][3]],
              [mtp_cp10[2][0],mtp_cp10[2][1],mtp_cp10[2][2],mtp_cp10[2][3]],
              [mtp_cp10[3][0],mtp_cp10[3][1],mtp_cp10[3][2],mtp_cp10[3][3]]])
			  
mtp_cpdn = [[0 for i in range(4)] for j in range(4)] #the transition probabilities for model 4

mtp_cpdn[0][0]=1
mtp_cpdn[0][1]=0
mtp_cpdn[0][2]=0
mtp_cpdn[0][3]=0

mtp_cpdn[1][0]=0
mtp_cpdn[1][1]=1
mtp_cpdn[1][2]=0
mtp_cpdn[1][3]=0

mtp_cpdn[2][0]=0
mtp_cpdn[2][1]=0
mtp_cpdn[2][2]=1
mtp_cpdn[2][3]=0

mtp_cpdn[3][0]=0
mtp_cpdn[3][1]=0
mtp_cpdn[3][2]=0
mtp_cpdn[3][3]=1

mtp_cpdn=np.array([[mtp_cpdn[0][0],mtp_cpdn[0][1],mtp_cpdn[0][2],mtp_cpdn[0][3]],
              [mtp_cpdn[1][0],mtp_cpdn[1][1],mtp_cpdn[1][2],mtp_cpdn[1][3]],
              [mtp_cpdn[2][0],mtp_cpdn[2][1],mtp_cpdn[2][2],mtp_cpdn[2][3]],
              [mtp_cpdn[3][0],mtp_cpdn[3][1],mtp_cpdn[3][2],mtp_cpdn[3][3]]])
