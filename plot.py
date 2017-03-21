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
giventype = ['raw_gyros[X]','raw_gyros[Y]','raw_gyros[Z]','raw_gyros_110[0]','raw_gyros_110[1]',
'magneto.mx','magneto.my','magneto.mz','magneto_raw.x','magneto_raw.y','magneto_raw.z',
'magneto_rectified.x','magneto_rectified.y','magneto_rectified.z','magneto_offset.x','magneto_offset.y','magneto_offset.z']

print np.shape(giventype)
datarecord = loadObj('data1_1.pkl')

#8-10
data =np.array(datarecord)[:,8:11]
#data =np.array(datarecord)[:,0:3]
plt.figure(1)

plt.plot(range(len(data[:,0].T)), data[:,0].T,'b.-',label='magneto_raw.x') #[:,8:11]
plt.plot(range(len(data[:,1].T)), data[:,1].T,'r.-',label='magneto_raw.y')
plt.plot(range(len(data[:,2].T)), data[:,2].T,'g.-',label='magneto_raw.z')
#'''
'''
plt.plot(range(len(data[:,0].T)), data[:,0].T,'b.-',label='raw_gyros[X]') #[:,0:3]
plt.plot(range(len(data[:,1].T)), data[:,1].T,'r.-',label='raw_gyros[Y]')
plt.plot(range(len(data[:,2].T)), data[:,2].T,'g.-',label='raw_gyros[Z]')
#'''



