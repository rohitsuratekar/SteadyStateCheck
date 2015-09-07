import numpy as np
import matplotlib.pyplot as plt
import matplotlib

open_normal = 0  #0 = mutant , 1 = Normal , 2 = light, double mutant

if open_normal == 1:
    with open("current_result_log.txt") as original_parameters:
        k2 = [[float(digit) for digit in line.split()] for line in original_parameters]
    k2 = np.asarray(k2)
    k2 = k2[k2[:,0]< 0.1 , :]
#    k2 = k2[k2[:,15] > 28.2 , :]
#    k2 = k2[k2[:,15] < 28.7 , :]
    k1 = k2
    #plt.scatter(k1[:,16],k1[:,0],color = 'k', label='CDPDAG',alpha=1)
    #plt.scatter(k1[:,14],k1[:,0],color = 'y',label='PMPA',alpha=1)
    #plt.scatter(k1[:,15],k1[:,10],color = 'c', label='ERPA',alpha=1)
    #plt.scatter(k1[:,10],k1[:,0],color = 'b',label='PMPI',alpha=1)
    #plt.scatter(k1[:,11],k1[:,0],color = 'r',label='PI4P',alpha=1)
    #plt.scatter(k1[:,12],k1[:,0],color = 'g', label='PIP2',alpha=1)
    #plt.scatter(k1[:,13],k1[:,0],color = 'm', label='DAG',alpha=1)

    #plt.scatter(k1[:,0],k1[:,4],color = 'r', label='Error',alpha=1)
    #plt.scatter(k1[:,10],k1[:,14])
    #plt.hist(k1[:,6],100, alpha=0.5, label='Error From PIP2')
    #plt.hist(k1[:,7],100, alpha=0.5, label='Error From PI4P')
    #plt.hist(k1[:,8],100, alpha=0.5, label='Error From PA ')
    #plt.hist(k1[:,9],100, alpha=0.5, label='Error From DAG')
    #plt.hist(k1[:,10],100, alpha=0.5, label='PMPI')
    #plt.hist(k1[:,11],100, alpha=0.5, label='PI4P')
    #plt.hist(k1[:,12],100, alpha=0.5, label='PIP2')
    #plt.hist(k1[:,13],100, alpha=0.5, label='DAG')
    #plt.hist(k1[:,15],100, alpha=0.5, label='ERPA')
    #plt.hist(k1[:,14],100, alpha=0.5, label='PMPA')
    #plt.hist(k1[:,16],100, alpha=0.6, label='CDPDAG')


#print k1
if open_normal == 0:
    with open("mutant_log.txt") as original_parameters:
        k2 = [[float(digit) for digit in line.split()] for line in original_parameters]
    k2 = np.asarray(k2)
    #k2 = k2[k2[:,6] < 1000 , :] #Mutant factor less than this value
    k2 = k2[k2[:,6] != 1 , :]
    k1 = k2
    i1 = k1[:,15]/k1[:,7]
    i2 = k1[:,16]/k1[:,8]
    i3 = k1[:,17]/k1[:,9]
    i4 = k1[:,18]/k1[:,10]
    i5 = k1[:,19]/k1[:,11]
    i6 = k1[:,20]/k1[:,12]
    i7 = k1[:,21]/k1[:,13]
    i8 = k1[:,22]/k1[:,14]
    m1 = (k1[:,19]+k1[:,20])/(k1[:,11]+k1[:,12])
    m2 = (k1[:,15]+k1[:,22])/(k1[:,7]+k1[:,14])
    #plt.hist(m1,100, alpha=0.5, label='Total PA ')
    #plt.hist(m2,100, alpha=0.5, label='Total PI ')
    #plt.hist(i1,100, alpha=0.5, label='PMPI ')
    plt.hist(i2,100, alpha=0.5, label='PI4P ')
    plt.hist(i3,100, alpha=0.5, label='PIP2 ')
    plt.hist(i4,100, alpha=0.5, label='DAG')
    #plt.hist(i5,100, alpha=0.5, label='PMPA ')
    #plt.hist(i6,100, alpha=0.5, label='ERPA ')
    #plt.hist(i7,100, alpha=0.5, label='CDPDAG ')
    #plt.hist(i8,100, alpha=0.5, label='ERPI ')


if open_normal == 2:
    with open("light_recovery.txt") as original_parameters:
        k2 = [[float(digit) for digit in line.split()] for line in original_parameters]
    k2 = np.asarray(k2)
    k12 = k2[k2[:,5] == 12.8 , :]
    k8 = k2[k2[:,5] == 8 , :]
    k16 = k2[k2[:,5] == 1.6 , :]
    ksmall = k2[k2[:,5] == 0.16 , :]
    #k1 = k2
    plt.hist(k12[:,6],100, alpha=0.5, label='20 %')
    plt.hist(k8[:,6],100, alpha=0.5, label='50 %')
    plt.hist(k16[:,6],100, alpha=0.5, label='90 %')
    plt.hist(ksmall[:,6],100, alpha=0.5, label='99 %')

if open_normal == 3:
    with open("mutant_log.txt") as original_parameters:
        k2 = [[float(digit) for digit in line.split()] for line in original_parameters]
    k2 = np.asarray(k2)
    #k2 = k2[k2[:,6] < 1000 , :] #Mutant factor less than this value
    k2 = k2[k2[:,6] == 1 , :] #Enzyme 1
    k2 = k2[k2[:,8] != 1 , :] #Enzyme 2
    k1 = k2
    i1 = k1[:,17]/k1[:,9]
    i2 = k1[:,18]/k1[:,10]
    i3 = k1[:,19]/k1[:,11]
    i4 = k1[:,20]/k1[:,12]
    i5 = k1[:,21]/k1[:,13]
    i6 = k1[:,22]/k1[:,14]
    i7 = k1[:,23]/k1[:,15]
    i8 = k1[:,24]/k1[:,16]
    m1 = (k1[:,21]+k1[:,22])/(k1[:,13]+k1[:,14])
    m2 = (k1[:,17]+k1[:,24])/(k1[:,9]+k1[:,16])
    #plt.hist(m1,100, alpha=0.5, label='Total PA ')
    #plt.hist(m2,100, alpha=0.5, label='Total PI ')
    #plt.hist(i1,100, alpha=0.5, label='PMPI ')
    plt.hist(i2,100, alpha=0.5, label='PI4P ')
    #plt.hist(i3,100, alpha=0.5, label='PIP2 ')
    #plt.hist(i4,100, alpha=0.5, label='DAG')
    #plt.hist(i5,100, alpha=0.5, label='PMPA ')
    #plt.hist(i6,100, alpha=0.5, label='ERPA ')
    #plt.hist(i7,100, alpha=0.5, label='CDPDAG ')
    #plt.hist(i8,100, alpha=0.5, label='ERPI ')

plt.xlabel('Ratio os steady states ( PATP/WT)')
plt.ylabel('Frequency')
plt.title('PATP')
#plt.axhline()
#plt.axvline()
plt.legend(loc='upper left', bbox_to_anchor=(1, 0.5))
plt.savefig('samplefigure.png', bbox_inches='tight')
plt.show()
