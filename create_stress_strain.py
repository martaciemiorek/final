import numpy as np


def create_stress_strain_curve(strain_array, force_array, cs): #calculates stress by dividing force by cross section and returns list of stress vs strain values
    stress_array = np.array(force_array) / float(cs)
    temp_strain = np.array(strain_array)
    stress_strain = np.concatenate((temp_strain, stress_array), dtype=float)
    return stress_strain

