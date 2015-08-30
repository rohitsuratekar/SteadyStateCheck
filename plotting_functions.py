import numpy as np
import matplotlib.pyplot as plt
import matplotlib

open_normal = 0

if open_normal == 1:
    with open("current_result_log.txt") as original_parameters:
        k2 = [[float(digit) for digit in line.split()] for line in original_parameters]
    k2 = np.asarray(k2)
    k2 = k2[k2[:,0]< 0.1 , :]
#    k2 = k2[k2[:,15] > 28.2 , :]
#    k2 = k2[k2[:,15] < 28.7 , :]
    k1 = k2

#print k1
if open_normal == 0:
    with open("mutant_log.txt") as original_parameters:
        k2 = [[float(digit) for digit in line.split()] for line in original_parameters]
    k2 = np.asarray(k2)
    k2 = k2[k2[:,6] > 1 , :] #Mutant factor less than this value
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
plt.hist(m2,100, alpha=0.5, label='Total PI ')
plt.hist(i1,100, alpha=0.5, label='PMPI ')
#plt.hist(i2,100, alpha=0.5, label='PI4P ')
#plt.hist(i3,100, alpha=0.5, label='PIP2 ')
#plt.hist(i4,100, alpha=0.5, label='DAG (after/before)')
#plt.hist(i5,100, alpha=0.5, label='PMPA ')
#plt.hist(i6,100, alpha=0.5, label='ERPA ')
#plt.hist(i7,100, alpha=0.5, label='CDPDAG ')
plt.hist(i8,100, alpha=0.5, label='ERPI ')

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

plt.xlabel('Ratio of steady states (cds/WT)')
plt.ylabel('Frequency')
plt.title('CDPDAGS overexpression')
#plt.axhline()
#plt.axvline()
plt.legend(loc='upper left', bbox_to_anchor=(1, 0.5))
plt.savefig('samplefigure.png', bbox_inches='tight')
plt.show()
