import math
import SSC_initial_conditions, SSC_ode_function, SSC_ode_function, SSC_parameter_values
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib

with open("current_result_log.txt") as original_parameters:
    k2 = [[float(digit) for digit in line.split()] for line in original_parameters]
k2 = np.asarray(k2)
k2 = k2[k2[:,0]< 0.1 , :] #Select error less than 10%
k2 = k2[k2[:,10] > 25 , :] #Condition on PMPI
k2 = k2[k2[:,10] < 32 , :] #Condition on PMPI
#k2 = k2[k2[:,14] > 28 , :] #Condition on PMPA
k2 = k2[k2[:,14] < 12 , :] #Condition on PMPA
#k2 = k2[k2[:,15] < 10 , :] #Condition on ERPA
#k2 = k2[k2[:,10] < 26 , :]
m = np.random.randint(0,len(k2))
r = k2[m]
v2 = r[1]
v5 = r[2]
v7 = r[3]
v8 = r[4]
v1 = (10.0*v5*v2)/((125.0*v2) - v5)  #Assuming Km of PITP is 10 times others
v3 = (20.0*v5)/(125.0)
v4 = v3
v6 = (5.98*v5*v7)/((125.0*v7) - (5.98*v5))
para_values = [v1, v2, 0.01, v3, 0.01, v4, v5, 0.01, v6, v7, v8]
vmax_table = [v2,v5,v7,v8,0.01]
y = SSC_initial_conditions.initial_conditions_vector()
time_coord = SSC_initial_conditions.time_conditions()
t  = np.linspace(time_coord[0], time_coord[1], 10000)
soln = odeint(SSC_ode_function.ode_function, y, t , args=(vmax_table,))
all_concentrations_main = soln[-1,:]
pPMPI = soln[:, 0]
pPI4P = soln[:, 1]
pPIP2 = soln[:, 2]
pDAG= soln[:, 3]
pPMPA= soln[:, 4]
pERPA= soln[:, 5]
pCDPDAG= soln[:, 6]
pERPI= soln[:, 7]

all_concentrations_main = np.array(all_concentrations_main).tolist()

mfh2 = open('result_values.txt','a')
things_to_write = para_values + all_concentrations_main
things_to_write2 = [ elem1 for elem1 in things_to_write ]
mfh2.write('\t'.join(str(k1) for k1 in things_to_write2))
mfh2.write('\n')
mfh2.close()

plt.figure()
plt.plot(t, pPMPI, label='PMPI',linewidth=2.0)
plt.plot(t, pPI4P, label='PI4P',linewidth=2.0)
plt.plot(t, pPIP2, label='PIP2',linewidth=2.0)
plt.plot(t, pDAG, label='DAG',linewidth=2.0)
plt.plot(t, pPMPA, label='PMPA',linewidth=2.0)
plt.plot(t, pERPA, label='ERPA',linewidth=2.0)
plt.plot(t, pCDPDAG, label='CDPDAG',linewidth=2.0)
#plt.plot(t, cERPI, label='ERPI',linewidth=2.0)
plt.xlabel('Time (min)')
plt.ylabel('Concentration (uM)')
plt.title('Concentration Profile')
plt.legend(loc=0)
plt.legend(loc='upper left', bbox_to_anchor=(1, 0.5))
plt.savefig('python.png', bbox_inches='tight')
plt.show()
