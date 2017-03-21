# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:37:57 2016

@author: Jerry
"""
import numpy as np

#filepath = 'F:/实验结果/新实验结果10_120s/速度均值位移均值为零/'
filepath = 'F:/实验结果/新实验结果10_120s/加速度均值位移均值为零/'
filepath=unicode(filepath,'utf8')
f1 = open(filepath+'TotalTime.csv','rb')
f2 = open(filepath+'Value_X-Speed.csv','rb')
f3 = open(filepath+'Value_Y-Speed.csv','rb')
f4 = open(filepath+'Value_Z-Speed.csv','rb')

savePath = filepath


lines=f1.readlines();
linesX=f2.readlines();
linesY=f3.readlines();
linesZ=f4.readlines();

totaltime = []
dataX =[]
dataY=[]
dataZ=[]

for i in range(0,len(lines)-1):
#for i in range(2,5002):#len(lines)):
    linedata = lines[i].strip('\r')
    linedata = lines[i].split(',')
    linedata[0] = float(linedata[0].strip(' '))
    
    linedataX = linesX[i].strip('\r')
    linedataX = linesX[i].split(',')
    linedataX[0] = float(linedataX[0].strip(' '))
    
    linedataY = linesY[i].strip('\r')
    linedataY = linesY[i].split(',')
    linedataY[0] = float(linedataY[0].strip(' '))
    
    linedataZ = linesZ[i].strip('\r')
    linedataZ = linesZ[i].split(',')
    linedataZ[0] = float(linedataZ[0].strip(' '))
    #print linedata
    if i == 0 :
        totaltime = np.array(linedata[0]);
        dataX = np.array(linedataX[0]);
        dataY = np.array(linedataY[0]);
        dataZ = np.array(linedataZ[0]);
        #totaltime.append(linedata[0])
    #elif i==1:
        #tmp = np.add(totaltime,np.array(linedata[0]))
        #totaltime = np.vstack((totaltime,tmp))
    else:
        #tmp = np.add(totaltime[i-1],np.array(linedata[0]))
        totaltime=np.vstack((totaltime,np.array(linedata[0])))
        dataX = np.vstack((dataX,np.array(linedataX[0])));
        dataY = np.vstack((dataY,np.array(linedataY[0])));
        dataZ = np.vstack((dataZ,np.array(linedataZ[0])));
        #totaltime.append(totaltime[i-1]+linedata[0])

print np.shape(np.array(totaltime))
np.savetxt(savePath+'Value_X-Speed.txt',np.hstack((totaltime,dataX)),fmt='%f',delimiter=' ')
np.savetxt(savePath+'Value_Y-Speed.txt',np.hstack((totaltime,dataY)),fmt='%f',delimiter=' ')
np.savetxt(savePath+'Value_Z-Speed.txt',np.hstack((totaltime,dataZ)),fmt='%f',delimiter=' ')