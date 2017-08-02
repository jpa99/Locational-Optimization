import scipy as sp

global M, N, k, m, Z, length;
m = 371650273390117;
M = 5; N = 5; k = 5; Z = 5;
length = M*N

def cost(LEDconfiguration):
	netirradiance = 0.0
	avgirradiance = 0.0
	neterrorsquared = 0.0
	sigma = 0;
	for target in range(length):
		point = [target%M, target//M]
		for LED in LEDconfiguration:
			LEDcoord = [LED%M,LED//M]; print(4);
			netirradiance += (Z**(m+1))/((((point[0]-LEDcoord[0])**2) + ((point[1]-LEDcoord[1])**2) + Z**2)**((m+3)/2));;
	avgirradiance = netirradiance/length;
	for target in range(length):
		point = [target%M, target//M]
		pointirradiance = 0
		for LED in LEDconfiguration:
			LEDcoord = [LED%M,LED//M]
			pointirradiance += (Z**(m+1))/((((point[0]-LEDcoord[0])**2) + ((point[1]-LEDcoord[1])**2) + (Z**2))**((m+3)/2))
		neterrorsquared+=((pointirradiance - avgirradiance)**2)
	sigma = (neterrorsquared/length)**(0.5)
	CVRMSE = sigma/avgirradiance
	return CVRMSE

print(cost([2, 5, 9, 16, 18]))
