# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:44:19 2016

@author: ml
"""

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
#giventype = ['AccX_raw [LSB]', 'AccY_raw [LSB]','AccZ_raw [LSB]'] 
#AccX_phys_filt [mg]; AccY_phys_filt [mg]; AccZ_phys_filt [mg];
giventype = ['AccX_phys_filt [mg]','AccY_phys_filt [mg]','AccZ_phys_filt [mg]'] 
#giventype = ['Pitch_ref_embedded [mdeg]','Roll_ref_embedded [mdeg]','Yaw_ref_embedded [mdeg/s]'] 
#giventype = ['Pitch_rc_embedded [-]','Roll_rc_embedded [-]','Yaw_rc_embedded [-]'] 
#mesures_20160617_143452.txt
#f1 = open('data/2016-618/mesures_20160618_173049.txt','rb')

#f1 = open('/home/ml/Software/ARDrone_SDK_2_0_1/Examples/Linux/Build/Release/mesures_20161022_172811.txt','rb')
#savePath = 'result/'
#saveName = 'stable60min_mesures_20161022_172811'

f1 = open('/media/ml/JERRY32G/DataRes/res14/mesures_20170315_095638.txt')

savePath = '/media/ml/JERRY32G/DataRes/res14/'
saveName = 'mesures_20170315_095638'

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
for i in range(2,len(lines)):
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
    #temp = []
    linedata = lines[i].split(';')
    #temp.append(linedata[0].strip(' '))
    ####################################
    if ( i  ==  2 ) :
        deltatime.append(float(0))#yinggaixie1sange dangzhong1haixuyao1yige _
    else:
        deltatime.append(float(linedata[0].strip(' ')));
        

print np.shape(data)          

np.savetxt(savePath+'.csv',data,fmt='%f',delimiter=',')
np.savetxt(savePath+'_accX.csv',np.array(data)[:,0],fmt='%f',delimiter='')
np.savetxt(savePath+'_accY.csv',np.array(data)[:,1],fmt='%f',delimiter='')
np.savetxt(savePath+'_accZ.csv',np.array(data)[:,2],fmt='%f',delimiter='')


np.savetxt(savePath+'_timeInterval.csv',np.array(deltatime),fmt='%f',delimiter='')
'''
np.savetxt(savePath+'_accXwithTime.csv',np.vstack((np.array(data)[:,0],np.array(deltatime))).T,fmt='%f',delimiter=',')
np.savetxt(savePath+'_accYwithTime.csv',np.vstack((np.array(data)[:,1],np.array(deltatime))).T,fmt='%f',delimiter=',')
np.savetxt(savePath+'_accZwithTime.csv',np.vstack((np.array(data)[:,2],np.array(deltatime))).T,fmt='%f',delimiter=',')
#'''
