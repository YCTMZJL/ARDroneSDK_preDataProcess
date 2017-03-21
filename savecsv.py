# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 11:25:34 2016

@author: PKU_Jerry
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
#giventype = ['AccX_phys_filt [mg]','AccY_phys_filt [mg]','AccZ_phys_filt [mg]'] 
#giventype = ['Pitch_ref_embedded [mdeg]','Roll_ref_embedded [mdeg]','Yaw_ref_embedded [mdeg/s]'] 
#giventype = ['Pitch_rc_embedded [-]','Roll_rc_embedded [-]','Yaw_rc_embedded [-]'] 
#mesures_20160617_143452.txt
#f1 = open('data/2016-618/mesures_20160618_173049.txt','rb')
f1 = open('data/2016-623/mesures_20160623_194834.txt','rb')
lines=f1.readlines();
f1.close()
count = 0
indexRecord = []
#line[0]
Infoline =  lines[1].split(';')
data = []
#for i in range(len(giventype)):
for j in range(len(Infoline)):
    indexRecord.append(Infoline[j].strip(' '))#去除字符串首末的空格
#data = [giventype] #[] #giventype#[];
data.append(indexRecord)
for i in range(2,len(lines)):
    #temp = []
    linedata = lines[i].strip('\n')
    linedata = lines[i].split(';')
    curdata=[]
    for line in linedata: 
        curdata.append(line.strip(' '))
    #print linedata
    #for index in indexRecord:
        #temp.append(float(linedata[index]))
    data.append(curdata)

#alldata = giventype + data
#alldata = np.array(giventype)
#alldata.append(giventype)
#saveObj(data, 'Finout_data617_14_PitchRollYaw_rc_embedded.pkl') 

#saveObj(data, 'Finout_624_161037_acc_ph_XYZ.pkl') 

print np.shape(indexRecord)          
#np.savetxt('Findout-6-18_1.txt',data,fmt='%.4f',delimiter=',')  
#mesures_20160617_143452.txt
np.savetxt('mesures_20160623_194834.csv',data,fmt='%s',delimiter=',')
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
