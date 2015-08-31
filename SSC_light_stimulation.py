#August 2015
#Checking steady state parameters with light stimulation
#Warning: Parameter value file contains only Km Values

import math
import SSC_initial_conditions, SSC_ode_function, SSC_ode_function, SSC_parameter_values
import numpy as np
from scipy.integrate import odeint
#Parameter initializing
stimulation_factor = 170 #this will be change in PLC Vmax

#Open parameter values which gave correct results
with open("temp_file.txt") as original_parameters:
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

    #Initial Steady state
    y = SSC_initial_conditions.initial_conditions_vector()     # initial condition vector
    time_coord = SSC_initial_conditions.time_conditions()
    t  = np.linspace(time_coord[0], time_coord[1], 10000)   # time grid
    soln = odeint(SSC_ode_function.ode_function, y, t , args=(vmax_table,))

    #Light Stimulation
    y1 = soln[-1,:]  #Get all final concentrations, This will initial condition for next step
    t1 = np.linspace(time_coord[0], time_coord[2], 10000)
    stimulus_soln = odeint(SSC_ode_function.light_ode, y1, t1 , args=(vmax_table,stimulation_factor))
