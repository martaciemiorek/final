import numpy as np
def calculate_strain(strain_array): #calculates strain
    strain = np.array(strain_array, dtype=float)
    l0 = strain[0, 0] - strain[0, 1]
    delta_l = np.subtract(strain[1:-1, 0], strain[1:-1, 1]) - l0
    epsilon = delta_l / l0
    #print(epsilon.tolist())
    return epsilon.tolist()

#calculate_strain(strain_array)
