# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 17:52:45 2016

@author: Jerry
"""
import matplotlib.pyplot as plt
import numpy as np
import cPickle as cP
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

################################################################
f1 = open('debug.txt','rb')#('result618/FindoutACCXYZ-6-18_1.txt','rb')
lines=f1.readlines();
f1.close()
count = 0
indexRecord = []
#line[0]
data = []
#Infoline =  lines[0].split(',')
for line in lines:
    temp = line.strip('\n')
    temp = temp.split()
    data.append(map(float,temp))
    #data.append(map(str,temp))
    #data.append(temp)
data = np.array(data)
#data = np.array(map(float,data))


#data = data - acc
datainUse = data.copy()
##########################################
vel = datainUse.copy()#/1000
s = datainUse.copy()#/1000

for i in range(1,len(datainUse)):
    vel[i] = np.add( vel[i], vel[i-1] )
    s[i] = np.add( vel[i], s[i-1] )
  
############################################
plt.figure('acc_thetaphi_6_23')

plt.plot(range(len(data[:,0].T)), data[:,0].T,'b.-',label='accPhi') #[:,8:11]
plt.plot(range(len(data[:,1].T)), data[:,1].T,'r.-',label='accTheta')
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
plt.figure('vel_thetaphi_6_23')
plt.plot(range(len(data[:,0].T)), vel[:,0].T,'b.-',label='vX') #[:,8:11]
plt.plot(range(len(data[:,1].T)), vel[:,1].T,'r.-',label='vY')
#plt.plot(range(len(data[:,2].T)), vel[:,2].T,'g.-',label='vZ')
plt.figure('s_thetaphi_6_23')
#plt.plot(range(len(data[:,0].T)), (s[:,0].T % 360),'b.-',label='sX') #[:,8:11]
#plt.plot(range(len(data[:,1].T)), (s[:,1].T % 360),'r.-',label='sY')
#plt.plot(range(len(data[:,2].T)), s[:,2].T,'g.-',label='sZ')
plt.plot(range(300), (s[0:300,0].T % 360),'b.-',label='sX') #[:,8:11]
plt.plot(range(300), (s[0:300,1].T % 360),'r.-',label='sY')


