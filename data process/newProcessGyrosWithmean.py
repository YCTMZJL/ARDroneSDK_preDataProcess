# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 20:03:24 2016

@author: ml
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 13:23:21 2016

@author: Jerry
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 14:13:40 2016

@author: ml
"""

import numpy as np

import matplotlib.pyplot as plt

#filepath = 'D:/Jerry/2-Lab/data process/data process/result/'
filepath = '/media/ml/Ubuntu 14.0/result/res2/'
savepath = filepath# 'D:/Jerry/2-Lab/data process/data process/newResult/'
savename = 'Mean_fly_Jonny_mesures_20161118_204012_GyrosZ.csv' #Gyros
f1 = open(filepath + 'fly_Jonny_mesures_20161118_204012_GyrosZ.csv','rb')
f2 = open(filepath + 'fly_Jonny_mesures_20161118_204012_timeInterval.csv','rb')
lines=f1.readlines();
linesfortime = f2.readlines();
f1.close()
f2.close()
count = 0

deltatime = []
data = []#[giventype] #[] 

groupnum = 10   #每多少个区一次平均
sumdata = [0]
sumtime = [0]
meandata=[0]
lenth = min(len(lines),len(linesfortime))
print lenth

for i in range(lenth):
    #temp = []
    linedata = lines[i].strip('\n')
    linedata = linedata.split(',')
    linetime = linesfortime[i].strip('\n')
    linetime = linetime.split(',')
    deltatime.append(float(linetime[0]))
    data.append(float(linedata[0]))
    if ( i == 0 ):
         # sumdata = np.add(sumdata,np.array(data)[0:,0:3])
        #meandata = sumdata
        sumdata[0] = np.array(data)[i]*(deltatime[i])
        sumtime[0] =np.array(deltatime)[i]
        if sumtime[i] == 0 :
            meandata[0] = np.array(data)[i]
        else:
            meandata[0] = (sumdata[i] / sumtime[i])
        #continue #头不作处理 
    elif ( i  ==  1 ):
    #elif ( i  <  3 +  groupnum ):
        sumdata = np.vstack(( sumdata, np.add(sumdata, np.array(data)[i]*(deltatime[i])) ))
        sumtime = np.vstack((sumtime,np.add(sumtime,np.array(deltatime)[i])))
        if sumtime[i] == 0 :
            meandata = np.vstack((meandata,np.array(data)[i]))
        else:
            meandata = np.vstack((meandata,(sumdata[i] / sumtime[i])))
    elif ( i  <  1 +  groupnum ):
        sumdata = np.vstack((sumdata,np.add(sumdata[i-1],np.array(data)[i]*(deltatime[i]))))
        sumtime = np.vstack((sumtime,np.add(sumtime[i-1],np.array(deltatime)[i])))
        if sumtime[i] == 0 :
             meandata = np.vstack((meandata,np.array(data)[i]))
        else:
             meandata = np.vstack((meandata,(sumdata[i] / sumtime[i])))
    #elif ( i  <  4+  groupnum ):
    else:
        sumdata = np.vstack((sumdata,np.add(sumdata[i-1],np.array(data)[i]*(deltatime[i])) - np.array(data)[i-groupnum ]*(deltatime[i-groupnum])  ))
        sumtime = np.vstack((sumtime,np.add(sumtime[i-1],np.array(deltatime)[i]) - np.array(deltatime)[i-groupnum] ))
        meandata = np.vstack((meandata,(sumdata[i] / sumtime[i])))
        
print np.shape(data)     
     
np.savetxt(savepath+savename,meandata,fmt='%f',delimiter=',')