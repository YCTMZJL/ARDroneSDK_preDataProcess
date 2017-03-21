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
giventype1 = ['AccX_phys_filt [mg]','AccY_phys_filt [mg]','AccZ_phys_filt [mg]'] 
giventype2 = ['GyroX_phys_filt [deg/s]','GyroY_phys_filt [deg/s]','GyroZ_phys_filt [deg/s]'] 

giventype = giventype1 + giventype2

#f1 = open('/home/ml/Software/ARDrone_SDK_2_0_1/Example/Linux/Build/Realse/mesures_20160715_164903.txt','rb')
#f1 = open('mesures_20160715_164903.txt','rb')
#f1 = open('/home/ml/Software/ARDrone_SDK_2_0_1/Examples/Linux/Build/Release/mesures_20161022_152717.txt','rb')
f1 = open('/media/ml/JERRY32G/DataRes/res23/mesures_20170319_110145.txt')

savePath ='/media/ml/JERRY32G/DataRes/res23/'
saveName = 'mesures_20170319_110145'
savePath = savePath + saveName

lines=f1.readlines();
f1.close()
count = 0
indexRecord = []
Infoline =  lines[1].split(';')
for i in range(len(giventype)):
    for j in range(len(Infoline)):
        if(giventype[i] == Infoline[j].strip(' ')):#去除字符串首末的空格
            indexRecord.append(j)
            break;
data = []#[giventype] #[] 
for i in range(2,len(lines)):
    temp = []
    linedata = lines[i].split(';')
    for index in indexRecord:
        temp.append(float(linedata[index]))
    data.append(temp)
print np.shape(data)          
data = np.array(data)
###########################################################################
timerecord=[]
deltatime = []

for i in range(2,len(lines)):
#for i in range(2,5002):#len(lines)):
    #temp = []
    linedata = lines[i].split(';')
    #temp.append(linedata[0].strip(' '))
    ####################################
    if ( i  ==  2 ) :
        deltatime.append(float(0))#yinggaixie1sange dangzhong1haixuyao1yige _
    else:
        deltatime.append(float(linedata[0].strip(' ')));
        

print np.shape(data)          

#######################################################
plt.figure('accXYZ')

plt.plot(range(len(data[:,0].T)), data[:,0].T,'b.-',label='accX') #[:,8:11]
plt.plot(range(len(data[:,1].T)), data[:,1].T,'r.-',label='accY')
plt.plot(range(len(data[:,2].T)), data[:,2].T,'g.-',label='accZ')
##############################################################################
plt.figure('GyrosXYZ')

plt.plot(range(len(data[:,3].T)), data[:,3].T,'b.-',label='GyrosX') #[:,8:11]
plt.plot(range(len(data[:,4].T)), data[:,4].T,'r.-',label='GyrosY')
plt.plot(range(len(data[:,5].T)), data[:,5].T,'g.-',label='GyrosZ')
###############################################################################
plt.figure('Acc-GyrosX')

plt.plot(range(len(data[:,0].T)), data[:,0].T,'b.-',label='accX') #[:,8:11]
plt.plot(range(len(data[:,3].T)), data[:,3].T,'r.-',label='GyrosX')

#################################################################################
plt.figure('Acc-GyrosY')

plt.plot(range(len(data[:,1].T)), data[:,1].T,'b.-',label='accY') #[:,8:11]
plt.plot(range(len(data[:,4].T)), data[:,4].T,'r.-',label='GyrosY')

#################################################################################
plt.figure('Acc-GyrosZ')

plt.plot(range(len(data[:,2].T)), data[:,2].T,'c.-',label='accY') #[:,8:11]
plt.plot(range(len(data[:,5].T)), data[:,5].T,'m.-',label='GyrosY')

np.savetxt(savePath+'.csv',data,fmt='%f',delimiter=',')
np.savetxt(savePath+'_accX.csv',np.array(data)[:,0],fmt='%f',delimiter='')
np.savetxt(savePath+'_accY.csv',np.array(data)[:,1],fmt='%f',delimiter='')
np.savetxt(savePath+'_accZ.csv',np.array(data)[:,2],fmt='%f',delimiter='')
np.savetxt(savePath+'_GyrosX.csv',np.array(data)[:,3],fmt='%f',delimiter='')
np.savetxt(savePath+'_GyrosY.csv',np.array(data)[:,4],fmt='%f',delimiter='')
np.savetxt(savePath+'_GyrosZ.csv',np.array(data)[:,5],fmt='%f',delimiter='')


np.savetxt(savePath+'_timeInterval.csv',np.array(deltatime),fmt='%f',delimiter='')