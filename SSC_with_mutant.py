#August 2015
#Checking steady state parameters with mutant data
#Warning: Parameter value file contains only Km Values

import math
import SSC_initial_conditions, SSC_ode_function, SSC_ode_function, SSC_parameter_values
import numpy as np
from scipy.integrate import odeint
#Setting up chang in parameter in mutation
change_factor_list = [0.01, 0.125, 0.25, 0.5, 1] #For rdgA
#change_factor_list = [0.01, 0.5, 1, 5, 10] #For PIS and CDPDAGS

#Open parameter values which gave correct results
with open("current_result_log.txt") as original_parameters:
    para_set = [[float(digit) for digit in line.split()] for line in original_parameters]

para_set = np.asarray(para_set)
para_set = para_set[para_set[:,0]< 0.1 , :]  #Take only values with error less than 10%

for para_elements in range(len(para_set)):

    current_para_set = para_set[para_elements,:] #Select rows
    v2 = current_para_set[1]
    v5 = current_para_set[2]
    v7 = current_para_set[3]
    v8 = current_para_set[4]
    v_reversible = 0.01
    vmax_table = [v2,v5,v7,v8,v_reversible] #Rest of Vmax will be set according to these values
    y = SSC_initial_conditions.initial_conditions_vector()     # initial condition vector
    time_coord = SSC_initial_conditions.time_conditions()
    t  = np.linspace(time_coord[0], time_coord[1], 10000)   # time grid
    soln = odeint(SSC_ode_function.ode_function, y, t , args=(vmax_table,))

    all_concentrations_main = soln[-1,:]  #Get all final concentrations
    save_before = np.array(all_concentrations_main).tolist()
    change_para = 6  #Changing DAGK Vmax

    for cf in change_factor_list :
            print change_para, cf
            change_factor = cf
            soln_mutant = odeint(SSC_ode_function.mutant_ode, y, t , args=(vmax_table,change_para, change_factor))
            mutant_concentration_all = soln_mutant[-1,:]  #Get all final concentrations
            save_after = np.array(mutant_concentration_all).tolist()
            #Saving results
            mfh2 = open('mutant_log.txt','a')
            things_to_write2 = vmax_table + [change_para] + [change_factor] + save_before + save_after
            things_to_write2 = [ float(round(elem1,3)) for elem1 in things_to_write2 ]
            mfh2.write('\t'.join(str(k1) for k1 in things_to_write2))
            mfh2.write('\n')
            mfh2.close()
