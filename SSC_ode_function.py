#ODE Function
from SSC_parameter_values import parameter_values
m2 = parameter_values()


def ode_function(y, t, vmax_table):
	v2 = vmax_table[0]
	v5 = vmax_table[1]
	v7 = vmax_table[2]
	v8 = vmax_table[3]
	v2i = vmax_table[4]
	v3i = vmax_table[4]
	v5i = vmax_table[4]
	v1 = (10.0*v5*v2)/((125.0*v2) - v5)  #Assuming Km of PITP is 10 times others
	v3 = (20.0*v5)/(125.0)
	v4 = v3
	v6 = (5.98*v5*v7)/((125.0*v7) - (5.98*v5))

	k1 = m2[0]
	k2 = m2[1]
	k2i = m2[2]
	k3 = m2[3]
	k3i = m2[4]
	k4 = m2[5]
	k5 = m2[6]
	k5i = m2[7]
	k6 = m2[8]
	k7 = m2[9]
	k8 = m2[10]


	pmpi = y[0]
	pi4p = y[1]
  	pip2 = y[2]
   	dag  = y[3]
	pmpa = y[4]
	erpa = y[5]
	cdpdag=y[6]
	erpi = y[7]

# the model equations
	f_pmpi = (v1*erpi)/(k1 + erpi) + (v2i*pi4p)/(k2i + pi4p) - (v2*pmpi)/(k2 + pmpi)
	f_pi4p = (v2*pmpi)/(k2 + pmpi) + (v3i*pip2)/(k3i + pip2) - (v2i*pi4p)/(k2i + pi4p) - (v3*pi4p)/(k3 + pi4p)
	f_pip2 = (v3*pi4p)/(k3 + pi4p) - (v3i*pip2)/(k3i + pip2) - (v4*pip2)/(k4 + pip2)
	f_dag =  (v4*pip2)/(k4 + pip2) + (v5i*pmpa)/(k5i + pmpa) - (v5*dag)/(k5 + dag)
	f_pmpa = (v5*dag)/(k5 + dag)   - (v5i*pmpa)/(k5i + pmpa) - (v6*pmpa)/(k6 + pmpa)
	f_erpa = (v6*pmpa)/(k6 + pmpa) - (v7*erpa)/(k7 + erpa)
	f_cdpdag = (v7*erpa)/(k7 + erpa) - (v8*cdpdag)/(k8 + cdpdag)
	f_erpi = (v8*cdpdag)/(k8 + cdpdag) - (v1*erpi)/(k1 + erpi)

	return [f_pmpi, f_pi4p, f_pip2, f_dag, f_pmpa, f_erpa, f_cdpdag, f_erpi]