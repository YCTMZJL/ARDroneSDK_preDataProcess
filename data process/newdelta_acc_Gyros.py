# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 20:30:53 2016

@author: ml
"""

import numpy as np


#filepath = 'D:/Jerry/2-Lab/data process/data process/result/'
filepath = '/media/ml/Ubuntu 14.0/result/res1/'
savepath = filepath# 'D:/Jerry/2-Lab/data process/data process/newResult/' #Delta_Mean_stable_Jonny_20161118_203114
savename = 'Delta_Mean_stable_Jonny_20161118_203114_accY.csv'#Gyros
f1 = open(filepath + 'Mean_stable_Jonny_20161118_203114_accY.csv','rb')
f2 = open(filepath + 'stable_Jonny_20161118_203114_timeInterval.csv','rb')
lines=f1.readlines();
linesfortime = f2.readlines();
f1.close()
f2.close()
count = 0

deltatime = []
data = []#[giventype] #[] 

groupnum = 10   #每多少个区一次平均
#sumdata = [0]
#sumtime = [0]
#meandata=[0]
deltadata = [0]
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
        continue #头不作处理 
    elif(i == 1) :
        deltadata = np.vstack(( deltadata,0))
    elif ( i  >  1 ):
    #elif ( i  <  3 +  groupnum ):
        deltadata = np.vstack(( deltadata,(data[i-1]-data[i])/deltatime[i] ))
       
        
print np.shape(deltadata)     
     
np.savetxt(savepath+savename,deltadata,fmt='%f',delimiter=',')