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
data = np.ones((100,3))

datainUse = data.copy()
##########################################
vel = datainUse.copy()
s = datainUse.copy()

for i in range(1,len(datainUse)):
    vel[i] = np.add( vel[i], vel[i-1] )
    s[i] = np.add( vel[i], s[i-1] )
  
############################################
plt.figure('acc')

plt.plot(range(len(data[:,0].T)), data[:,0].T,'b.-',label='accX') #[:,8:11]
#plt.plot(range(len(data[:,1].T)), data[:,1].T,'r.-',label='accY')
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
plt.figure('vel')
plt.plot(range(len(data[:,0].T)), vel[:,0].T,'b.-',label='vX') #[:,8:11]
#plt.plot(range(len(data[:,1].T)), vel[:,1].T,'r.-',label='vY')
#plt.plot(range(len(data[:,2].T)), vel[:,2].T,'g.-',label='vZ')

####################################################
plt.figure('s')
plt.plot(range(len(data[:,0].T)), s[:,0].T,'b.-',label='sX') #[:,8:11]
#plt.plot(range(len(data[:,1].T)), s[:,1].T,'r.-',label='sY')
#plt.plot(range(len(data[:,2].T)), s[:,2].T,'g.-',label='sZ')




