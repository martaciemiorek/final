import csv
import matplotlib.pyplot as plt
import numpy as np


def write_stress_strain_to_csv(stress_strain, sample):
    ss = np.array(stress_strain)
    strain = ss[:, 0].tolist()
    stress = ss[:, 1].tolist()
    filename = F'{sample}stress_strain.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Stress [MPa]', 'Strain'])
        writer.writerows(zip(stress, strain))


def plot_graph(stress_strain, sample):
    ss = np.array(stress_strain)
    strain = ss[:, 0].tolist()
    stress = ss[:, 1].tolist()
    plt.plot(strain, stress)
    plt.title(f'{sample}')
    plt.xlabel('Strain')
    plt.ylabel('Stress [MPa]')
    #plt.show()
    plt.savefig(f'{sample}.jpg', format='jpg', dpi=300)

