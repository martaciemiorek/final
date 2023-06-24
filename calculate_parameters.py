import numpy as np

def calculate_UTS_UE():   #calculates Ultimate Tensile Strength and Total Elongation
    stress_strain = create_stress_strain_curve()
    stress = stress_strain[:,1]
    UTS = stress.max()
    UTS_index = np.where(stress_strain == value)
    UE = stress_strain[UTS_index,1]
    print(UTS)
    print(UE)

calculate_UTS_UE()

def calculate_YS(): #calculates Yield Strength and Uniform Elongation
    pass

