# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 15:20:09 2016

@author: root
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

groupnumAcc = 10   #每多少个区一次平均
groupnumGyros = 20   #每多少个区一次平均
sumtimeAcc = [0]
sumdataAcc = [0,0,0]
meandataAcc=[0,0,0]
sumtimeGyros = [0]
sumdataGyros = [0,0,0]
meandataGyros=[0,0,0]

for i in range(2,len(lines)):
    temp = []
    linedata = lines[i].split(';')
    timerecord.append(linedata[0].split('_'))
    ####################################For deltaTime
    if ( i  ==  2 ) :
        deltatime.append(float(0))#yinggaixie1sange dangzhong1haixuyao1yige _
    elif(timerecord[i-2][0] == timerecord[i-3][0] and timerecord[i-2][1] == timerecord[i-3][1] and timerecord[i-2][2] == timerecord[i-3][2]):
        delta = (float(timerecord[i-2][3])- float(timerecord[i-3][3]))*0.001
        deltatime.append(delta)
       # if (delta*0.001>10 or delta*0.001==0): print i-2,'delta',delta
    elif(timerecord[i-2][0] == timerecord[i-3][0] and timerecord[i-2][1] == timerecord[i-3][1]):
        delta = (float(timerecord[i-2][3])-float(timerecord[i-3][3]))*0.001+(float(timerecord[i-2][2])-float(timerecord[i-3][2]))*60
        if (delta*0.001>10 or delta*0.001==0): print i-2,delta*0.001
        deltatime.append(delta)#单位是秒
    ######################################For ori Data
    for index in indexRecord:
        temp.append(float(linedata[index]))
    data.append(temp)
    #######################################For Acc
    if ( i == 2 ):
         # sumdata = np.add(sumdata,np.array(data)[0:,0:3])
        #meandata = sumdata
        continue #头不作处理 
    elif ( i  ==  3 ):
    #elif ( i  <  3 +  groupnum ):
        sumdataAcc = np.vstack(( sumdataAcc, np.add(sumdataAcc, np.array(data)[i-2,0:3]*(deltatime[i-2])) ))
        sumtimeAcc = np.vstack((sumtimeAcc,np.add(sumtimeAcc,np.array(deltatime)[i-2])))
        meandataAcc = np.vstack((meandataAcc,(sumdataAcc[i-2] / sumtimeAcc[i-2])))
    elif ( i  <  3 +  groupnumAcc ):
        sumdataAcc= np.vstack((sumdataAcc,np.add(sumdataAcc[i-3],np.array(data)[i-2,0:3]*(deltatime[i-2]))))
        sumtimeAcc= np.vstack((sumtimeAcc,np.add(sumtimeAcc[i-3],np.array(deltatime)[i-2])))
        meandataAcc = np.vstack((meandataAcc,(sumdataAcc[i-2] / sumtimeAcc[i-2])))
    #elif ( i  <  4+  groupnum ):
    else:
        sumdataAcc = np.vstack((sumdataAcc,np.add(sumdataAcc[i-3],np.array(data)[i-2,0:3]*(deltatime[i-2])) - np.array(data)[i-2-groupnumAcc  ,0:3]*(deltatime[i-2-groupnumAcc ])  ))
        sumtimeAcc = np.vstack((sumtimeAcc,np.add(sumtimeAcc[i-3],np.array(deltatime)[i-2]) - np.array(deltatime)[i-2-groupnumAcc ] ))
        meandataAcc = np.vstack((meandataAcc,(sumdataAcc[i-2] / sumtimeAcc[i-2])))

