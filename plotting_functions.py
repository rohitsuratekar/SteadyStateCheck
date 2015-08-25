import numpy as np
import matplotlib.pyplot as plt
import matplotlib

with open("current_result_log.txt") as original_parameters:
    k2 = [[float(digit) for digit in line.split()] for line in original_parameters]
k2 = np.asarray(k2)
k2 = k2[k2[:,0]< 0.018 , :]
print k2
k1 = k2

#plt.scatter(k1[:,16],k1[:,0],color = 'k', label='CDPDAG',alpha=1)
#plt.scatter(k1[:,14],k1[:,0],color = 'y',label='PMPA',alpha=1)
#plt.scatter(k1[:,15],k1[:,0],color = 'c', label='ERPA',alpha=1)
#plt.scatter(k1[:,10],k1[:,0],color = 'b',label='PMPI',alpha=1)
#plt.scatter(k1[:,11],k1[:,0],color = 'r',label='PI4P',alpha=1)
#plt.scatter(k1[:,12],k1[:,0],color = 'g', label='PIP2',alpha=1)
#plt.scatter(k1[:,13],k1[:,0],color = 'm', label='DAG',alpha=1)

#plt.scatter(k1[:,0],k1[:,4],color = 'r', label='Error',alpha=1)
#plt.scatter(k1[:,1],k1[:,10])

#plt.hist(k1[:,10],100, alpha=0.5, label='PMPI')
#plt.hist(k1[:,11],100, alpha=0.5, label='PI4P')
#plt.hist(k1[:,12],100, alpha=0.5, label='PIP2')
#plt.hist(k1[:,13],100, alpha=0.5, label='DAG')
#plt.hist(k1[:,15],100, alpha=0.5, label='ERPA')
#plt.hist(k1[:,14],100, alpha=0.5, label='PMPA')
#plt.hist(k1[:,16],100, alpha=0.6, label='CDPDAG')
plt.hist(k1[:,0],100)

plt.xlabel('Error')
plt.ylabel('Frequency')
plt.title('With error smaller than 10%')
#plt.axhline()
plt.axvline()
plt.legend(loc='upper left', bbox_to_anchor=(1, 0.5))
plt.savefig('samplefigure.png', bbox_inches='tight')
plt.show()
