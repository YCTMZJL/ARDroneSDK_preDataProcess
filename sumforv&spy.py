# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:18:43 2016
cal v & s with supposing that  
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
    

#datarecord = loadObj('Finout_data617_21_accXYZ.pkl')
f1 = open('Findout-617_21_accXYZ.txt','rb')
lines=f1.readlines();
f1.close()
count = 0
indexRecord = []
#line[0]
Infoline_type =  lines[0].split(',')

data =[]
data.append(map(float,lines[1].split(',')));
s = data[0]
vel = data[0]
for i in range(2,len(lines)):
    linedata = lines[i].strip('\n')
    linedata = linedata.strip('\r')
    linedata = linedata.split(',')
    data.append(map(float,linedata))
    #vel.append([np.add(data[i-1],vel[i-2])])
    #s.append([np.add(vel[i-1],s[i-2])])
data = np.array(data)
#8-10
print np.shape(data)
vel = data
s = data
for i in range(2,len(data)):
    vel[i] = np.add( vel[i], vel[i-1] )
    s[i] = np.add( vel[i], s[i-1] )

plt.figure(1)
plt.plot(range(len(data[:,0].T)), vel[:,0].T,'b.-',label='vX') #[:,8:11]
plt.plot(range(len(data[:,1].T)), vel[:,1].T,'r.-',label='vY')
plt.plot(range(len(data[:,2].T)), vel[:,2].T,'g.-',label='vZ')
plt.figure(2)
plt.plot(range(len(data[:,0].T)), s[:,0].T,'b.-',label='sX') #[:,8:11]
plt.plot(range(len(data[:,1].T)), s[:,1].T,'r.-',label='sY')
plt.plot(range(len(data[:,2].T)), s[:,2].T,'g.-',label='sZ')