#######################################For Gyros
    if ( i == 2 ):
         # sumdata = np.add(sumdata,np.array(data)[0:,0:3])
        #meandata = sumdata
        continue #头不作处理 
    elif ( i  ==  3 ):
    #elif ( i  <  3 +  groupnum ):
        sumdataGyros = np.vstack(( sumdataGyros, np.add(sumdataGyros, np.array(data)[i-2,3:6]*(deltatime[i-2])) ))
        sumtimeGyros = np.vstack((sumtimeGyros,np.add(sumtimeGyros,np.array(deltatime)[i-2])))
        meandataGyros = np.vstack((meandataGyros , (sumdataGyros[i-2] / sumtimeGyros[i-2])))
    elif ( i  <  3 +  groupnumGyros ):
        sumdataGyros = np.vstack((sumdataGyros , np.add(sumdataGyros[i-3] , np.array(data)[i-2,3:6]*(deltatime[i-2]))))
        sumtimeGyros = np.vstack((sumtimeGyros , np.add(sumtimeGyros[i-3] , np.array(deltatime)[i-2])))
        meandataGyros = np.vstack((meandataGyros , (sumdataGyros[i-2] / sumtimeGyros[i-2])))
    #elif ( i  <  4+  groupnum ):
    else:
        sumdataGyros = np.vstack((sumdataGyros,np.add(sumdataGyros[i-3],np.array(data)[i-2,3:6]*(deltatime[i-2])) - np.array(data)[i-2-groupnumGyros ,3:6]*(deltatime[i-2-groupnumGyros])  ))
        sumtimeGyros = np.vstack((sumtimeGyros,np.add(sumtimeGyros[i-3],np.array(deltatime)[i-2]) - np.array(deltatime)[i-2-groupnumGyros] ))
        meandataGyros = np.vstack((meandataGyros , (sumdataGyros[i-2] / sumtimeGyros[i-2])))
        
print np.shape(data)          
###########################################################################
meandata = np.hstack((meandataAcc,meandataGyros))
############################################################################
dataOri = np.array(data).copy()
data = np.array(meandata)#np.array(data)
datainUse = data.copy()#/1000
##########################################
meanaccX = -4.88260384226 #-26.6490947569 #- #12.2746653721
meanaccY = 67.7608625058#70.472140655##69.4756070888
meanaccZ = -1031.31441295#-#-1025.56600925# -1004.12261109
 #-1003.13 #-1001.37242649

length = len(data)
meanaccX = np.tile(meanaccX,length)
meanaccY = np.tile(meanaccY,length)
meanaccZ = np.tile(meanaccZ,length)
meanacc = np.vstack((meanaccX,meanaccY, meanaccZ)).T

print np.shape(meanacc)
datainUse[:,0:3] = datainUse[:,0:3].copy() - meanacc
datainUse[0,0:3] = [0,0,0]
##########################################
vel = datainUse[:,0:3].copy()
s = datainUse[:,0:3].copy()

time = 0.01

for i in range(1,len(datainUse)):
    vel[i] = np.add( vel[i]* deltatime[i], vel[i-1] )
    s[i] = np.add( vel[i]* deltatime[i], s[i-1] )
    
print 's=',np.mean(s[:,2].T)
print  'accX=',np.mean(data[:,0].T),' accY=',np.mean(data[:,1].T),' accZ=',np.mean(data[:,2].T)
print  'accX_minusMean=',np.mean(datainUse[:,0].T),' accY_minusMean=',np.mean(datainUse[:,1].T),' accZ_minusMean=',np.mean(datainUse[:,2].T)
########################################################################
plt.figure('accXYZ_ori')

plt.plot(range(len(data[:,0].T)), dataOri[:,0].T,'b.-',label='accX') #[:,8:11]
plt.plot(range(len(data[:,1].T)), dataOri[:,1].T,'r.-',label='accY')
plt.plot(range(len(data[:,2].T)), dataOri[:,2].T,'g.-',label='accZ')
####################################################
####################################################
plt.figure('accXYZ_Mean')

plt.plot(range(len(data[:,0].T)), data[:,0].T,'b.-',label='accX') #[:,8:11]
plt.plot(range(len(data[:,1].T)), data[:,1].T,'r.-',label='accY')
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