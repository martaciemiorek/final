import csv
import matplotlib.pyplot as plt


def write_stress_strain_to_csv(stress_strain, sample):
    ss = np.arraray(stress_strain)
    strain = ss[:, 0].tolist()
    stress = ss[:, 1].tolist()
    filename = F'{sample}stress_strain.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Stress [MPa]', 'Strain'])
        writer.writerows(zip(stress, strain))




def plot_graph():
    freq_force_array = force_by_frequency(frequency)
    stress_strain = create_stress_strain_curve(freq_force_array)
    strain, stress = zip(*stress_strain)
    plt.plot(strain, stress)
    plt.title("AlZn")
    plt.xlabel('Strain')
    plt.ylabel('Stress [MPa]')
    #plt.show()
    plt.savefig('AlZn.jpg', format='jpg', dpi=300)

plot_graph()