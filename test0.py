# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 16:36:43 2016

@author: Jerry
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 17:52:45 2016

@author: Jerry
"""
import matplotlib.pyplot as plt
import numpy as np
import cPickle as cP
import math
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
    
################################################################
#datarecord = loadObj('Finout_data622_12_accXYZ.pkl')
#giventype = datarecord[0];
#print np.shape(giventype)
###############################################################
accXbase = -66.673#293#-66.67293196318596#2067.80448065 #np.mean(map(float,data[:,0].T))
accYbase = 47.619#24#47.619237568725275 #np.mean(map(float,data[:,1].T))
accZbase = -1025.73#019#-1025.7301925097195 #np.mean(map(float,data[:,2].T))
print accXbase, accYbase, accZbase
################################################################
f1 = open('resultdata/Findout-0623_1948_acc_ph_XYZ.txt','rb')#('result618/FindoutACCXYZ-6-18_1.txt','rb')
lines=f1.readlines();
f1.close()
count = 0
indexRecord = []
#line[0]
data = []
Infoline =  lines[0].split(',')
for i in range(1,len(lines)):
    temp = lines[i].split(',')
    data.append(map(float,temp))
data = np.array(data)
print data
'''
#8-10
#data1= np.array(datarecord)[1:,:]
data1= (datarecord)[1:len(datarecord)]
data = map(float,np.array(data1))
#data =np.array(datarecord)[:,0:3]
#'''
length = len(data)
accXbase = np.tile(accXbase,length)
accYbase = np.tile(accYbase,length)
accZbase = np.tile(accZbase,length)

acc = np.vstack((accXbase,accYbase, accZbase)).T

time = 0.01
data = data - acc
data = data/1000
datainUse = data.copy()
##########################################
vel = datainUse.copy()
s = datainUse.copy()
vel[0] = 0.0
s[0] =  0.0
for i in range(1,len(datainUse)):
    vel[i] = np.add( vel[i]*time, vel[i-1] )
    s[i] = np.add( vel[i]*time, s[i-1] )
  
############################################
plt.figure('ALL')
#plt.plot(range(6000), data[2000:8000,1].T*10000,'r.-',label='accX') #[:,8:11]
plt.plot(range(len(data[:,0].T*10000)), data[:,0].T*1000,'r.-',label='accX') #[:,8:11]
#plt.plot(range(len(data[:,1].T)), data[:,1].T*100,'r.-',label='accY')
#plt.plot(range(len(data[:,2].T)), data[:,2].T,'g.-',label='accZ')
#'''
#accXbase = 2067.80448065 #np.mean(map(float,data[:,0].T))
#accYbase = 2044.6065852 #np.mean(map(float,data[:,1].T))
#accZbase = 2540.59198914 #np.mean(map(float,data[:,2].T))
#print accXbase, accYbase, accZbase

#accYbase = np.mean(data[:,1])
#accZbase = np.mean(data[:,2])
################################################

'''
plt.plot(range(len(data[:,0].T)), data[:,0].T,'b.-',label='Pitchrc') #[:,8:11]
plt.plot(range(len(data[:,1].T)), data[:,1].T,'r.-',label='Rollrc')
plt.plot(range(len(data[:,2].T)), data[:,2].T,'g.-',label='Yawrc')
#'''
################################################
#plt.figure('velXYZ-623_1948')11
#plt.plot(range(6000), vel[2000:8000,1].T*10,'b.-',label='vY')

plt.plot(range(len(data[:,0].T)), vel[:,0].T,'b.-',label='vX') #[:,8:11]
#plt.plot(range(len(data[:,1].T)), vel[:,1].T*10,'b.-',label='vY')
#plt.plot(range(len(data[:,2].T)), vel[:,2].T,'g.-',label='vZ')

####################################################
#plt.figure('sXYZ-623_1948')#
#plt.plot(range(6000), s[2000:8000,1].T/1000,'g.-',label='sY')

plt.plot(range(len(data[:,0].T)), s[:,0].T/1000,'g.-',label='sX') #[:,8:11]
#plt.plot(range(len(data[:,1].T)), s[:,1].T/1000,'g.-',label='sY')
#plt.plot(range(len(data[:,2].T)), s[:,2].T,'g.-',label='sZ')
##########################################################################
plt.figure('acc')
plt.plot(range(9500), data[2000:11500,2].T,'g.-',label='accZ')
plt.plot(range(9500), data[2000:11500,0].T,'b.-',label='accX') #[:,8:11]
plt.plot(range(9500), data[2000:11500,1].T,'r.-',label='accY')
#plt.plot(range(len(data[:,2].T)), data[:,2].T,'g.-',label='accZ')
#################################################################
plt.figure('3D_s')#
ax=plt.subplot(111,projection='3d') #创建一个三维的绘图工程
#plt.plot_surface(s[:,0].T, s[:,1].T,s[:,1].T, rstride=1, cstride=1, cmap='rainbow')
ax.scatter(s[:,0],s[:,1],s[:,2],c='y') #绘点
ax.set_zlabel('Z') #坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()
##############################################################