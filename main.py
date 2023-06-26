from open_samples import create_samples_data
from open_strain import create_array_from_strain_file
from calc_strain import calculate_strain
from open_force import create_force_list
from force_divided_by_frequency import force_by_frequency
from create_stress_strain import create_stress_strain_curve
#from export import write_stress_strain_to_csv
#from export import plot_graph
#from calculate_parameters import calculate_UTS_UE
from shift_strain import calculate_intercept
from shift_strain import substract_intercept


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
def run_calc(samples_list, cross_section, frequency):
    paramteres =[]
    for sample, cs in zip(samples_list, cross_section):
        strain_array = create_array_from_strain_file(sample) # creates strain array
        strain=calculate_strain(strain_array)
        #print(strain)
        create_force_list(sample)  # creates force list
        force_arr = create_force_list((sample))
        #print(force_arr)
        force_array = force_by_frequency(frequency, force_arr) # creates force array adjusted to frequency
        #print(force_by_frequency(frequency, force_arr))
        stress_strain = create_stress_strain_curve(strain, force_array, cs) #creates stress - strain curve
        intercept = calculate_intercept(stress_strain) # if curve is shifted on X-axis, it is corrected
        print(intercept)
        #x = substract_intercept(stress_strain,intercept)
        #print (x)
        if intercept >= 0.01:
            stress_strain = substract_intercept(stress_strain, intercept)
            #print(stress_strain)
            return stress_strain
        else:
            #print(stress_strain)
            return stress_strain


        print(stress_strain)
        #print('-----------------')
        #write_stress_strain_to_csv(stress_strain, sample) # saves stress strain to .csv
        #plot_graph(stress_strain, sample) # saves plot to .jpg
        #calculate_UTS_UE(stress_strain) # calcultes paramteters and creates table saved to .csv
        #print(calculate_E(stress_strain))
run_calc(samples_names, cross_section, frequency)

