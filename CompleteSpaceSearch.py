import itertools

global M, N, k, m, Z, length;
m = 31.371650273390117;
M = 5; N = 5; k = 5; Z = 5; # adjustible
length = M*N

def cost(LEDconfiguration):
	netirradiance = 0.0
	avgirradiance = 0.0
	neterrorsquared = 0.0
	sigma = 0;
	for target in range(length):
		point = [target%M, target//M]
		for LED in LEDconfiguration:
			LEDcoord = [LED%M,LED//M];
			netirradiance += (Z**(m+1))/\
                        ((((point[0]-LEDcoord[0])**2) + ((point[1]-LEDcoord[1])**2) + Z**2)**((m+3)/2));
	avgirradiance = netirradiance/length;
	for target in range(length):
		point = [target%M, target//M]
		pointirradiance = 0
		for LED in LEDconfiguration:
			LEDcoord = [LED%M,LED//M]
			pointirradiance += (Z**(m+1))/\
                        ((((point[0]-LEDcoord[0])**2) + ((point[1]-LEDcoord[1])**2) + (Z**2))**((m+3)/2))
		neterrorsquared+=((pointirradiance - avgirradiance)**2)
	sigma = (neterrorsquared/length)**(0.5)
	CVRMSE = sigma/avgirradiance
	return CVRMSE, LEDconfiguration

# itertools.combinations(M*N, k) generates all combinations of k elements from set {1, 2, ..., M*N-1}
combinations = itertools.combinations(range(length), k)

minimum = (1), #upper bound on CV(RMSE)

for combination in combinations:
    solution = cost(combination)
    if(solution[0] < minimum[0]):
        minimum = solution

print(minimum[0])

print(minimum[1])
