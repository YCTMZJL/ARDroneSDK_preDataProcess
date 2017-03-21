# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:30:08 2016

@author: ml
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 10:38:58 2016

@author: Jerry
"""
import numpy as np
filepath = '/media/ml/Ubuntu 14.0/result/res1/'#'result/' #'F:/实验结果/新实验结果8_60s/速度均值位移均值为零/'
filepath=unicode(filepath,'utf8')
f1 = open(filepath+'stable_Jonny_20161118_203114_timeInterval.csv','rb')
savePath = filepath
saveName = 'TotalTime_stable_Jonny_20161118_203114_timeInterval.csv'
savePath = savePath + saveName
lines=f1.readlines();

totaltime = []

for i in range(0,len(lines)-1):
#for i in range(2,5002):#len(lines)):
    linedata = lines[i].strip('\r')
    linedata = lines[i].split(',')
    linedata[0] = float(linedata[0].strip(' '))
    #print linedata
    if i == 0 :
        totaltime = np.array(linedata[0]);
        #totaltime.append(linedata[0])
    elif i==1:
        tmp = np.add(totaltime,np.array(linedata[0]))
        totaltime = np.vstack((totaltime,tmp))
    else:
        tmp = np.add(totaltime[i-1],np.array(linedata[0]))
        totaltime=np.vstack((totaltime,tmp))
        #totaltime.append(totaltime[i-1]+linedata[0])

print np.shape(np.array(totaltime))
np.savetxt(savePath,totaltime,fmt='%f',delimiter=',')
'''
np.savetxt(savePath+'.csv',data,fmt='%f',delimiter=',')
np.savetxt(savePath+'_accX.csv',np.array(data)[:,0],fmt='%f',delimiter='')
np.savetxt(savePath+'_accY.csv',np.array(data)[:,1],fmt='%f',delimiter='')
np.savetxt(savePath+'_accZ.csv',np.array(data)[:,2],fmt='%f',delimiter='')


np.savetxt(savePath+'_timeInterval.csv',np.array(deltatime),fmt='%f',delimiter='')

np.savetxt(savePath+'_accXwithTime.csv',np.vstack((np.array(data)[:,0],np.array(deltatime))).T,fmt='%f',delimiter=',')
np.savetxt(savePath+'_accYwithTime.csv',np.vstack((np.array(data)[:,1],np.array(deltatime))).T,fmt='%f',delimiter=',')
np.savetxt(savePath+'_accZwithTime.csv',np.vstack((np.array(data)[:,2],np.array(deltatime))).T,fmt='%f',delimiter=',')
#'''