# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 14:13:40 2016

@author: ml
"""

import numpy as np
import cPickle as cP
import matplotlib.pyplot as plt
#import math
from mpl_toolkits.mplot3d import Axes3D 

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
    
##############################################


giventype1 = ['AccX_phys_filt [mg]','AccY_phys_filt [mg]','AccZ_phys_filt [mg]'] 
giventype2 = ['GyroX_phys_filt [deg/s]','GyroY_phys_filt [deg/s]','GyroZ_phys_filt [deg/s]'] 

giventype = giventype1 + giventype2

#f1 = open('/home/ml/Software/ARDrone_SDK_2_0_1/Example/Linux/Build/Realse/mesures_20160715_164903.txt','rb')
#f1 = open('mesures_20160715_164903.txt','rb')
f1 = open('/home/ml/Software/ARDrone_SDK_2_0_1/Examples/Linux/Build/Release/mesures_onlyup_20160729_193305.txt','rb')
lines=f1.readlines();
f1.close()
count = 0
indexRecord = []
Infoline =  lines[1].split(';')

for j in range(len(Infoline)):
    for i in range(len(giventype)):
        if (giventype[i] == Infoline[j].strip(' ')):#去除字符串首末的空格
            indexRecord.append(j)
            break;

timerecord=[]
deltatime = []
data = []#[giventype] #[] 

groupnum = 10   #每多少个区一次平均
sumdata = [0,0,0]
sumtime = [0]
meandata=[0,0,0]

for i in range(2,len(lines)):
    temp = []
    linedata = lines[i].split(';')
    timerecord.append(linedata[0].split('_'))
    ####################################
    if ( i  ==  2 ) :# day_h_m_ms
        deltatime.append(float(0))#yinggaixie1sange dangzhong1haixuyao1yige _
    elif(timerecord[i-2][0] == timerecord[i-3][0] and timerecord[i-2][1] == timerecord[i-3][1] and timerecord[i-2][2] == timerecord[i-3][2]):
        delta = (float(timerecord[i-2][3])- float(timerecord[i-3][3]))*0.001
        deltatime.append(delta)
       # if (delta*0.001>10 or delta*0.001==0): print i-2,'delta',delta
    elif(timerecord[i-2][0] == timerecord[i-3][0] and timerecord[i-2][1] == timerecord[i-3][1]):
        delta = (float(timerecord[i-2][3])-float(timerecord[i-3][3]))*0.001+(float(timerecord[i-2][2])-float(timerecord[i-3][2]))*60
        if (delta*0.001>10 or delta*0.001==0): print i-2,delta*0.001
        deltatime.append(delta)
    ######################################
    for index in indexRecord:
        temp.append(float(linedata[index]))
    data.append(temp)
    #######################################
    if ( i == 2 ):
         # sumdata = np.add(sumdata,np.array(data)[0:,0:3])
        #meandata = sumdata
        continue #头不作处理 
    elif ( i  ==  3 ):
    #elif ( i  <  3 +  groupnum ):
        sumdata = np.vstack(( sumdata, np.add(sumdata, np.array(data)[i-2,0:3]*(deltatime[i-2])) ))
        sumtime = np.vstack((sumtime,np.add(sumtime,np.array(deltatime)[i-2])))
        meandata = np.vstack((meandata,(sumdata[i-2] / sumtime[i-2])))
    elif ( i  <  3 +  groupnum ):
        sumdata = np.vstack((sumdata,np.add(sumdata[i-3],np.array(data)[i-2,0:3]*(deltatime[i-2]))))
        sumtime = np.vstack((sumtime,np.add(sumtime[i-3],np.array(deltatime)[i-2])))
        meandata = np.vstack((meandata,(sumdata[i-2] / sumtime[i-2])))
    #elif ( i  <  4+  groupnum ):
    else:
        sumdata = np.vstack((sumdata,np.add(sumdata[i-3],np.array(data)[i-2,0:3]*(deltatime[i-2])) - np.array(data)[i-2-groupnum ,0:3]*(deltatime[i-2-groupnum])  ))
        sumtime = np.vstack((sumtime,np.add(sumtime[i-3],np.array(deltatime)[i-2]) - np.array(deltatime)[i-2-groupnum] ))
        meandata = np.vstack((meandata,(sumdata[i-2] / sumtime[i-2])))
        
print np.shape(data)          
###########################################################################
#np.savetxt('XYZacc_160705__205110_right.txt',data,fmt='%s',delimiter=' ')
############################################################################
dataOri = np.array(data).copy()
data = np.array(meandata)#np.array(data)
datainUse = data.copy()#/1000
##########################################
meanaccX = np.mean(data[1:10,0].T)#-35.854862327 
print meanaccX
#-4.88260384226 #-26.6490947569 #- #12.2746653721
meanaccY =np.mean(data[1:,1].T)# 33.159057149
#67.7608625058#70.472140655##69.4756070888
meanaccZ =np.mean(data[1:,2].T)#-1031.950#-1028.0009666
#-1031.31441295#-#-1025.56600925# -1004.12261109
 #-1003.13 #-1001.37242649

length = len(data)
meanaccX = np.tile(meanaccX,length)
meanaccY = np.tile(meanaccY,length)
meanaccZ = np.tile(meanaccZ,length)
meanacc = np.vstack((meanaccX,meanaccY, meanaccZ)).T

print np.shape(meanacc)
datainUse[:,0:3] = datainUse[:,0:3].copy() - meanacc
datainUse[0] = [0,0,0]#第一组数设置为零
##########################################
vel = datainUse[:,0:3].copy()
s = datainUse[:,0:3].copy()

time = 0.01

for i in range(1,len(datainUse)):
    vel[i] = np.add( vel[i]* deltatime[i], vel[i-1] )
    s[i] = np.add( vel[i]* deltatime[i], s[i-1] )
    
print 's_mean=',np.mean(s[:,2].T)
print  'accX=',np.mean(data[1:,0].T),' accY=',np.mean(data[1:,1].T),' accZ=',np.mean(data[1:,2].T)
print  'accX_minusMean=',np.mean(datainUse[1:,0].T),' accY_minusMean=',np.mean(datainUse[1:,1].T),' accZ_minusMean=',np.mean(datainUse[1:,2].T)
########################################################################
plt.figure('accXYZ_ori')

#plt.plot(range(len(data[:,0].T)), dataOri[:,0].T,'b.-',label='accX') #[:,8:11]
#plt.plot(range(len(data[:,1].T)), dataOri[:,1].T,'r.-',label='accY')
plt.plot(range(len(data[:,2].T)), dataOri[:,2].T,'g.-',label='accZ')
####################################################
####################################################
plt.figure('accXYZ_Mean')

#plt.plot(range(len(data[:,0].T)), data[:,0].T,'b.-',label='accX') #[:,8:11]
#plt.plot(range(len(data[:,1].T)), data[:,1].T,'r.-',label='accY')
plt.plot(range(len(data[:,2].T)), data[:,2].T,'g.-',label='accZ')

####################################################
plt.figure('accXYZ_minusMean')

plt.plot(range(len(data[:,0].T)), datainUse[:,0].T,'b.-',label='accX') #[:,8:11]
plt.plot(range(len(data[:,1].T)), datainUse[:,1].T,'r.-',label='accY')
plt.plot(range(len(data[:,2].T)), datainUse[:,2].T,'g.-',label='accZ')

#############################################
plt.figure('sZ')
plt.plot(range(len(s[:,2].T)), s[:,2].T,'g.-',label='s')
#############################################
'''
##############################################################################
plt.figure('GyrosXYZ')

plt.plot(range(len(data[:,3].T)), data[:,3].T,'b.-',label='GyrosX') #[:,8:11]
plt.plot(range(len(data[:,4].T)), data[:,4].T,'r.-',label='GyrosY')
plt.plot(range(len(data[:,5].T)), data[:,5].T,'g.-',label='GyrosZ')
###############################################################################
plt.figure('Acc-GyrosX')

plt.plot(range(len(data[:,0].T)), data[:,0].T,'b.-',label='accX') #[:,8:11]
plt.plot(range(len(data[:,3].T)), data[:,3].T,'r.-',label='GyrosX')

#################################################################################
plt.figure('Acc-GyrosY')

plt.plot(range(len(data[:,1].T)), data[:,1].T,'b.-',label='accY') #[:,8:11]
plt.plot(range(len(data[:,4].T)), data[:,4].T,'r.-',label='GyrosY')

#################################################################################
plt.figure('Acc-GyrosZ')

plt.plot(range(len(data[:,2].T)), data[:,2].T,'c.-',label='accY') #[:,8:11]
plt.plot(range(len(data[:,5].T)), data[:,5].T,'m.-',label='GyrosY')

#'''
###############################################################################
fig = plt.figure('3D_s')# 据说是版本的wenti
#ax=plt.subplot(111,projection='3d') #创建一个三维的绘图工程
ax = Axes3D(fig)
#plt.plot_surface(s[:,0].T, s[:,1].T,s[:,1].T, rstride=1, cstride=1, cmap='rainbow')
ax.scatter(s[:,0],s[:,1],s[:,2],c='y') #绘点
ax.set_zlabel('Z') #坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()
##############################################################
#'''