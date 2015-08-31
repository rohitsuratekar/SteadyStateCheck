#August 2015
#Checking steady state parameters with light stimulation
#Warning: Parameter value file contains only Km Values
import matplotlib.pyplot as plt
import math
import SSC_initial_conditions, SSC_ode_function, SSC_ode_function, SSC_parameter_values
import numpy as np
from scipy.integrate import odeint
#Parameter initializing
pip2_depletion_value_table = [0.16, 1.6 , 8, 12.8] #Values of PIP2 after light stimulation (1%, 10%, 50%, 80%)

#Open parameter values which gave correct results
with open("temp_file.txt") as original_parameters:
    para_set = [[float(digit) for digit in line.split()] for line in original_parameters]

para_set = np.asarray(para_set)
para_set = para_set[para_set[:,0]< 0.1 , :]  #Take only values with error less than 10%

for pip2_depletion_value in range(len(pip2_depletion_value_table)):
    for para_elements in range(len(para_set)):

        current_para_set = para_set[para_elements,:] #Select rows
        v2 = current_para_set[1]
        v5 = current_para_set[2]
        v7 = current_para_set[3]
        v8 = current_para_set[4]
        v_reversible = 0.01
        vmax_table = [v2,v5,v7,v8,v_reversible] #Rest of Vmax will be set according to these values

        #Initial Steady state
        y = SSC_initial_conditions.initial_conditions_vector()     # initial condition vector
        time_coord = SSC_initial_conditions.time_conditions()
        t  = np.linspace(time_coord[0], time_coord[1], 10000)   # time grid
        soln = odeint(SSC_ode_function.ode_function, y, t , args=(vmax_table,))
        stored_pip2_value = soln[-1,2]
        #Light Stimulation
        #y1 = soln[-1,:]  #Get all final concentrations, This will initial condition for next step
        #t1 = np.linspace(time_coord[0], time_coord[2], 100)
        #stimulus_soln = odeint(SSC_ode_function.light_ode, y1, t1 , args=(vmax_table,stimulation_factor))

        #infinite Vmax of PLC
        y2=soln[-1,:]
        y2[3] = y2[3]+y[2] - pip2_depletion_value #DAG Value
        y2[2] = pip2_depletion_value #New PIP2 value
        #Recovery phase
        #y2 = stimulus_soln[-1,:]
        t2 = np.linspace(time_coord[0], time_coord[3], 10000)
        recovery_soln = odeint(SSC_ode_function.ode_function, y2, t2 , args=(vmax_table,))

        pip2_recovery = recovery_soln[:,2]
        percent90_value = stored_pip2_value*0.9
        recovery_time_array = t2 [pip2_recovery > percent90_value]
        if len(recovery_time_array) == 0:
            final_recovery_time = 1989
        if len(recovery_time_array) != 0:
            final_recovery_time = recovery_time_array[0]

        mfh2 = open('modified_light_recovery.txt','a')
        things_to_write2 = vmax_table + [pip2_depletion_value] + [final_recovery_time] 
        things_to_write2 = [ float(round(elem1,3)) for elem1 in things_to_write2 ]
        mfh2.write('\t'.join(str(k1) for k1 in things_to_write2))
        mfh2.write('\n')
        mfh2.close()
