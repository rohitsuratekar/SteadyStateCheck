#Parameter Values
original_parameters = open("SSC_para.txt", 'r')
m1 = original_parameters.read().split()
def parameter_values():
	k1 = m1[0]
	k1 = float (k1)
	k2 = m1[1]
	k2 = float (k2)
	k2i = m1[2]
	k2i = float (k2i)
	k3 = m1[3]
	k3 = float (k3)
	k3i = m1[4]
	k3i = float (k3i)
	k4 = m1[5]
	k4 = float (k4)
	k5 = m1[6]
	k5 = float (k5)
	k5i = m1[7]
	k5i = float (k5i)
	k6 = m1[8]
	k6 = float (k6)
	k7 = m1[9]
	k7 = float (k7)
	k8 = m1[10]
	k8 = float (k8)
	return [k1,k2,k2i,k3,k3i,k4,k5,k5i,k6,k7,k8]
