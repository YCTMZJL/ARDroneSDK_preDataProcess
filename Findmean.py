# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 20:18:32 2016

@author: ml
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
f1 = open('/home/ml/Software/ARDrone_SDK_2_0_1/Examples/Linux/Build/Release/mesures_20160901_104255.txt','rb')
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
###########################################################################
#np.savetxt('XYZacc_160705__205110_right.txt',data,fmt='%s',delimiter=' ')
############################################################################
data = np.array(data)
data = data
datainUse = data.copy()#/1000
##########################################
meanaccX =0#np.mean(data[1:,0].T)
meanaccY =0#np.mean(data[1:,1].T)
meanaccZ =0#np.mean(data[1:,2].T)
 #-1003.13 #-1001.37242649

length = len(data)
meanaccX = np.tile(meanaccX,length)
meanaccY = np.tile(meanaccY,length)
meanaccZ = np.tile(meanaccZ,length)
meanacc = np.vstack((meanaccX,meanaccY, meanaccZ)).T

print np.shape(meanacc)
datainUse[:,0:3] = datainUse[:,0:3].copy() - meanacc
##########################################
acc= datainUse[:,0:3].copy()
vel = datainUse[:,0:3].copy()
s = datainUse[:,0:3].copy()

time = 0.01

#for i in range(1,len(datainUse)):
 #   vel[i] = np.add( vel[i]*time, vel[i-1] )
 #   s[i] = np.add( vel[i]*time, s[i-1] )

for i in range(1,len(datainUse)):
    #vel[i] = np.add( vel[i]* deltatime[i], vel[i-1] )
    #curV = acc[i]
    curV=np.add (acc[i], acc[i-1])/2
    vel[i] = np.add( curV* time, vel[i-1] )
    ############################3
    #s[i] = np.add( vel[i]* deltatime[i], s[i-1] )
    #curS=vel[i]
    curS=np.add (vel[i], vel[i-1])/2
    s[i] = np.add( curS* time, s[i-1] )
    
print 's=',np.mean(s[:,2].T)
print 'accZ=',np.mean(data[:,2].T)
########################################################################
plt.figure('accXYZ2')

plt.plot(range(len(data[:,0].T)), data[:,0].T,'b.-',label='accX') #[:,8:11]
plt.plot(range(len(data[:,1].T)), data[:,1].T,'r.-',label='accY')
plt.plot(range(len(data[:,2].T)), data[:,2].T,'g.-',label='accZ')
'''
#############################################
plt.figure('sZ')
plt.plot(range(len(s[:,2].T)), s[:,2].T,'g.-',label='s')
#############################################
'''
'''
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

'''
###############################################################################
#fig = plt.figure('3D_s_160705_135048_left')# 据说是版本的wenti
#ax=plt.subplot(111,projection='3d') #创建一个三维的绘图工程
ax = Axes3D(fig)
#plt.plot_surface(s[:,0].T, s[:,1].T,s[:,1].T, rstride=1, cstride=1, cmap='rainbow')
ax.scatter(s[:,0],s[:,1],s[:,2],c='y') #绘点
ax.set_zlabel('Z') #坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()
##############################################################
#'''