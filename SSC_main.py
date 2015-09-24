#August 2015
#Checking steady state parameters
#Warning: Parameter value file contains only Km Values

import math
import SSC_initial_conditions, SSC_ode_function, SSC_ode_function, SSC_parameter_values
import numpy as np
from scipy.integrate import odeint
#import matplotlib
#matplotlib.use('TkAgg') #For interactive plots
#import matplotlib.pyplot as plt
#Setting up Vmax table (These are all free parameters)
v_reversible = 0.01 #all Except laza
#Specify Range
conditions_true = 0 #Initialization

v2 = temp_v2 #PI4K
v4 = temp_v4 #PLC
v5 = temp_v5 #DAGK
v5i = temp_v5i #LAZA
v8 = temp_v8 #PIS
v_reversible = 0.01

#Check conditions if given parameters are giving any negative values
if ((20.0*v2) - v4) > 0 :
    if ((25.0*v4) - (4.0*v5)) > 0 :
        temp_value1 = v5i/(1 - ((4.0*v5)/(25.0*v4)))
        if ((3.34*temp_value1)-v4) > 0 :
            conditions_true = 1

if conditions_true == 1:
    vmax_table = [v2,v4,v5,v5i,v8,v_reversible] #Rest of Vmax will be set according to these values
    y = SSC_initial_conditions.initial_conditions_vector()     # initial condition vector
    time_coord = SSC_initial_conditions.time_conditions()
    t  = np.linspace(time_coord[0], time_coord[1], 10000)   # time grid
    soln = odeint(SSC_ode_function.ode_function_lazaro, y, t , args=(vmax_table,))
    pPMPI = soln[:, 0]
    pPI4P = soln[:, 1]
    pPIP2 = soln[:, 2]
    pDAG= soln[:, 3]
    pPMPA= soln[:, 4]
    pERPA= soln[:, 5]
    pCDPDAG= soln[:, 6]
    pERPI= soln[:, 7]

    all_concentrations_main = soln[-1,:]  #Get all final concentrations
    total_concentration_main = sum(all_concentrations_main)  #Total Concentration

    cPMPI = all_concentrations_main[0]
    cPI4P = all_concentrations_main[1]
    cPIP2 = all_concentrations_main[2]
    cDAG= all_concentrations_main[3]
    cPMPA= all_concentrations_main[4]
    cERPA= all_concentrations_main[5]
    cCDPDAG= all_concentrations_main[6]
    cERPI= all_concentrations_main[7]

    other_than_erpi = [ cPMPI, cPI4P, cPIP2, cDAG, cPMPA, cERPA, cCDPDAG ]
    total_pi = cPMPI + cERPI
    total_pa = cPMPA + cERPA
    other_than_cdpdag = [ total_pa, total_pi, cPI4P, cPIP2 ]


    j1 = [i1 for i1 in all_concentrations_main if i1 < 0 ] #Checking for negative values
    j2 = [i2 for i2 in other_than_erpi if i2 > cERPI ] #Checking Values greater than ERPI
    j3 = [i3 for i3 in other_than_cdpdag if i3 < cCDPDAG ] #Checking Values less than CDPDAG

    penalty_error = 0

    if len(j1) == 0:
        penalty_error = penalty_error -400
    if len(j2) == 0:
        penalty_error = penalty_error -10
    if len(j3) == 0:
        penalty_error = penalty_error -5

    #Error checking
    rpip2=cPIP2/(cERPI+cPMPI) #Should be 0.05
    rpi4p=cPI4P/(cERPI+cPMPI)  #Should be 0.05
    rpa= (cPMPA+cERPA)/(cERPI+cPMPI) #Should be 0.167
    rdag= (cDAG)/(cERPI+cPMPI) #Should be 0.008

    error_from_pip2 = (math.fabs(rpip2-0.05))/0.05
    error_from_pi4p = (math.fabs(rpi4p-0.05))/0.05
    error_from_pa = (math.fabs(rpa-0.167))/0.167
    error_from_dag = (math.fabs(rdag-0.008))/0.008

    ferror = error_from_pip2 + error_from_pi4p + error_from_pa + error_from_dag
    error_details = [error_from_pip2 ,error_from_pi4p, error_from_pa, error_from_dag]
    #Adding Penalty Error
    ferror = ferror + 415 + penalty_error

    #Saving results
    fh2 = open('lazaro_result_log.txt','a')
    write_con = np.array(all_concentrations_main).tolist()
    things_to_write = [ferror] + vmax_table + error_details + write_con
    things_to_write = [ float(round(elem1,3)) for elem1 in things_to_write ]
    fh2.write('\t'.join(str(k1) for k1 in things_to_write))
    fh2.write('\n')
    fh2.close()
    conditions_true = 0 #Reset
