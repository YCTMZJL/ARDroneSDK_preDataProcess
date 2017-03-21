# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 23:29:23 2016

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
datarecord = loadObj('Finout_data622_12_accXYZ.pkl')
giventype = datarecord[0];
print np.shape(giventype)
###############################################################
accXbase = 2067.80448065 #np.mean(map(float,data[:,0].T))
accYbase = 2044.6065852 #np.mean(map(float,data[:,1].T))
accZbase = 2540.59198914 #np.mean(map(float,data[:,2].T))
print accXbase, accYbase, accZbase
################################################################
f1 = open('Findout-617_21_accXYZ.txt','rb')
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
'''
#8-10
#data1= np.array(datarecord)[1:,:]
data1= (datarecord)[1:len(datarecord)]
data = map(float,np.array(data1))
#data =np.array(datarecord)[:,0:3]
#'''
length = len(data)
accXbase = np.tile(accXbase,length)

plt.figure(1)

plt.plot(range(len(data[:,0].T)), data[:,0].T,'b.-',label='accX') #[:,8:11]
plt.plot(range(len(data[:,1].T)), data[:,1].T,'r.-',label='accY')
plt.plot(range(len(data[:,2].T)), data[:,2].T,'g.-',label='accZ')
#'''
#accXbase = 2067.80448065 #np.mean(map(float,data[:,0].T))
#accYbase = 2044.6065852 #np.mean(map(float,data[:,1].T))
#accZbase = 2540.59198914 #np.mean(map(float,data[:,2].T))
#print accXbase, accYbase, accZbase

#accYbase = np.mean(data[:,1])
#accZbase = np.mean(data[:,2])


'''
plt.plot(range(len(data[:,0].T)), data[:,0].T,'b.-',label='Pitchrc') #[:,8:11]
plt.plot(range(len(data[:,1].T)), data[:,1].T,'r.-',label='Rollrc')
plt.plot(range(len(data[:,2].T)), data[:,2].T,'g.-',label='Yawrc')
#'''



