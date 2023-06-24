import numpy as np
from open_samples import create_samples_data
from open_strain import create_array_from_strain_file
from calc_strain import calculate_strain
from open_force import create_force_list
from force_divided_by_frequency import force_by_frequency
from create_stress_strain import create_stress_strain_curve
from export import write_stress_strain_to_csv


frequency = 5 #int(input("Podaj częstotliwość zapisu zdjęć w Hz: "))
#Samples_list_path = input('nazwę pliku z listą próbek: ;)

samples_data = create_samples_data()
#print(samples_data)
samples_names = samples_data[0]
#print(samples_names)
cross_section = samples_data[1]
#print(cross_section)
#podaj DIC frequency
#podaj ścieżkę do pliku samples_list
def run_calc(samples_list, cross_section):
    for sample, cs in zip(samples_list, cross_section):
        strain_array = create_array_from_strain_file(sample)
        strain=calculate_strain(strain_array)
        create_force_list(sample)
        force_arr = create_force_list((sample))
        force_by_frequency(frequency, force_arr)
        print(force_by_frequency(frequency, force_arr))
        force_array = force_by_frequency(frequency, force_arr)
        stress_strain = create_stress_strain_curve(strain, force_array, cs)
        print(stress_strain)
        write_stress_strain_to_csv(stress_strain, sample)

run_calc(samples_names, cross_section)



# force_by_freq(frequency) -> force_array

# create_stress_strain(strain_array, force_array)
# save_stress_strain(create_stress_strain)
# plot_and_save(stress_strain)
# calculate_parameters(stress_strain)