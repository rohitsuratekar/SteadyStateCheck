import math
import SSC_initial_conditions, SSC_ode_function, SSC_ode_function, SSC_parameter_values
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib

with open("current_result_log.txt") as original_parameters:
    k2 = [[float(digit) for digit in line.split()] for line in original_parameters]
k2 = np.asarray(k2)
k2 = k2[k2[:,0]< 0.1 , :]
k2 = k2[k2[:,15] > 28.2 , :]
k2 = k2[k2[:,15] < 28.7 , :]
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

vmax_table = [v2,v5,v7,v8,v_reversible]
y = SSC_initial_conditions.initial_conditions_vector()
time_coord = SSC_initial_conditions.time_conditions()
t  = np.linspace(time_coord[0], time_coord[1], 10000)
soln = odeint(SSC_ode_function.ode_function, y, t , args=(vmax_table,))


mfh2 = open('result_values.txt','a')
things_to_write2 = para_values
things_to_write2 = [ float(round(elem1,3)) for elem1 in things_to_write2 ]
mfh2.write('\t'.join(str(k1) for k1 in things_to_write2))
mfh2.write('\n')
mfh2.close()

print r[0]
