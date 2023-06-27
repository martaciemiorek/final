from open_samples import create_samples_data
from open_strain import create_array_from_strain_file
from calc_strain import calculate_strain
from open_force import create_force_list
from force_divided_by_frequency import force_by_frequency
from create_stress_strain import create_stress_strain_curve
from export import write_stress_strain_to_csv
from export import plot_graph
from calculate_parameters import calculate_UTS_UE
from shift_strain import calculate_intersection
from shift_strain import substract_intersection
import csv
import os


frequency = int(input("Podaj częstotliwość zapisu zdjęć w Hz: "))
samples_file_path = input('Podaj ściezkę pliku z listą próbek: ')
file_name = os.path.basename(samples_file_path)

samples_data = create_samples_data(file_name)
samples_names = samples_data[0]
cross_section = samples_data[1]

def main(samples_list, cross_section, frequency):
    paramters = {'Sample': [], 'UTS [MPa]': [], 'UE': []}
    for sample, cs in zip(samples_list, cross_section):
        paramters['Sample'].append(sample)
        strain_array = create_array_from_strain_file(sample) # creates strain array
        strain=calculate_strain(strain_array)
        create_force_list(sample)  # creates force list
        force_arr = create_force_list(sample)
        force_array = force_by_frequency(frequency, force_arr) # creates force array adjusted to frequency
        stress_strain = create_stress_strain_curve(strain, force_array, cs) #creates stress - strain curve
        intersection = calculate_intersection(stress_strain) # if curve is shifted on X-axis, it is corrected
        if intersection >= 0.001:
            stress_strain = substract_intersection(stress_strain, intersection)
        write_stress_strain_to_csv(stress_strain, sample) # saves stress strain to .csv
        plot_graph(stress_strain, sample) # saves plot to .jpg
        UTS_UE = calculate_UTS_UE(stress_strain) # calcultes paramteters and creates table saved to .csv
        paramters['UTS [MPa]'].append(UTS_UE[0])
        paramters['UE'].append(UTS_UE[1])

    results = 'parameters.csv'
    keys = list(paramters.keys())
    values = list(paramters.values())
    transposed_values = zip(*values)
    with open(results, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(keys)
        writer.writerows(transposed_values)
    print("All done!")


if __name__ == "__main__":
  main(samples_names, cross_section, frequency)