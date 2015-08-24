#Parameter Values
original_parameters = open("SSC_para.txt", 'r')
m1 = original_parameters.read().split()
def parameter_values():
	k1 = m1[11]
	k1 = float (k1)
	k2 = m1[12]
	k2 = float (k2)
	k2i = m1[13]
	k2i = float (k2i)
	k3 = m1[14]
	k3 = float (k3)
	k3i = m1[15]
	k3i = float (k3i)
	k4 = m1[16]
	k4 = float (k4)
	k5 = m1[17]
	k5 = float (k5)
	k5i = m1[18]
	k5i = float (k5i)
	k6 = m1[19]
	k6 = float (k6)
	k7 = m1[20]
	k7 = float (k7)
	k8 = m1[21]
	k8 = float (k8)
	return [k1,k2,k2i,k3,k3i,k4,k5,k5i,k6,k7,k8]
