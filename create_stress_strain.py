import numpy as np


def create_stress_strain_curve(strain_array, force_array, cs): #calculates stress by dividing force by cross section and returns list of stress vs strain values
    stress_array = np.array(force_array) / float(cs)
    temp_strain = np.array(strain_array)
    #len_stress = len(stress_array)
    len_strain = len(temp_strain)
    cut_stress_array = stress_array[0:len_strain]
    stress_strain = np.column_stack((temp_strain, cut_stress_array))
    return stress_strain

