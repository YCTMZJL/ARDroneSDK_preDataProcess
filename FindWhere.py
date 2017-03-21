# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 20:00:32 2016

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
f1 = open('/home/ml/Software/ARDrone_SDK_2_0_1/Examples/Linux/Build/Release/mesures_stable_20160718_162432.txt','rb')
lines=f1.readlines();
f1.close()
count = 0
indexRecord = []#加上时间
#line[0]
Infoline =  lines[1].split(';')
for i in range(len(giventype)):
    for j in range(len(Infoline)):
        if(giventype[i] == Infoline[j].strip(' ')):#去除字符串首末的空格
            indexRecord.append(j)
            break;
#data = [giventype] #[] #giventype#[];
data=[]
for i in range(2,len(lines)):
    temp = []
    linedata = lines[i].split(';')
    for index in indexRecord:
        temp.append(float(linedata[index]))
    data.append(temp)

#alldata = giventype + data
#alldata = np.array(giventype)
#alldata.append(giventype)
#saveObj(data, 'Finout_data617_14_PitchRollYaw_rc_embedded.pkl') 

#saveObj(data, 'Finout_624_161037_acc_ph_XYZ.pkl') 

print np.shape(data)          
np.savetxt('stable_20160718_162432.txt',data,fmt='%.4f',delimiter=',')  
#mesures_20160617_143452.txt
#================================================================
#np.savetxt('XYZacc_160705__205110_right.txt',data,fmt='%s',delimiter=' ')
#np.savetxt('Findout623_194834_acXYZ.txt',data,fmt='%s',delimiter=',')    
#  mesures_20160623_194834.txt 
'''
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
    #datarecord = datarecord  + [temp]
    if (count % 5 == 0):
        datarecord = datarecord  + [temp]
        temp = []
#'''