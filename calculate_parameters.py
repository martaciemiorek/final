import numpy as np
#from scipy.stats import linregress

def calculate_UTS_UE(stress_strain):   #calculates Ultimate Tensile Strength and Total Elongation
    stress = stress_strain[:,1]
    strain = stress_strain[:,0]
    UTS = stress.max()
    UTS_index = np.where(stress_strain == UTS)[0]
    UE = strain[UTS_index]
    UE_list = UE.tolist()
    UTS_UE = [UTS, UE_list]
    return UTS_UE
    #print(UTS_UE)


# def calculate_E(stress_strain):
#     stress = stress_strain[:,1]
#     strain = stress_strain[:, 0]
#     UTS = stress.max()
#     mask = (0.4*UTS < stress) & (stress < 0.8 * UTS)
#     elastic_stress = stress[mask]
#     elastic_strain = strain[mask]
#     linear_regression = linregress(elastic_stress,elastic_strain)
#     intersection = linear_regression[1]
#     print(linear_regression)
#     print(intersection)
#     print(elastic_stress)
#     print(elastic_strain)




def calculate_YS(stress_strain): #calculates Yield Strength and Uniform Elongation

    pass
