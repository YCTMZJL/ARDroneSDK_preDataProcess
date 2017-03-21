# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 11:01:09 2016

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
    
#for which type I need
giventype = ['AccX_raw [LSB]', 'AccY_raw [LSB]','AccZ_raw [LSB]'] 
#AccX_phys_filt [mg]; AccY_phys_filt [mg]; AccZ_phys_filt [mg];
giventype =giventype + ['AccX_phys_filt [mg]','AccY_phys_filt [mg]','AccZ_phys_filt [mg]'] 
#giventype = ['Pitch_ref_embedded [mdeg]','Roll_ref_embedded [mdeg]','Yaw_ref_embedded [mdeg/s]'] 
#giventype = ['Pitch_rc_embedded [-]','Roll_rc_embedded [-]','Yaw_rc_embedded [-]'] 
#mesures_20160617_143452.txt
#f1 = open('data/2016-618/mesures_20160618_173049.txt','rb')
f1 = open('F:/Jerry/DATA/Data9_13/mesures_stable120_20160913_150035.txt','rb')
savePath = 'F:/Jerry/FLY_DATA/'
saveName = 'test'
savePath = savePath + saveName
lines=f1.readlines();
f1.close()
count = 0
indexRecord = []
#line[0]
Infoline =  lines[1].split(';')
for i in range(len(giventype)):
    for j in range(len(Infoline)):
        if(giventype[i] == Infoline[j].strip(' ')):#去除字符串首末的空格
            indexRecord.append(j)
            break;
data = []#[giventype] #[] #giventype#[];
for i in range(2,5002):
#for i in range(2,5002):
    temp = []
    linedata = lines[i].split(';')
    for index in indexRecord:
        temp.append(float(linedata[index]))
    data.append(temp)

timerecord=[]
deltatime = []

for i in range(2,len(lines)):
#for i in range(2,5002):#len(lines)):
    temp = []
    linedata = lines[i].split(';')
    timerecord.append(linedata[0].split('_'))
    ####################################
    if ( i  ==  2 ) :
        deltatime.append(float(0))#yinggaixie1sange dangzhong1haixuyao1yige _
    elif(timerecord[i-2][0] == timerecord[i-3][0] and timerecord[i-2][1] == timerecord[i-3][1] and timerecord[i-2][2] == timerecord[i-3][2]):
        delta = (float(timerecord[i-2][3])- float(timerecord[i-3][3]))*0.001
        deltatime.append(delta)
       # if (delta*0.001>10 or delta*0.001==0): print i-2,'delta',delta
    elif(timerecord[i-2][0] == timerecord[i-3][0] and timerecord[i-2][1] == timerecord[i-3][1]):
        delta = (float(timerecord[i-2][3])-float(timerecord[i-3][3]))*0.001+(float(timerecord[i-2][2])-float(timerecord[i-3][2]))*60
        if (delta*0.001>10 or delta*0.001==0): print i-2,delta*0.001
        deltatime.append(delta)



np.savetxt(savePath+'.csv',data,fmt='%f',delimiter=',')

print np.shape(data)          
'''
np.savetxt(savePath+'.csv',data,fmt='%f',delimiter=',')
np.savetxt(savePath+'_accX.csv',np.array(data)[:,0],fmt='%f',delimiter='')
np.savetxt(savePath+'_accY.csv',np.array(data)[:,1],fmt='%f',delimiter='')
np.savetxt(savePath+'_accZ.csv',np.array(data)[:,2],fmt='%f',delimiter='')


np.savetxt(savePath+'_timeInterval.csv',np.array(deltatime),fmt='%f',delimiter='')

np.savetxt(savePath+'_accXwithTime.csv',np.vstack((np.array(data)[:,0],np.array(deltatime))).T,fmt='%f',delimiter=',')
np.savetxt(savePath+'_accYwithTime.csv',np.vstack((np.array(data)[:,1],np.array(deltatime))).T,fmt='%f',delimiter=',')
np.savetxt(savePath+'_accZwithTime.csv',np.vstack((np.array(data)[:,2],np.array(deltatime))).T,fmt='%f',delimiter=',')
#'''
