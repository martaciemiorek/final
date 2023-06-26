from scipy.stats import linregress
import numpy as np
def calculate_intercept(stress_strain): #calculates E and return intercept for shifted data
    stress = stress_strain[:,1]
    strain = stress_strain[:, 0]
    UTS = stress.max()
    mask = (0.4*UTS < stress) & (stress < 0.8 * UTS)
    elastic_stress = stress[mask]
    elastic_strain = strain[mask]
    linear_regression = linregress(elastic_stress,elastic_strain)
    intercept = linear_regression[1]
    return intercept
    #print(linear_regression)
    #print(intercept)
    #print(elastic_stress)
    #print(elastic_strain)

def substract_intercept(stress_strain, intercept):
    stress = stress_strain[:, 1]
    strain = stress_strain[:, 0]
    corrected_strain = np.array(strain) - int(intercept)
    mask = (strain >= 0)
    strain_mask = corrected_strain[mask]
    stress_mask = stress[mask]
    new_stress_strain = np.column_stack((strain_mask, stress_mask))
    return new_stress_strain
    #print(len(strain_mask))
    #print(len(stress_mask))

