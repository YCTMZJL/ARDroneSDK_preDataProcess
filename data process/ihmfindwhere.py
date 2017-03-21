# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 17:30:31 2016

@author: ml
"""

# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 15:33:19 2016
Find relation
@author: Jerry
"""
import numpy as np
import cPickle as cP
import matplotlib.pyplot as plt
#import math
from mpl_toolkits.mplot3d import Axes3D 

# 持久化保存对象
def saveObj(obj, filePath):
    file_obj = open(filePath, "wb")
    cP.dump(obj, file_obj)
    file_obj.close()

# 加载持久化的对象
def loadObj(filePath):
    file_obj = open(filePath, "rb")
    obj = cP.load(file_obj)
    return obj
    
##############################################

f1 = open('/media/ml/JERRY32G/DataRes/res15/ihm_recordInfo_20170316_104440.txt')

savePath = '/media/ml/JERRY32G/DataRes/res15/'
saveName = 'ihm_recordInfo_20170316_104440'
savePath = savePath + saveName

lines=f1.readlines();
f1.close()
count = 0
Infoline =  lines[1].split(';')
###########################################################################
data =[]
for i in range(len(lines)):
    linedata = lines[i].strip('\n ')
    linedata = lines[i].split('  ')
    linedata = map(float, linedata)
    data.append((linedata))
        
data = np.array(data)
print np.shape(data)          

#######################################################
plt.figure('accXYZ')

plt.plot(range(len(data[:,6].T)), data[:,6].T,'b.-',label='accX') #[:,8:11]
plt.plot(range(len(data[:,7].T)), data[:,7].T,'r.-',label='accY')
plt.plot(range(len(data[:,8].T)), data[:,8].T,'g.-',label='accZ')
##############################################################################
plt.figure('GyrosXYZ')

plt.plot(range(len(data[:,4].T)), data[:,3].T,'b.-',label='GyrosX') #[:,8:11]
plt.plot(range(len(data[:,5].T)), data[:,4].T,'r.-',label='GyrosY')
plt.plot(range(len(data[:,6].T)), data[:,5].T,'g.-',label='GyrosZ')
###############################################################################
plt.figure('dx-dy')

plt.plot(range(len(data[:,0].T)), data[:,1].T,'b.-',label='accX') #[:,8:11]
plt.plot(range(len(data[:,3].T)), data[:,2].T,'r.-',label='GyrosX')

#################################################################################

#np.savetxt(savePath+'.csv',data,fmt='%f',delimiter=',')
np.savetxt(savePath+'_dX.csv',np.array(data)[:,1],fmt='%f',delimiter='')
np.savetxt(savePath+'_dY.csv',np.array(data)[:,2],fmt='%f',delimiter='')
np.savetxt(savePath+'_accX.csv',np.array(data)[:,6],fmt='%f',delimiter='')
np.savetxt(savePath+'_accY.csv',np.array(data)[:,7],fmt='%f',delimiter='')
np.savetxt(savePath+'_accZ.csv',np.array(data)[:,8],fmt='%f',delimiter='')
np.savetxt(savePath+'_GyrosX.csv',np.array(data)[:,3],fmt='%f',delimiter='')
np.savetxt(savePath+'_GyrosY.csv',np.array(data)[:,4],fmt='%f',delimiter='')
np.savetxt(savePath+'_GyrosZ.csv',np.array(data)[:,5],fmt='%f',delimiter='')


np.savetxt(savePath+'_timeInterval.csv',np.array(data)[:,0],fmt='%f',delimiter='')
#'''