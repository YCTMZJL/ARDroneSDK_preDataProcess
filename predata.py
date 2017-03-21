# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 15:33:55 2016
[0]: 0000;,
@author: Jerry
"""
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
#giventype = ['aw_gyros[X]','raw_gyros[Y]']#'raw_gyros[Z]','raw_gyros_110','raw_gyros_110[1]','magneto.mx','magneto.my','magneto.mz','magneto_raw.x','magneto_raw.y','magneto_raw.z','magneto_rectified.x','magneto_rectified.y','magneto_rectified.z','magneto_offset.x','magneto_offset.y','magneto_offset.z'}
#giventype.shape
print np.shape(giventype)
datarecord = []
'''

res = []
for j in range(3):
    temp=[]
    for i in range(9):
        #temp = np.column_stack((temp,i))#
        temp.append(i)
    #res = np.row_stack((res,temp)) # top = np.column_stack((a, np.zeros((3,3))))
    res = res + [temp]
print np.shape(res)
    
'''
f1 = open('data/2016-618/record_file_20160618_173049.txt','rb')
lines=f1.readlines();
f1.close()
count = 0
temp = []
for line in lines:
    count = count +1
    print count
    #line=line.strip('\n')
    datamerge = line.split(';')
    #temp=[]
    for datamergepart in datamerge:
        data = datamergepart.split(':')
        flag = 0
        for i in range(len(giventype)):
            if data[0] == giventype[i]:
                #print 'find'
                flag = 1
                temp.append(float(data[1]))
                break
        '''
        if flag == 1:
            print 'nofind'
            temp.append(0)
        '''
    #datarecord = datarecord  + [temp]
    if (count % 5 == 0):
        datarecord = datarecord  + [temp]
        temp = []
        
saveObj(datarecord, 'data618_18.pkl') 
print np.shape(datarecord)          
np.savetxt('out-6-18_1.txt',datarecord,fmt='%.4f',delimiter=',')    

   

 #'''     
