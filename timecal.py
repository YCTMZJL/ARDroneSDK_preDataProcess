# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 15:33:55 2016
[0]: 0000;,
for time cal
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


giventype = ['TimeRecord']

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
f1 = open('data/2016-622/record_file_20160622_124924.txt','rb')
lines=f1.readlines();
f1.close()
count = 0
countTime = 0
pretime = '0'
maxcountTime = 0
temp = []
record =[]
for line in lines:
    count = count +1
    #print count
    line = line.strip('\n')
    data = line.split(':')    
    if data[0] == giventype[0]:
        if data[1] == pretime:
            countTime = countTime + 1
        else:
            record.append(countTime)
            maxcountTime = max(maxcountTime,countTime)
            #print maxcountTime
            countTime = 1
            temp.append(data[1])
            pretime = data[1]
   
#print maxcountTime      
#saveObj(temp, 'data622_12_time.pkl') 
print np.shape(temp)          
np.savetxt('out20160622_124924_time.txt',record,fmt='%.4f',delimiter=',')    

   

 #'''     

