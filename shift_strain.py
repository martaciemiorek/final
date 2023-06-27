from scipy.stats import linregress
import numpy as np
def calculate_intersection(stress_strain): #calculates E and return intercept for shifted data
    stress = stress_strain[:,1]
    strain = stress_strain[:, 0]
    UTS = stress.max()
    mask = (0.4*UTS < stress) & (stress < 0.8 * UTS)
    elastic_stress = stress[mask]
    elastic_strain = strain[mask]
    linear_regression = linregress(elastic_stress,elastic_strain)
    intersection = linear_regression[1]
    return intersection

def substract_intersection(stress_strain, intersection):
    stress = stress_strain[:, 1]
    strain = stress_strain[:, 0]
    corrected_strain = np.array(strain) - float(intersection)
    mask = (corrected_strain > 0)
    strain_masked = corrected_strain[mask]
    stress_masked = stress[mask]
    new_stress_strain = np.column_stack((strain_masked, stress_masked))
    return new_stress_strain
    #print(len(strain_mask))
    #print(len(stress_mask))

